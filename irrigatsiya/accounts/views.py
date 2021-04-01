
from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
    )
from .models import Profile
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages

# class RegisterView(UserRegisterForm):
#     template_name = "register.html"
#     form_class = UserRegisterForm
#     def form_valid(self, form):
#         form.save()
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password1")
#         messages.info(f'Hey {username}, We are glad to see you here!Try our tutorials!')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return redirect("courses")

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            messages.info(request, f'Hey {username}, Account has been created!')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("profile")
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

@login_required
def profile (request):
    if request.method=="POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm( request.POST, request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request, "profile.html", context)

class ProfileView(LoginRequiredMixin, DetailView, FormView):    
    template_name = 'profile.html'    
    #queryset = User.objects.all()    
    
    # def get_object(self):        
    #     id_ = self.kwargs.get("username")        
    #     user = get_object_or_404(Profile, username=id_)     # User, username=id_   
    #     return user
    form_class = ProfileUpdateForm
    second_form_class = UserUpdateForm
    success_url = 'profile'

    def get_queryset(self):
        self.user = get_object_or_404(Profile, name=self.kwargs['pk'])
        return Profile.objects.filter()

    def get_context_data(self, **kwargs): 
        context = super(ProfileView, self).get_context_data(**kwargs)
        if 'u_form' not in context:
            context['u_form'] = self.form_class(request = self.request)
        if 'p_form' not in context:
            context['p_form'] = self.form_class(request = self.request)
        return context

    def form_invalid(self, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        self.object = self.get_queryset()
        if 'form' in request.POST:
            form_class = self.get_form_class()
            form_name = 'u_form'
        else:
            form_class = self.second_form_class
            form_name = 'p_form'
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(**{form_name:form})            
    # def u_form_form_valid(self, form):
    #     return super().form_valid(form)
    
    # def get_context_data(self, *args, **kwargs):
    #     super(Profile, self).get_context_data(*args, **kwargs)
    #     context = {
    #         'user': self.request.user
    #     }
    #     return context
    # def p_form_form_valid(self, form):
    #     return super().form_valid(form)
    
    

# @login_required
# def profile (request):
#     context = {
#             'user': request.user
#         }
#     return render(request, "profile.html", context)