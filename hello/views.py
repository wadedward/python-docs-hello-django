from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hi Angela, Today - Monday October 16th, Its in the evening time, While we are learning AZURE Cloud Computing[AZ900] & its very very interesting :-) ~!! I cant stop thinking about falling in love with you again.")
