from django.test import TestCase
from students.models import Student


# Create your model tests here.
class StudentTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Student.objects.create(student_id="G00001", first_name="Sally", last_name="McGuire", grade_level="K",
                               phone_number=5207057335, email="sally.mcguire@anyschool.com")

    def test_get_absolute_url(self):
        student = Student.objects.get(id=1)
        # this will also fail if the urlconf is not defined
        self.assertEquals(student.get_absolute_url(), '/students/student/1')

    def test_object_name_is_last_name_comma_first_name(self):
        student = Student.objects.get(id=1)
        expected_object_name = f'{student.last_name}, {student.first_name}'
        self.assertEquals(expected_object_name, str(student))

    def test_student_id_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('student_id').verbose_name
        self.assertEquals(field_label, 'student id')

    def test_student_id_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('student_id').max_length
        self.assertEquals(max_length, 15)

    def test_first_name_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_first_name_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 20)

    def test_last_name_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_last_name_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 20)
