from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render_to_response

from django.views.generic import ListView
from django.views.generic.edit import FormView
from main.models import Master, Reception, Human, MasterUsl, ContactsForm, Stock
from main.forms import ReceptionForm, UserCreateForm, UserForm, ProfileForm, ContactsForms,StockForm
from django.http import JsonResponse
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404


from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.

def mainPage(request, category_slug=None):
    stock = Stock.objects.all()

    if request.method == 'POST':

        stockform = StockForm(request.POST)
        if stockform.is_valid():
            stockform.save()

            messages.success(request, f'Спасибо за запись, скоро с Вами свяжется администратор!')

            return HttpResponseRedirect('/#zapis')
    else:
        stockform = StockForm()

    return render(request, 'pages/main.html', {
        'stockform': stockform,
        'stock': stock,
    })


def aboutPage(request, category_slug=None):
    return render(request, 'pages/about_us.html')



def blogPage(request, category_slug=None):
    stock = Stock.objects.all()

    if request.method == 'POST':
        stockform = StockForm(request.POST)
        if stockform.is_valid():
            stockform.save()

            messages.success(request, f'Спасибо за запись, скоро с Вами свяжется администратор!')
            return HttpResponseRedirect('/blog#zapis')
    else:
        stockform = StockForm()
    return render(request, 'pages/blog.html', {
        'stockform': stockform,
        'stock': stock
    })




def pricesPage(request, category_slug=None):
    return render(request, 'pages/prices.html')


def contactsPage(request, category_slug=None):
    if request.method == 'POST':

        formCont = ContactsForms(request.POST)
        if formCont.is_valid():
            person = formCont.cleaned_data.get('person')
            mail = formCont.cleaned_data.get('mail')
            message = formCont.cleaned_data.get('message')
            cont = ContactsForm(person=person, mail=mail, message=message)
            cont.save()
            messages.success(request, f'Все прошло успешно')
            return HttpResponseRedirect('/contacts')
    else:
        formCont = ContactsForms()
    return render(request, 'pages/contacts.html', {'formCont': formCont})



class MasterList(ListView):
    model = Master
    template_name='pages/reserv.html'
    context_object_name = 'masters'

class ReceptionView(FormView):
    form_class = ReceptionForm
    template_name = 'pages/reception.html'

    def form_valid(self, form):
        fcd = form.cleaned_data
        curr_master=Master.objects.get(id= self.kwargs['master_id'])
        usl= MasterUsl.objects.filter(master= self.kwargs['master_id']);
        response_dict={"form":form,
                       "master":curr_master,
                       "curr_date":fcd['date'],
                       "curr_time":fcd['time'],
                       "uslugi":fcd['uslugi'],
                       "cost":fcd['cost'],

                       "person_id":fcd['person_id'],
                       # "usl":usl,

                       }
        # условие для предотвращения записи на одно и то же время
        if Reception.objects.filter(date=fcd['date'],time=fcd['time'],master=curr_master).count()==0:
            Reception.objects.create(date=fcd['date'],time=fcd['time'],
                                     client_name=fcd['client_name'],
                                     client_info=fcd['client_info'],
                                     master=curr_master,
                                     # uslugi = usl,
                                     uslugi = fcd['uslugi'],
                                     cost = fcd['cost'],
                                     person_id = fcd['person_id'],
                                     )
            return render(self.request,'pages/reception.html', response_dict)
        else:
            response_dict["message"]="Вы уже зарегистрированны на это время"
            return render(self.request,'pages/reception.html', response_dict)

    def get_context_data(self, **kwargs):
        context = super(ReceptionView, self).get_context_data(**kwargs)
        context['master']=Master.objects.get(id= self.kwargs['master_id'])
        context['usl']= MasterUsl.objects.filter(master= self.kwargs['master_id']);

        return context


def date_from_ajax (request):
    if request.method == "POST" and request.is_ajax():
        master=Master.objects.get(id= request.POST.get("master_id"))
        reception_set=master.reception_set.filter(date=request.POST.get("date_from_ajax"))
        time_list=[]
        for reception in reception_set:
            time_list.append(reception.time)
        return JsonResponse({'time_list':time_list})

class MainUserView(TemplateView):
    template_name = 'pages/authuser.html'

    def get(self, request):
        if request.user.is_authenticated:
            humans = Human.objects.all()
            ctx = {}
            ctx['humans'] = humans
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


class RegisterFormView(FormView):

    form_class = UserCreateForm
    success_url = "/login/"
    template_name = "pages/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView,self).form_invalid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "pages/login.html"
    success_url = "/"
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")



def a_change_password(request):
    if request.method == "POST":
        forms = PasswordChangeForm(request.user, request.POST)
        if forms.is_valid():
            user = forms.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль успешно изменен')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Пожалуйста исправьте ошибки')
    else:
        forms = PasswordChangeForm(request.user)
    return render(request, 'shop/product/change_password.html', {
        'forms': forms,
    })


def person(request, category_slug=None):

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        # profile_form = ProfileForm(request.POST, instance=request.user.userprofile)

        if user_form.is_valid():
        # if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            # profile_form.save()
            messages.success(request, ('Ваш профиль был успешно обновлен!'))
            return HttpResponseRedirect('/personal-page')
        else:
            messages.success(request, ('Пожалуйста исправьте ошибки!'))

    else:
        user_form = UserForm(instance=request.user)
        # profile_form = ProfileForm(instance=request.user.userprofile)

    u = User.objects.get(username=request.user)
    listZakaz = Reception.objects.filter(person_id = request.user)
    # phone = u.userprofile.phone
    # imagePerson = u.userprofile.avatar
    # usl = MasterUsl.objects.filter(master=self.kwargs['master_id']);

    if request.method == "POST":
        formsPass = PasswordChangeForm(request.user, request.POST)
        if formsPass.is_valid():
            user = formsPass.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль успешно изменен')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Пожалуйста исправьте ошибки')
    else:
        formsPass = PasswordChangeForm(request.user)

    return render(request, 'pages/personal-page.html', {
        # 'phone': phone,
        # 'imagePerson': imagePerson,
        'formsPass': formsPass,
        'user_form': user_form,
        # 'profile_form': profile_form,
        'listZakaz': listZakaz,
    })