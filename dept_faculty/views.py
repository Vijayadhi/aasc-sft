import csv
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.templatetags.static import static
from xhtml2pdf import pisa

from clg_admin.models import Semester, Faculty
from dept_admin.models import Courses, FacultyAllocation, SubjectAllocation
from dept_faculty.models import Students, AddAssessmentScore
from main_control.models import CustomUser


def render_to_pdf(template_src, context_dict={}):
    template = render_to_string(template_src, context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="score_report.pdf"'
    pisa_status = pisa.CreatePDF(template, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + template + '</pre>')
    return response


def generate_score_pdf(request, pk):
    score = get_object_or_404(AddAssessmentScore, pk=pk)

    # Extract student reg_nums from the scores dictionary
    student_reg_nums = score.scores.keys()

    # Query the Students model based on reg_nums
    students = Students.objects.filter(reg_num__in=student_reg_nums)

    # Create a dictionary mapping reg_num to student names
    students_dict = {student.reg_num: student.user.name for student in students}

    logo_url = request.build_absolute_uri(static('backend/assets/img/img.png'))

    # Prepare context for rendering the PDF
    context = {
        'course': score.subject.course,
        'batch': score.subject.batch,
        'subject': score.subject,
        'assessment': score.assessment,
        'semester': score.semester,
        'scores': score.scores,
        'student_dict': students_dict,
        'logo_url': logo_url,
        'month_year': score.month,
    }

    return render_to_pdf('dept_faculty/internal_pdf_template.html', context)


from django.contrib.auth.models import Group


def generatecummulative(request):
    semesters = Semester.objects.all()
    user_groups = request.user.groups.values_list("name", flat=True)  # Fetch only group names

    if "Class Tutor" in user_groups:
        user = Faculty.objects.get(user=request.user)
        class_tutor = FacultyAllocation.objects.filter(faculty=user).first()  # Use filter().first() to avoid errors

        context = {
            "semesters": semesters,
            "classes": class_tutor,
        }
        return render(request, "dept_faculty/generatecumulative.html", context)

    return render(request, "dept_faculty/generatecumulative.html")


def processmarklist(request):
    if request.method == "POST":
        semester_id = request.POST.get("semester")
        class_id = request.POST.get("classId")  # Ensure correct AJAX match

        if not semester_id or not class_id:
            return JsonResponse({"error": "Missing semester or class ID"}, status=400)

        # Retrieve the Faculty Allocation object
        try:
            allocation = FacultyAllocation.objects.get(id=class_id)
        except FacultyAllocation.DoesNotExist:
            return JsonResponse({"error": "Invalid class ID"}, status=404)

        # Retrieve Subject Allocations related to this class
        subject_allocations = SubjectAllocation.objects.filter(course=allocation.course, batch=allocation.batch)

        # Retrieve Assessment Scores based on semester & subject allocation
        scores = AddAssessmentScore.objects.filter(
            semester_id=semester_id,
            subject__in=subject_allocations  # Matching subjects in the subject allocations
        )

        # Serialize the data
        scores_data = list(scores.values("id", "subject__subject__name", "assessment__name", "scores", "month"))

        return JsonResponse({"message": "Mark list processed successfully!", "data": scores_data}, status=200)

    return JsonResponse({"message": "Invalid request method"}, status=405)


import csv
from django.http import HttpResponse
from .models import AddAssessmentScore

import csv
from django.http import HttpResponse
from .models import AddAssessmentScore, Students  # Import Student model

def fetch_student_marks(request):
    assessment_ids = request.GET.get("assessments", "").split(",")

    if not assessment_ids or assessment_ids == [""]:
        return HttpResponse("No assessments selected.", status=400)

    # Fetch assessment scores for selected assessments
    scores = AddAssessmentScore.objects.filter(id__in=assessment_ids).select_related("subject", "assessment")

    if not scores.exists():
        return HttpResponse("No data available.", status=400)

    # Prepare CSV response
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="Cumulative_Mark_List.csv"'

    writer = csv.writer(response)

    # Get subject name and assessment names dynamically
    subject_name = scores.first().subject.subject.name
    assessment_names = [score.assessment.name for score in scores]

    # Write Header
    writer.writerow(["Subject", subject_name])
    writer.writerow(["Assessments"] + assessment_names)
    writer.writerow([])  # Empty row
    writer.writerow(["Reg Number", "Student Name"] + assessment_names + ["Total", "Average", "Marks Out of 25"])

    # Process student marks
    student_data = {}

    # Fetch student names from the Student model
    student_names = {student.reg_num: student.user.name for student in Students.objects.all()}

    for score in scores:
        scores_dict = score.scores  # Directly using JSONField (already a dictionary)

        for reg_num, marks in scores_dict.items():
            marks = int(marks)  # Convert string marks to integer

            if reg_num not in student_data:
                student_name = student_names.get(reg_num, f"Unknown ({reg_num})")  # Lookup student name
                student_data[reg_num] = {
                    "name": student_name,
                    "marks": [],
                    "total": 0
                }

            student_data[reg_num]["marks"].append(marks)
            student_data[reg_num]["total"] += marks

    # Write student data to CSV
    for reg_num, data in student_data.items():
        total = data["total"]
        average = total / len(data["marks"])
        marks_out_of_25 = round((average / 100) * 25, 2)

        writer.writerow([reg_num, data["name"]] + data["marks"] + [total, round(average, 2), marks_out_of_25])

    return response
