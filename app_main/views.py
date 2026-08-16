from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from app_main.models import Todo


@login_required(login_url="/login/")
def home_page(request):
    todos = Todo.objects.filter(owner=request.user)
    return render(
        request=request,
        template_name='home_page.html',
        context={'todos': todos}
    )


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()
        username = request.POST.get("username", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        error_messages = []

        # 1. Majburiy maydonlarni tekshirish
        if not username or not email or not password1 or not password2:
            error_messages.append("'Username', 'Email', 'Parol' va 'Parolni tasdiqlash' maydonlari majburiy!")

        # 2. Username va Email bazada bor-yo'qligini tekshirish
        if User.objects.filter(username=username).exists():
            error_messages.append("Bunday 'Username' ga ega foydalanuvchi allaqachon mavjud.")

        if email and User.objects.filter(email=email).exists():
            error_messages.append("Bunday 'Email' allaqachon ro'yxatdan o'tgan.")

        # 3. Parol tekshiruvlari
        if password1 != password2:
            error_messages.append("Parollar bir-biriga mos kelmadi.")
        else:
            if len(password1) < 8:
                error_messages.append("Parol uzunligi kamida 8 ta belgidan iborat bo'lishi kerak.")
            if password1.isdigit():
                error_messages.append("Parol faqat raqamlardan iborat bo'la olmaydi (harf ham qatnashsin).")
            if password1.isalpha():
                error_messages.append("Parol faqat harflardan iborat bo'la olmaydi (raqam ham qatnashsin).")

        # Agar xatoliklar bo'lsa, qayta render qilish
        if error_messages:
            return render(request, "register.html", context={"error_messages": error_messages})

        # Xatolik bo'lmasa foydalanuvchini yaratish (create_user ishlatamiz)
        User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )
        return redirect("/login/")            

    return render(request, "register.html")


@login_required(login_url="/login/")
def new_todo(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        Todo.objects.create(
            owner=request.user,
            title=title,
            description=description,
        )
        return redirect('/')

    return render(request, "new_todo.html")


@login_required(login_url="/login/")
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    
    if todo.owner != request.user:
        return redirect("/")
    
    todo.delete()
    return redirect("/")


@login_required(login_url="/login/")
def todo_edit(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    
    if todo.owner != request.user:
        return redirect("/")

    if request.method == 'POST':
        todo.title = request.POST.get("title")
        todo.description = request.POST.get("description")
        todo.save()
        return redirect('/')

    return render(request, 'todo_edit.html', context={'todo': todo})


@login_required(login_url="/login/")
def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, owner=request.user)
    return render(request, 'todo_detail.html', context={'todo': todo})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(
        request=request,
        template_name='login_page.html',
    )


def logout_page(request):
    logout(request)
    return redirect('/login/')


def send_email(request):
    if request.method == "POST":
        recipient = request.POST.get("recipient")
        subject = request.POST.get("subject")
        body = request.POST.get("body")

        try:
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[recipient],
                fail_silently=False,
            )
            return HttpResponse("<h1>Email muvaffaqiyatli yuborildi!</h1>")
        except Exception as e:
            return HttpResponse(f"<h1>Xatolik yuz berdi:</h1> <p>{e}</p>")
        
    return render(request, "send_email.html")