from django.shortcuts import render
from enroll.models import User
from django.http import HttpResponse,HttpResponseRedirect
from .forms import Studentregistration



#The Function for add & show
def add_show(request):
    if request.method == 'POST':
        form = Studentregistration(request.POST) 
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            form = Studentregistration()
    else:
        form = Studentregistration()
    stu = User.objects.all()
    context= {

        'form': form,
        'stu' :stu,
    }

    return render(request, 'enroll/addandshow.html', context)

#Update Data
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(id=id)
        fm = Studentregistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(id=id)
        fm = Studentregistration(instance=pi)

    context = {
        'id' :id,
        'fm' : fm,
    }
    return render(request,'enroll/updatestudent.html',context)


#This function will Delete
def delete_data(request,id):
    stu = User.objects.get(id=id)
    stu.delete()
    return HttpResponseRedirect('/')
