from django.shortcuts import get_object_or_404
from .models import Country

def global_data(request):
    data = Country.objects.all()

    isMobile = "Mobile" in request.META.get('HTTP_USER_AGENT', '')
    if isMobile:
        # Do something if the request is coming from a mobile device
        isMobile = True
    else:
        # Do something if the request is not coming from a mobile device
        isMobile = False

    return {
        'data': data,
        'isClosed': False,
        'isMobile': isMobile,
        'showResults': False
    }
