from django.conf import settings # import the settings file

def doc_link(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'DOCUMENTATION_LINK': settings.DOCUMENTATION_LINK}