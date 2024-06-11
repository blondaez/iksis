from django.contrib.auth import login, authenticate
from django.core.checks import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from datetime import date

from .forms import SignUpForm, LoginForm, UpdateInfoForm, ServiceForm, ProcedureRecordForm, BlogForm
from .models import UserProfile, Service, ProcedureRecord, Blog


def index(request):
    return render(request, 'main/index.html')


def blog(request):
    return render(request, 'main/blog.html')


def blog_entry(request):
    return render(request, 'main/blog_entry.html')


def inject(request):
    return render(request, 'main/inject.html')


def estet(request):
    return render(request, 'main/estet.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_profile') if not user.is_staff else redirect('admin_profile')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


@login_required
def admin_profile(request):
    if not request.user.is_staff:
        return redirect('user_profile')
    today = date.today()
    today_records = ProcedureRecord.objects.filter(date=today, active=True)
    return render(request, 'main/admin_profile.html',{'today_records': today_records})


@login_required
def user_profile(request):
    if request.user.is_staff:
        return redirect('admin_profile')

    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_records = ProcedureRecord.objects.filter(client_profile=user_profile)

    return render(request, 'main/user_profile.html', {
        'user': user_profile,
        'user_records': user_records,
    })

def profile_info(request):
    return render(request, 'main/profile_info.html')


@login_required
def profile_info(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UpdateInfoForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UpdateInfoForm(instance=user_profile)

    return render(request, 'main/profile_info.html', {'form': form})


def service_new(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_profile')
    else:
        form = ServiceForm()
    return render(request, 'main/service_new.html', {'form': form})


def record_new(request):
    if request.method == 'POST':
        form = ProcedureRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_profile')
    else:
        form = ProcedureRecordForm()
    return render(request, 'main/record_new.html', {'form': form})


@login_required
def records_free(request):
    inactive_records = ProcedureRecord.objects.filter(active=False, response=False)
    return render(request, 'main/records_free.html', {'inactive_records': inactive_records})


@login_required
def book_record(request, record_id):
    record = get_object_or_404(ProcedureRecord, id=record_id)
    user_profile = getattr(request.user, 'userprofile', None)

    if request.method == 'POST':
        record.client_profile = user_profile
        record.response = True
        record.save()
        return redirect('records_free')

    return render(request, 'main/records_free.html',
                  {'inactive_records': ProcedureRecord.objects.filter(active=False, response=False)})


@login_required
def records_response(request):
    response_records = ProcedureRecord.objects.filter(response=True, confirmed=False)
    return render(request, 'main/records_response.html', {'response_records': response_records})


@login_required
def book_response_record(request, record_id):
    record = get_object_or_404(ProcedureRecord, id=record_id)
    if request.method == 'POST':
        record.confirmed = True
        record.save()
        return redirect('records_response')
    return render(request, 'main/records_response.html', {'response_records': ProcedureRecord.objects.filter(response=True, confirmed=False)})


@login_required
def records_today(request):
    today = date.today()
    today_records = ProcedureRecord.objects.filter(date=today, active=True)
    return render(request, 'main/records_today.html', {'today_records': today_records})


@login_required
def complete_record(request, record_id):
    record = get_object_or_404(ProcedureRecord, id=record_id)
    if request.method == 'POST':
        record.completed = True
        record.active = False
        record.save()
        return redirect('records_today')


@login_required
def cancel_record(request, record_id):
    record = get_object_or_404(ProcedureRecord, id=record_id)
    if request.method == 'POST':
        record.cancelled = True
        record.active = False
        record.save()
        return redirect('records_today')


@login_required
def records_all(request):  # странцица "Все записи"
    records_all = ProcedureRecord.objects.filter(active=True, cancelled=False)
    return render(request, 'main/records_all.html', {'records_all': records_all})


@login_required
def cancel_record_all(request, record_id):  # обработка отмены записи на странице "Все записи"
    record = get_object_or_404(ProcedureRecord, id=record_id)
    if request.method == 'POST':
        record.cancelled = True
        record.active = False
        record.save()
        return redirect('records_all')


def blog_new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = BlogForm()

    return render(request, 'main/blog_new.html', {'form': form})


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'main/blog.html', {'blogs': blogs})


def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'main/blog_detail.html', {'blog': blog})
