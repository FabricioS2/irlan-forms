from django.shortcuts import render
from .forms import QuestionForm 

# Create your views here.


def create(request):
   if request.method == "POST":
       form = QuestionForm(request.POST)
       if form.is_valid():
           question = Question()
           question.question_text = form.cleaned_data['question_text']
           question.pub_date = datetime.datetime.now()
           question.save()
           return HttpResponseRedirect(reverse('index'))
       #else:
   form = QuestionForm()
   return render(request, 'create.html', {'form': form})
