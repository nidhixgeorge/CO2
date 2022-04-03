from django.shortcuts import render

from .forms import CarbonForm1, CarbonForm2

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        form1 = CarbonForm1(request.POST)
        form2 = CarbonForm2(request.POST)
        msg = "We are working on calculating your carbon footprints"
        c = {
                    'form1' : form1,
                    'form2' : form2, 
                     'msg' : msg,                 
                    }
        return render(request, 'co2/homepage.html', c)   
    else:
        form1 = CarbonForm1()
        form2 = CarbonForm2()
        
        c = {
                        'form1' : form1,
                        'form2' : form2, 
                                        
                        }
        return render(request, 'co2/homepage.html', c)



def show_terms(request):    
    c = {}
    return render(request, 'co2/terms.html', c)    

def show_privacy(request):    
    c = {}
    return render(request, 'co2/privacy.html', c)

def contactus(request):    
    c = {}
    return render(request, 'co2/contactus.html', c)  