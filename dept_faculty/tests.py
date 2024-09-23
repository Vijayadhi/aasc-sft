from django.test import TestCase, override_settings

from config.settings import BASE_DIR
from dept_faculty.models import Students, CustomUser, Batch, Courses, Department
from django.contrib.auth.models import Group



class StudentsModelTest(TestCase):

    @override_settings(DATABASES={'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }})
    def setUp(self):
        # Create a Batch object
        self.batch = Batch.objects.create(
            batch_from_date='2023',
            batch_to_date='2025'
        )

        self.department, created = Department.objects.get_or_create(id=3, defaults={'name': 'Department of ComputerScience'})
        print(self.department)
        # Create a Courses object
        self.course = Courses.objects.create(
            name='B. Sc Info Tech',
            department=self.department,
        )

        # Create a student group if it doesn't already exist
        self.student_group, created = Group.objects.get_or_create(name='Student')

    def test_add_30_students(self):
        # Add 30 student objects to the Students model
        for i in range(1, 31):
            user = CustomUser.objects.create_user(
                username=f'student{i}',
                email=f'student{i}@example.com',
                password='password123',
                name=f'Student {i}'
            )
            student = Students.objects.create(
                user=user,
                reg_num=f'REG{i:03}',
                batch=self.batch,
                course=self.course
            )

            # Check if the student is saved successfully and belongs to the 'Student' group
            self.assertEqual(student.user.groups.filter(name='Student').exists(), True)

        # Verify that 30 students have been created
        self.assertEqual(Students.objects.count(), 30)
