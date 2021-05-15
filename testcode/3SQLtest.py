#KZ: SQL Injection - we use the open areas to try and get an admin password

from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpRequest
from LegacySite.models import *
from LegacySite.views import *
import json
import io

class SQLTest(TestCase):
     def setUp(self):
          self.client = Client()


     def sql_test(self):
        try:
#KZ: Here, we implement the union vulnerability, while also creating a generic username/password
            response =""
            password = 'Pepper1234'
            SaltyCustomer = User.objects.create(username='SaltyCustomer', password='Pepper1234')
#KZ: dummyProduct = Product.objects.create(product_name = 'test', product_image_path= 'test', recommended_price = 1, description = 'test')
#KZ dummyCard = Card.objects.create(id = 1, data= '123,34'.encode(), product = dummyProduct, amount = 95, fp='/tmp/addedcard_2_1.gftcrd',user=SaltyCustomer,used=1)
            
            data = io.StringIO {"merchant_id": "NYU Apparel Card", "customer_id": "SaltyCustomer", "total_value": "1999", "records": [{"record_type": "amount_change", "amount_added":2000, "signature": "' UNION select password from LegacySite_user where username = 'admin' || '"}]}
            #data = io.StringIO('{"merchant_id": "NYU Apparel Card", "customer_id": "SaltyCustomer", "total_value": "1999", "records": [{"record_type": "amount_change", "amount_added":2000, "signature": "[]"}]}')
                        filename="tests/Attack3-Injection_Attack.gftcrd"

            response = self.client.post('/use.html', {'card_data': data, 'filename' : filename, 'card_supplied': True, 'card_fname': 'test'},)
            #KZ: Commenting out these lines when not in use
            #print(response.content)
            #open("test.html","w").write(response.content.decode('utf-8'))
            #self.assertNotContains(response, password)
            
            raise Exception('dummy exception')
        except Exception as ex:
            if response != "" and password in response.content.decode('utf-8'):
                self.assertNotContains(response, password)
            else:
                assert 1==1
            



