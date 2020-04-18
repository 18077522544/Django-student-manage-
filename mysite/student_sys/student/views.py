from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from .forms import StudentForm
from django.urls import reverse


def index(request):

    students = Student.objects.all()
    # print('------------------'+type(students))
    if request.method == 'POST':
        form = StudentForm(request.POST)
    else:
        form = StudentForm(request.GET)
        if form.is_valid():
            # cleaned_data =form.cleaned_data
            # student = Student()
            # student.name = cleaned_data['name']
            # student.sex = cleaned_data['sex']
            # student.email = cleaned_data['email']
            # student.profession = cleaned_data['profession']
            # student.qq = cleaned_data['qq']
            # student.phone = cleaned_data['phone']
            # student.save()
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            form = StudentForm()

    context = {
        'students': students,
        'form': form,
    }
    return render(request, 'index.html', context=context)

