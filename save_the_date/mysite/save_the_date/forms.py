from django.forms import ModelForm
# from bootstrap_datepicker_plus import DatePickerInput  # Import the widget
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.contrib.admin.widgets import AdminDateWidget
# from bootstrap_datepicker_plus import DateTimePickerInput
from save_the_date.models import SaveTheDate

from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }        
        # widgets = {
        #     'pub_date': DateTimePickerInput,  # Use DatePickerInput widget
        # }
        # pub_date = forms.DateField()
        # pub_date = forms.DateField(widget=AdminDateWidget())

class SaveTheDateForm(forms.ModelForm):
    class Meta:
        model = SaveTheDate
        fields = '__all__' #  ['question_text', 'pub_date']
        widgets = {
            'event_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }    

class SaveTheDateCreateForm(ModelForm):
    class Meta:
        model = SaveTheDate
        fields = '__all__'

class SaveTheDateUpdateForm(ModelForm):
    class Meta:
        model = SaveTheDate
        fields = '__all__'

class SaveTheDateDeleteForm(ModelForm):
    class Meta:
        model = SaveTheDate
        fields = '__all__'
