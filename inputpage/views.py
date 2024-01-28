from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import g4f
g4f.debug.logging = True  # Enable debug logging
g4f.debug.version_check = False  # Disable automatic version checking

def home(request):
    if request.method=='POST':
        userinput=request.POST.get('user_input','')
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content":userinput}],
        )
        context={
        'response':response
        }
        return render(request,'inputpage/inputpage.html',context)
    else:
        return render(request,'inputpage/inputpage.html')
