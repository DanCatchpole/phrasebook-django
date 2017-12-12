from django.shortcuts import redirect

from .models import UserLanguage


class FirstLoginMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated:
            langs = UserLanguage.objects.filter(user=request.user)
            if langs.__len__() == 0:
                return redirect('phrasebook:first_login')
        return self.get_response(request)

    def get_response(self, request):
        pass
