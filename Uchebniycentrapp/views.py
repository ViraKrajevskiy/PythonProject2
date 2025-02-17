from django.shortcuts import render

from Uchebniycentrapp.models import Course, Student


def cours(request):
    courses = Course.objects.all()
    context = {
        "courses":courses,
        "title":"Course title"
    }
    return render(request,"index.html",context=context)

def student(request):
    students = Student.objects.all()

    context = {
        "students":students,
        "title":"full_name"
    }
    return render(request, "index.html", context=context)

