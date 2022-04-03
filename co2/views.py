from django.shortcuts import render

from .forms import CarbonForm1, CarbonForm2

# Create your views here.
def homepage(request):

    form1 = CarbonForm1()
    form2 = CarbonForm2()
    c = {
                    'form1' : form1,
                    'form2' : form2, 
                                      
                    }
    return render(request, 'co2/homepage.html', c)