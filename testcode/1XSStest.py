
#KZ: THis is the Python script to run the XSS attack

from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpRequest
from LegacySite.models import *
from LegacySite.views import *
import json

class XSSTest(TestCase):
     def setUp(self):
          self.client = Client()


     def XSSTest_1(self):
#KZ: utilizing XSS attack - taken from our XSS attack file - http://127.0.0.1:8000/gift?director=<script>alert("Congratulations! You Won!")</script>
          product = Product.objects.create(product_name = 'test', product_image_path= 'test', recommended_price = 1, description = 'test')
          response = self.client.get('/gift' , {'director' : '<script>alert("Congratulations! You Won!")</script>'})
          self.assertContains(response, "&lt;script&gt;alert(&quot;Congratulations! You Won!&quot;)&lt;/script&gt;", status_code=200)
