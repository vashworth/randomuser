from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone

@view_function
def process_request(request):
    json_response = ""
    context = {
        'response': json_response,
    }
    return request.dmp.render('index.html', context)
