from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from.models import Student
import codecs
# Create your views here.

def getindex(request):
    user = Student.objects.all()
    context ={
        'user':user,

    }
    return render(request, 'index.html', context)

def getfile(request):
    if request.method == 'POST':
        post=codecs.iterdecode(request.FILES['file'], 'utf-8')
        send = Student.generatefromcsv(post)

        redirect('index')
    return render(request, 'upload_form.html')