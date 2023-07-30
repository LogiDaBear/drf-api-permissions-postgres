from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Cereal


class CerealTests(TestCase):

  @classmethod
  def setUpTestData(cls):
    testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
    testuser1.save()

    test_thing = Cereal.objects.create(name="rake", owner=testuser1, description="Better for collecting leaves than shovel.")
    test_thing.save()
    
    test_thing2 = Cereal.objects.create(name="shovel", owner=testuser1, description="Better for digging than rake.")
    test_thing2.save()

  def test_things_model(self):
    thing = Cereal.objects.get(id=1)
    actual_owner = str(thing.owner)
    actual_name = str(thing.name)
    actual_description = str(thing.description)
    self.assertEqual(actual_owner, "testuser1")
    self.assertEqual(actual_name, "rake")
    self.assertEqual(actual_description, "Better for collecting leaves than shovel.")
    
  def test_things_2(self):
    thing = Cereal.objects.get(id=2)
    actual_owner = str(thing.owner)
    actual_name = str(thing.name)
    actual_description = str(thing.description)
    self.assertEqual(actual_owner, "testuser1")
    self.assertEqual(actual_name, "shovel")
    self.assertEqual(actual_description, "Better for digging than rake.")