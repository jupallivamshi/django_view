from django.shortcuts import render
import datetime


def dt(request):
    dte=datetime.datetime.now()
    name='vamshi'
    rollno=7
    marks=99.99
    my_dict={'date':dte,'name':name,'roll.no':rollno,'marks':marks}
    return render(request,'html/vapp1.html',my_dict)