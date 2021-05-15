#KZ: This is the script that runs the HTTPS check/test to see if we are secure from HTTP-based attacks

from django.test import TestCase, Client
from django.urls import reverse
from LegacySite.models import *
from LegacySite.views import *
from django.http import HttpRequest
import json
import io

class HTTPtest(TestCase):
     def setUp(self):
          self.client = Client()


     def http_test(self):
#KZ: Easy test, if the server at HTTPS can be reached, that means that HTTPS has been implemented. If not, we are still running HTTP
          response = self.client.get('https://localhost:8000')
          assert(response.status_code == 200)

