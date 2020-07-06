from django.shortcuts import render
from django.http import HttpResponse
from .forms import LargeForm, SnippetForm


# Create your views here.
def formPost(request):
    if request.method == 'POST':
        form = LargeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name)
    form = LargeForm()
    return render(request, 'form.html', {'form': form})

def snippet_detail(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            # print('Valid')
           form.save()

    form = SnippetForm()
    return render(request, 'form.html', {'form': form})