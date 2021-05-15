#KZ: This is the django file for running the CSRF attack - implemented with the csrf fiel 

from django.test import TestCase, Client
from django.urls import reversex
from django.http import HttpRequest
from LegacySite.models import *
from LegacySite.views import *
import json

class CSRFAttack(TestCase):
     def setUp(self):
          self.client = Client()


     def csrf_attack(self):
#KZ: Using the POST information we stored in the attack - http://127.0.0.1:8000/buy.html?director=<form action="http://127.0.0.1:8000/gift/0" method="POST"><input type="hidden" name="amount" value="2000"/><input type="hidden" name="username" value="hacker"/><input type="submit" value="More Info"/></form>
          '''
          <form action="http://127.0.0.1:8000/gift.html" method="POST">
            <input type="hidden" name="username" value="free_gift_card_attacker"/>
            <input type="hidden" name="amount" value="$5000"/>
          </form>
          '''
          product = Product.objects.create(product_name = 'test', product_image_path= 'test', recommended_price = 1, description = 'test')
          response = self.client.get('/buy' , {'director' : 'form action="http://127.0.0.1:8000/gift/0" method="POST"><input type="hidden" name="amount" value="2000"/><input type="hidden" name="username" value="hacker"/><input type="submit" value="More Info"/></form>'})
          self.assertContains(response, "form action=&quot;http://127.0.0.1:8000/gift/0&quot; method=&quot;POST&quot;&gt;&lt;input type=&quot;hidden&quot; name=&quot;amount&quot; value=&quot;2000&quot;/&gt;&lt;input type=&quot;hidden&quot; name=&quot;username&quot; value=&quot;hacker&quot;/&gt;&lt;input type=&quot;submit&quot; value=&quot;More Info&quot;/&gt;&lt;/form&gt;", status_code=200)
          