from django.test import TestCase
from .models import MyModel

class MyModelTest(TestCase):
    def setUp(self):
        MyModel.objects.create(name="Test", description="Test description")

    def test_my_model_creation(self):
        obj = MyModel.objects.get(name="Test")
        self.assertEqual(obj.description, "Test description")

from django.urls import reverse

class MyViewsTest(TestCase):
    def setUp(self):
        self.obj = MyModel.objects.create(name="Test", description="Test description")

    def test_index_view(self):
        response = self.client.get(reverse('myapp:index'))
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        response = self.client.get(reverse('myapp:detail', args=[self.obj.id]))
        self.assertEqual(response.status_code, 200)
