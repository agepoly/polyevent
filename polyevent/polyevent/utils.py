from django.http import HttpResponse
import json

def generate_api_response(data):
    return HttpResponse(json.dumps(data), content_type='text/json')
