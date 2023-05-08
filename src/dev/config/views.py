from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin

from .utils import execute


class StartPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {
            'a': 1,
            'b': '2',
        })

    def post(self, request):
        button_name = request.POST.get('button', '')
        if button_name == 'DB':
            return redirect(reverse('db_exec'))
        return render(request, 'home.html')


class DbPage(UserPassesTestMixin, View):
    '''
    Shows page of db executor, that can execute sql queries inner python code
    For debugging purposes
    Available only for advanced admin users
    '''

    def test_func(self) -> bool | None:
        return self.request.user.is_admin

    def get(self, request):
        return render(request, 'db_ex.html')

    def post(self, request):
        query = request.POST['query']
        params = request.POST['params']

        if query == '':
            return render(request, 'db_ex.html', context={
                'errors': ['Query must not be empty'],
                'query': query,
                'params': params
            })

        result = execute(query, params.split('\r\n'))
        if result[0] is False:
            return render(request, 'db_ex.html', context={
                'errors': [str(result[1])],
                'query': query,
                'params': params
            })

        return render(request, 'db_ex.html', context={
            'table_decription': result[2],
            'data': result[1],
            'query': query,
            'params': params,
        })
