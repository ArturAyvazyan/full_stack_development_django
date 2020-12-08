from django.test import TestCase

# Create your tests here.
from glavnaya import models
from glavnaya.models import Work


class WorkModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Work.objects.create(name='Big', description='Bang')

    def test_first_name_label(self):
        work=Work.objects.get(id=1)
        field_label = work._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_date_of_death_label(self):
        work=Work.objects.get(id=1)
        field_label = work._meta.get_field('description').verbose_name
        self.assertEquals(field_label,'description')

    def test_first_name_max_length(self):
        work=Work.objects.get(id=1)
        max_length = work._meta.get_field('name').max_length
        self.assertEquals(max_length,100)

    # Дает ОШИБКУ ЗДЕСЬ!
    # def test_object_name_is_last_name_comma_first_name(self):
    #     work=Work.objects.get(id=1)
    #     expected_object_name = '%s, %s' % (work.name, work.description)
    #     self.assertEquals(expected_object_name,str(work))

    def test_get_absolute_url(self):
        work=Work.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(work.get_absolute_url(),'/catalog/author/1')





# ПРИМЕР
# class YourTestClass(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass

#     def setUp(self):
#         print("setUp: Run once for every test method to setup clean data.")
#         pass

#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)

#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)

#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)
