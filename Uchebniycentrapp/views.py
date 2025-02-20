from django.shortcuts import render
from Uchebniycentrapp.models import Course, Student
from django.http import HttpResponse

def home(request):
    return HttpResponse("Главная страница")


def cours(request):
    courses = Course.objects.all()
    students = Student.objects.all()

    context = {
        "courses": courses,
        "students": students,
        "title": "Course and Students"
    }
    return render(request, 'app.html', context)



def category(request,id):
    courses = Course.objects.filter(id=id)
    students = Student.objects.all()

    context = {
        "courses": courses,
        "students": students,
        "title": "Course and Students"
    }
    return render(request, 'index.html', context)




#
#
# def cours(request):
#     courses = Course.objects.all()
#     context = {
#         "courses":courses,
#         "title":"Course title"
#     }
#     return render(request,'index.html',context=context)
#
# def student(request):
#     students = Student.objects.all()
#
#     context = {
#         "students":students,
#         "title":"full_name"
#     }
#     return render(request, "index.html", context=context)
#
