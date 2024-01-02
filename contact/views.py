from django.shortcuts import render, HttpResponsePermanentRedirect
from .models import Contact
from urllib.parse import parse_qs
# Create your views here.
def send(request):
    if request.method == "POST":
        data = wsgiRequestToDict(request)
        print(data)
        result = Contact(
            name=data['name'],
            email= data['email'],
            phone=data['phone'],
            subject=data['subject'],
            message=data['message']
            )
        result.save()
        print(result)
    return HttpResponsePermanentRedirect('/')
    

def wsgiRequestToDict(the_request):
    data = parse_qs(the_request.body.decode('utf-8'))
    data_dict = {key: value[0] for key, value in data.items()}
    return data_dict