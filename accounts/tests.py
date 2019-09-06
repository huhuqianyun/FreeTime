from django.test import TestCase

# Create your tests here.
import requests
from django.http import HttpRequest
base_url = 'http://127.0.0.1:8000/polls'
r = requests.get(base_url)
code = r.status_code
# text = r.text
print(code)
# print(text)
