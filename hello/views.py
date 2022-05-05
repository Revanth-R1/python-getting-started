from django.http import HttpResponse
from notify_run import Notify

def index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = ""
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    notify = Notify()
    notify.send(ip, 'https://notify.run/ywD5ejvGueujiNzm6SxF')
    #sending ip
    return HttpResponse(ip)
