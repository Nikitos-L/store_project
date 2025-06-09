from django.http import HttpResponse
from django.shortcuts import redirect

from subscriptions.models import UserSubscriptions


class RequestCheckSubsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (request.path.startswith('/products/api/orders/') and not
        UserSubscriptions.objects.filter(user__username=request.user.username).exists()):
            # return HttpResponse("Доступ только пользователям с подпиской", status=400)
            return redirect('http://127.0.0.1:8000/api-auth/login/?next=/products/api/')
        response = self.get_response(request)
        return response

    # def process_exception(self, request, exception):
    #     print(exception)