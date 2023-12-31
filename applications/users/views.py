from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib.admin.models import ADDITION, LogEntry
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse

from django.views.generic import ListView

from django.views.generic import (
    View,
    CreateView,
    UpdateView
)

from django.views.generic.edit import (
    FormView
)

from .forms import (
    UserRegisterForm, 
    LoginForm,
    UpdatePasswordForm,
    VerificationForm,
    UserCreateForm,
    UserUpdateForm
)
#
from .models import User, LogSesion, Asistencia
# 
from .functions import code_generator
from django.template.defaulttags import register


class UserRegisterView(LoginRequiredMixin, FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        # generamos el codigo
        codigo = code_generator()
        #
        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],
            ocupation=form.cleaned_data['ocupation'],
            # codregistro=codigo
        )
        # enviar el codigo al email del user
        asunto = 'Confrimacion d eemail'
        mensaje = 'Codigo de verificacion: ' + codigo
        email_remitente = 'cristian.perezs@cun.edu.co'
        #
        send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'],])
        # redirigir a pantalla de valdiacion

        return HttpResponseRedirect(
            reverse(
                'users_app:user-verification',
                kwargs={'pk': usuario.id}
            )
        )

class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)

class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )
class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)


class CodeVerificationView(FormView):
    template_name = 'users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:user-login')

    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk'],
        })
        return kwargs

    def form_valid(self, form):
        #
        User.objects.filter(
            id=self.kwargs['pk']
        ).update(
            is_active=True
        )
        return super(CodeVerificationView, self).form_valid(form)

class PasswordResetByUser(PasswordChangeView):
  template_name = 'users/update.html'
  success_url = '/'

class CargoListview(ListView):
    template_name = "users/panel.html"
    model = User
    paginate_by = 100  # if pagination is desired

class PanelListView(ListView):
    template_name = "panel.html"
    model = User

class UsersClienteView(ListView):
    model = User
    template_name = "users/cliente.html"
        

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        queryset   = User.objects.filter(d_i__icontains = kword, roles = 1)[:5]
        return queryset   
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        contexto = super().get_context_data(**kwargs)
        contexto ['count_users'] = self.get_queryset().count
        
        return contexto
    
    
    
class UserCreateView(LoginRequiredMixin, CreateView):
    form_class = UserCreateForm
    template_name = "users/create_user.html"
    success_url = reverse_lazy('users_app:users-cliente')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.roles = 1
        self.object.cliente_id_clie = 1
        
        self.object.save()
        return super(UserCreateView, self).form_valid(form)
        
class UserClienteUPdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "users/update_user_cliente.html"
    success_url = reverse_lazy('users_app:users-cliente')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'].fields['cliente'].queryset = User.objects.filter(cliente_id_clie=self.request.user.cliente.id_clie)   
    #     return context

class LogSesionListView(ListView):
    template_name = "users/logs_davivienda.html"
    model = LogSesion
    paginate_by = 10
    

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        queryset = LogSesion.objects.filter(cliente = "Davivienda", documento__contains = kword).order_by("-id")
        return queryset
    
class logpruebaListView(ListView):
    template_name = "users/logs_prueba.html"
    model = LogEntry
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        queryset = LogEntry.objects.filter(
            user__cliente = 1, user__username__contains = kword
            )
        return queryset 
    
    
@login_required
def exportusers(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow([
        'USUARIO', 'NOMBRE', #1
        'APELLIDO', 'DOCUMENTO' #2
          ])

    base = User.objects.filter(cliente__r_s = "Davivienda").values_list(
       'username', 'nombres',  #1      
       'apellidos', 'd_i', #2 
        )
    
    for guia in base:
        
        writer.writerow(guia)
        
        response['Content-Disposition'] = 'attachment; filename="informe.csv"'

    return response

# class UsersClienteView(ListView):
#     model = User
#     template_name = "users/cliente.html"
    
    
################### ASISTENCIA #################

class AsistenciaCreateView(LoginRequiredMixin, CreateView, ListView):
    template_name = "users/asistencia.html"
    model = Asistencia
    fields = ['check',]
    success_url = reverse_lazy('users_app:asistencia')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(AsistenciaCreateView, self).form_valid(form)
    
