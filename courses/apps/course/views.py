from django.shortcuts import render, redirect
from ..login.models import *
from models import *
from django.contrib import messages
# Create your views here.
def loggedin(request, id):
    if request.session.get('id') == None:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    context = {
        'user': user
    }
    return render(request , 'loggedin.html', context)

def courses(request, id):
    user = User.objects.get(id=request.session['id'])
    all_courses = Course.objects.all()
    liked = User.objects

    context = {
        'user': user,
        'all_courses': Course.objects.all(),
    }
    return render(request, 'courses.html', context)

def add(request, id):
    #print "wtf"
    user = User.objects.get(id=request.session['id'])
    context = {
        'user': user
    }
    return render(request, 'create.html', context)

def view(request, id, course_id):
    user = User.objects.get(id=request.session['id'])
    course = Course.objects.get(id=course_id)
    context = {
        'user': user,
        'course': course,
    }
    return render(request, 'view.html', context)

def creating(request, id):
    course_name = request.POST['name']
    course_description = request.POST['description']

    id = request.session['id']
    errors = Course.objects.validate_course(request.POST)
    user = User.objects.get(id=request.session['id'])

    if len(errors):
        print "errors!!! ALERT"
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/{}/add'.format(id))
    else:
        print "it added it?"

        description = Description.objects.create(description=course_description)
        Course.objects.create(course_name=course_name, description=description, creator=user)
        print "passe through?"

        return redirect('/{}/courses'.format(id))

def update(request, id, course_id):
    user = User.objects.get(id=request.session['id'])
    context = {
        'user': user,
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'update.html', context)

def updating(request, id, course_id):
    user = User.objects.get(id=request.session['id'])
    all_courses = Course.objects.all()
    print Course.objects.get(id=course_id).description.description

    #updating Course Name
    #b = Course.objects.get(id=course_id)
    #b.course_name= request.POST['course_name']
    #b.description= request.POST['description']
    #b.save()

    #description = Description.objects.get(id=request.session['id']).update(description=request.POST['description'])
    #Course.objects.get(id=request.session['id']).update(course_name=request.POST['course_name'], description=description)
    
    #Course.objects.filter(id=course_id).update(description=request.POST['description'])

    print "updating"
    return redirect('/{}/courses'.format(id))

def like(request, id, course_id):
    course = Course.objects.get(id=course_id)
    user = User.objects.get(id=request.session['id'])
    course.likers.add(user)
    return redirect('/{}/courses'.format(id))

def unlike(request, id, course_id):
    course = Course.objects.get(id=course_id)
    user = User.objects.get(id=request.session['id'])
    course.likers.remove(user)
    return redirect('/{}/courses'.format(id))

def delete(request, id, course_id):
    print "deleting"
    b = Course.objects.get(id=course_id)
    b.delete()
    return redirect('/{}/courses'.format(id))
