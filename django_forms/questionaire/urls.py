from .views import (
    thanks_view,
    questionaireA,
    SampleFormView,
    SFCreateView,
    process_something
)
    
from django.urls import path

urlpatterns = [
    path('', questionaireA, name='quiz-a'),
    path('sample/', SampleFormView.as_view(), name='sample_form'),
    # inside .as_view() - we can add properties like .as_view(greeting="G'day")
    path('sample2/', SFCreateView.as_view(), name='sample_form2'),
    path('ajax/sample2/', process_something, name='ajax_sample2'),
    path('thanks/', thanks_view, name='thanks')
]