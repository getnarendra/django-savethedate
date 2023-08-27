from django.shortcuts import render, redirect
from save_the_date import forms
# from .forms import SaveTheDateForm
from django.http import HttpResponse, Http404
from .forms import SaveTheDateCreateForm, SaveTheDateForm, SaveTheDateUpdateForm, SaveTheDateDeleteForm
from .models import SaveTheDate
from django.views import i18n
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import QuestionForm  # Create a forms.py file for your forms

def questions_list(request):
    questions = Question.objects.all()
    return render(request, 'questions_list.html', {'questions': questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'question_detail.html', {'question': question})


def date_create(request):
    if request.method == 'POST':
        form = SaveTheDateCreateForm(request.POST)
        if form.is_valid():
            print("first_text_print : ", form.cleaned_data['first_name']) 
            print("email_print : ", form.cleaned_data['email']) 
            form.save()
            return redirect('save_the_date')
    else:
        form = SaveTheDateForm()
    return render(request, 'savedate_add_form.html', {'form': form})

def date_update(request, pk):
    save_the_date = get_object_or_404(SaveTheDate, pk=pk)
    if request.method == 'POST':
        form = SaveTheDateUpdateForm(request.POST, instance=save_the_date)
        if form.is_valid():
            form.save()
            return redirect('save_the_date')
    else:
        form = SaveTheDateForm(instance=save_the_date)
    return render(request, 'savedate_add_form.html', {'form': form, 'save_the_date': save_the_date})

def date_delete(request, pk):
    # save_the_date = get_object_or_404(SaveTheDate, pk=pk)
    save_the_date = get_object_or_404(SaveTheDate, pk=pk)
    if request.method == 'POST':
        save_the_date.delete()
        return redirect('save_the_date')
    return render(request, 'savedate_confirm_delete.html', {'save_the_date': save_the_date})



def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            print("question_text_print : ", form.cleaned_data['question_text']) 
            print("pub_date_print : ", form.cleaned_data['pub_date']) 
            form.save()
            return redirect('questions_list')
    else:
        form = QuestionForm()
    return render(request, 'question_form.html', {'form': form})

def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('questions_list')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'question_form.html', {'form': form, 'question': question})

def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        question.delete()
        return redirect('questions_list')
    return render(request, 'question_confirm_delete.html', {'question': question})



def default_view(request):
    return render(request, 'default.html')

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def questions(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def save_the_date_create(request):
    form = SaveTheDateCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('save_the_date_list')
    return render(request, 'save_the_date_create.html', {'form': form})

# def save_the_date(request):
#     if request.method == 'POST':
#         form = SaveTheDateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('save_the_date_success')
#     else:
#         form = SaveTheDateForm()
#     return render(request, 'save_the_date.html', {'form': form})

# def save_the_date_success(request):
#     return render(request, 'save_the_date_success.html')


# def index(request):
#     return render(request, 'save_the_date.html')

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def save_the_date(request):
#     try:
#         savethedate = SaveTheDate.objects.get()
#     except SaveTheDate.DoesNotExist:
#         raise Http404("Date does not exist")
#     return render(request, "save_the_date.html", {"savethedate": savethedate})

def save_the_date(request):
    try:
        savethedates = SaveTheDate.objects.all()
    except SaveTheDate.DoesNotExist:
        raise Http404("Date does not exist")
    return render(request, "save_the_date.html", {"savethedates": savethedates})


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "detail.html", {"question": question})