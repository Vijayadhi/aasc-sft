from django.core.management.base import BaseCommand
from dept_faculty.models import Students, CustomUser, Batch, Courses, Department
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Populate the database with students'

    def handle(self, *args, **kwargs):
        department, created = Department.objects.get_or_create(id=3, defaults={'name': 'CSE'})
        batch, created = Batch.objects.get_or_create(id=1 )
        course, created = Courses.objects.get_or_create(name='B.Sc Info Tech', defaults={'department': department})

        for i in range(1, 31):
            user = CustomUser.objects.create_user(
                username=f'student{i}',
                email=f'studentit{i}@example.com',
                password='password123',
                name=f'Student {i}'
            )
            student = Students.objects.create(
                user=user,
                reg_num=f'REG{i:03}',
                batch=batch,
                course=course
            )

            student_group, created = Group.objects.get_or_create(name='Student')
            user.groups.add(student_group)

            self.stdout.write(self.style.SUCCESS(f'Successfully created {student.user.name} with reg_num {student.reg_num}'))
