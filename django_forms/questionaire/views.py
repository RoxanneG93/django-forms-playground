from django.shortcuts import render
from .forms import SampleForm, SampleForm2
from django.views.generic.edit import FormView, CreateView, View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import BaseForm

# Create your views here.
def questionaireA(request):
    return render(request, 'questionaire.html')


# thanks view
def thanks_view(request):
    return render(request, 'thanks.html')


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        print("I am reached from form_valid")
        # response = super().form_valid(form)
        # Not valid for some reason...
        print(form.is_valid())

        if form.is_valid():
            if self.request.is_ajax():
                print("DETETING AJAX")
                # what was I supposed to do here??? I don't remember
                # maybe setup the data to save? idk
                data = {
                    'test': 200,
                }
                return JsonResponse(data)
            else:
                return form



# Lets make a Form Class based View
# how to we render the form?
# Benefits of FormView abstracts away from you the boilerplate code from having to per different views, 
# rather then checking if POST == 'GET' or 'POST
# If post call is_valid and if correct redirect user, otherwise show form again 
# IMPORTANT - FormView does NOT work on Models, just deals with Forms
# Below will show the different class methods we can override
class SampleFormView(FormView):
    template_name = 'questionaire/sample_form.html'
    form_class = SampleForm
    # you can override success method
    success_url = 'questionaire/thanks/'


    def get_initial(self):
        initial_data = super(SampleFormView, self).get_initial()
        initial_data['name']: 'This is the begin value'
        return initial_data

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        if '\'' in form.data['name'] or 'union' in form.data['name'].lower():
            print('SQL injection attempt!')
        return super(SampleFormView, self).form_invalid(form)
    
    # def get_success_url(self):
    #     return reverse('thanks')



# What is reverse_lazy?


# Note also that you can only inherit from one generic view - that is, 
# only one parent class may inherit from View and the rest (if any) should be mixins. 
# Trying to inherit from more than one class that inherits from View - for example, 
# trying to use a form at the top of a list and combining ProcessFormView and ListView 
# - won’t work as expected.
class ParentFormClass(View):
    is_completed = None

    def get(self, request):
        return HttpResponse(self.is_completed)


class SFCreateView(AjaxableResponseMixin,CreateView):
    template_name = 'questionaire/sample_form2.html'
    form_class = SampleForm2
    success_url = '/thanks/'
    # Can aslo point to Model
    # model = ModelDummyUser
    # fields = ('first_name', 'last_name)

    # We can override is_completed
    is_completed = True
    initial = {'name': 'jin'}


    def get(self, request, *args, **kwargs):

        # view logic goes here
        form = self.form_class(initial=self.initial)
        print('this is the GET request')
        return render(request, self.template_name, {'form': form})
        # return HttpResponse(self.is_completed)
    
    def post(self, request, *args, **kwargs):
        print('this is the post request from Class View')
        form = self.form_class(request.POST)

        response = self.form_valid(form)

        # return response

        # return response
        # print(response)
        if form.is_valid():
        #     # <process form cleaned data>
        #     # return HttpResponseRedirect('/success/')
            print('form submitted!')
            # response = self.form_valid(form)
            # print(response)
            # form.
            # newForm = BaseForm()
            # newForm.save()
            response = self.form_valid(form)

            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {'form': form})


def process_something(request):
    print('I am processing something!!!')
    # province_id = request.GET.get('province')
    # districts = District.objects.filter(province_no_id=province_id).order_by('district')
    # return render(request, '*********.html', {'districts': districts})
