from django.shortcuts import render
from django.http.response import HttpResponseRedirect



def main(request):
    return render(request, 'main_page/test.html')