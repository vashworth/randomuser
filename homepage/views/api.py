from homepage import models as m
from django_mako_plus import view_function
import json
from django.forms.models import model_to_dict
from django.core import serializers

@view_function
def process_request(request):
    json_response = ""
    if (request.method == 'GET'):
        try:
            #check for api key
            test = m.APIKey.objects.get(key=request.GET.get('key'))

            #get person by googleID
            person = m.Person.objects.get(googleID=request.GET.get('googleID'))

            #return as json
            person_dict = model_to_dict( person )
            json_response = json.dumps(person_dict)

        except m.Person.DoesNotExist:
            #get all people
            people = m.Person.objects.all()
            #return as json
            people_json = serializers.serialize('json', people)
            json_response = people_json

        except m.APIKey.DoesNotExist:
            json_response = "Invalid api key"

    elif (request.method == 'POST'):
        try:
            #check for api key
            test = m.APIKey.objects.get(key=request.GET.get('key'))
            #get person by id
            person = m.Person.objects.get(googleID=request.GET.get('googleID'))

            person.googleID = request.GET.get('googleID')
            person.first_name = request.GET.get('first_name')
            person.last_name = request.GET.get('last_name')
            person.email = request.GET.get('email')
            person.company = request.GET.get('company')
            person.cell_phone = request.GET.get('cell_phone')
            person.home_phone = request.GET.get('home_phone')
            person.work_phone = request.GET.get('work_phone')
            person.home_address = request.GET.get('home_address')
            person.work_address = request.GET.get('work_address')
            person.spouse = request.GET.get('spouse')
            person.bio = request.GET.get('bio')
            person.img_url = request.GET.get('img_url')
            person.positions = request.GET.get('positions')

            if (person.googleID is not None):
                person.save()
                json_response = "Updated person"

        except m.APIKey.DoesNotExist:
            json_response = "Invalid api key"
        except m.Person.DoesNotExist:
            p = m.Person()
            p.googleID = request.GET.get('googleID')
            p.first_name = request.GET.get('first_name')
            p.last_name = request.GET.get('last_name')
            p.email = request.GET.get('email')
            p.company = request.GET.get('company')
            p.cell_phone = request.GET.get('cell_phone')
            p.home_phone = request.GET.get('home_phone')
            p.work_phone = request.GET.get('work_phone')
            p.home_address = request.GET.get('home_address')
            p.work_address = request.GET.get('work_address')
            p.spouse = request.GET.get('spouse')
            p.bio = request.GET.get('bio')
            p.img_url = request.GET.get('img_url')
            p.positions = request.GET.get('positions')

            if (p.googleID is not None):
                p.save()
                json_response = "Created new person"

    context = {
        'response': json_response,
    }
    return request.dmp.render('index.html', context)
