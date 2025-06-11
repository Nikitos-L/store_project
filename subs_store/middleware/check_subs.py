from django.http import HttpResponse
from django.shortcuts import redirect

from subscriptions.models import UserSubscriptions


class RequestCheckSubsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (request.path.startswith('/products/api/orders/') and not
        UserSubscriptions.objects.filter(user=request.user.id).exists() and
        request.user.username != 'admin'):
            # return HttpResponse("Доступ только пользователям с подпиской", status=400)
            return redirect('http://127.0.0.1:8000/api-auth/login/?next=/products/api/')
        response = self.get_response(request)
        return response