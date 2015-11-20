from django.shortcuts import render_to_response
from django.template import Context
from models import People

"""
 C4
"""

def add_people(request):
    if request.POST:
        post = request.POST
        new_people = People(\
            name = post["name"],\
            stu_id = post["stu_id"],\
            phone = post["phone"],\
            email = post["email"],\
            qq = post["qq"],\
            address = post["address"],\
            birth_date = post["birth_date"])
        if post["sex"] == 'M':
            new_people.sex = True
        else:
            new_people.sex = False
        new_people.save()
    count = People.objects.all().count()
    c = Context({"count":count})
    return render_to_response("add_people.html", c)

def view_all(request):
    people_list = People.objects.all()
    c = Context({"people_list":people_list,})
    return render_to_response("view_all.html", c)
    
