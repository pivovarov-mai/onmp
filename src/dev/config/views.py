from django.views import View
from django.shortcuts import render


class StartPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {
            'a': 1,
            'b': '2',
        })
