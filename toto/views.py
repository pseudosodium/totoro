from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        return render(request, "toto/home.html",
        {"ques":Question.objects.filter(author=request.user),
        "ans":Answer.objects.filter(author=request.user),
        "allQues":Question.objects.all().order_by('-datePublished')})
    else:
        return render(request, 'toto/home.html')

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request,user)
            messages.info(request, f"Your are now logged in as: {username}")
            return redirect("/")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request, "toto/register.html", {"form":form})

    form = NewUserForm
    return render(request, "toto/register.html", {"form":form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Your are now logged in as: {username}")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, "toto/login.html", {"form":form})

def logout_request(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("/")

def view_profile(request):
    return render(request, "toto/account.html", {"user":request.user})

def ask_question(request):
    if request.method == 'POST':
        try:
            form = QuestionForm(request.POST)
            if form.is_valid():
                ques = form.save(commit=False)
                ques.author = request.user
                ques.save()
                messages.success(request, "Questions asked successfully!")
                return redirect('/')
        except:
            form = QuestionForm(request.POST)
            messages.info(request, "A similar question already exists! Try checking that out first!")
            return redirect('/')

    form = QuestionForm()
    return render(request, 'toto/ask.html', {'form':form})

def single_slug(request, single_slug):
    ques_slug = [q.question_slug for q in Question.objects.all()]
    if single_slug in ques_slug:
        matching_ans = Answer.objects.filter(title__question_slug=single_slug)
        ans_url = {}
        return render(request, 'toto/qna.html', {'ques':Question.objects.filter(question_slug=single_slug), 'ans':matching_ans, 'slug':single_slug})

    return HttpResponse(f"We couldnt find anything with '{single_slug}'")

def ans_question(request, single_slug):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.author = request.user
            ques = Question.objects.filter(question_slug=single_slug)
            for q in ques:
                ans.title = q
            ans.save()
            messages.success(request, "Questions answered successfully!")
            return redirect('/')
    form = AnswerForm()
    return render(request, 'toto/ans.html', {'form':form})

def delete_ques(request, single_slug):
    Question.objects.filter(question_slug=single_slug).delete()
    messages.success(request, 'Question deleted successfully!')
    return redirect('/')
