from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Neigbourhood,Business

# Create your tests here.

class NeigbourhoodTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_Neigbourhood =Neigbourhood()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_Neigbourhood,Neigbourhood))



class BusinessTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_business =Business()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))

    #Testing Save Method
    def test_save_method(self):
    
        business = Business.objects.all()
        self.assertFalse(len(business)>0)

