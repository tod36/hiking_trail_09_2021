from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView

from mountain.forms import UserRegisterForm, UserLoginForm, TrailForm
from mountain.models import Trail, Difficulty
from mountain.utils import MyMixin


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Success registration')
            return redirect('home')
        else:
            messages.error(request, 'Wrong')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


class HomeTrail(MyMixin, ListView):
    model = Trail
    template_name = 'home_trails_list.html'
    context_object_name = 'trails'
    # mixin_prop = 'hello tourist'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mixin_prop'] = self.get_prop()
        return context


class TrailsByDifficulty(MyMixin, ListView):
    model = Trail
    template_name = 'home_trails_list.html'
    context_object_name = 'trails'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Difficulty.objects.get(pk=self.kwargs['difficulty_id']))
        return context

    def get_queryset(self):
        return Trail.objects.filter(difficulty_id=self.kwargs['difficulty_id']).select_related(
            'difficulty')


class ViewTrail(ListView):
    model = Trail
    context_object_name = 'trails'
    template_name = 'trails_list.html'
    pk_url_kwarg = 'trails_id'


class TrailUpdateView(UpdateView):
    model = Trail
    fields = '__all__'
    template_name = 'trail_update_form.html'
    # success_url = 'home_trail_list.html'


class TrailDetailView(DetailView):
    template_name = 'trail_detail.html'
    model = Trail
    context_object_name = 'trails'


class TrailDeleteView(DeleteView):
    template_name = 'trail_check_delete.html'
    model = Trail
    success_url = reverse_lazy('home')


class TrailCreateView(CreateView):
    form_class = TrailForm
    template_name = 'trail_create_form.html'
    raise_exception = True
