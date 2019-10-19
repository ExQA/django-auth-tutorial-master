from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from my_project.calc_operations import calc_object


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def calculator(request):
    ctx = {}
    ctx['operations'] = calc_object.keys()

    if request.method == 'GET':
        print(calc_object.keys())
    elif request.method == 'POST':
        try:
            first_num = float(request.POST.get('first_num').strip())
            operation = request.POST.get('operation')
            second_num = float(request.POST.get('second_num'))
            result = calc_object[operation](first_num, second_num)
            ctx['result'] = result
        except(ValueError, ZeroDivisionError, ) as e:
            ctx['msg'] = e
    return render(request, 'calculator.html', ctx)


def calculator_non_auth(request):
    ctx = {}
    ctx['operations'] = calc_object.keys()

    if request.method == 'GET':
        print(calc_object.keys())
    elif request.method == 'POST':
        try:
            first_num = float(request.POST.get('first_num').strip())
            operation = request.POST.get('operation')
            second_num = float(request.POST.get('second_num'))
            result = calc_object[operation](first_num, second_num)
            ctx['result'] = result
        except(ValueError, ZeroDivisionError, ) as e:
            ctx['msg'] = e
    return render(request, 'calculator.html', ctx)
