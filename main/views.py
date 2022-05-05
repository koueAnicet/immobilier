from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/index.html')
def index(request):
    return render(request, 'main/index.html')
    
def about(request) :
    return render(request, 'main/about.html')
def agent(request) :
    return render(request, 'main/agents-grid.html')
def agentSingle(request) :
    return render(request, 'main/agents-single.html')
    
def blog(request) :
    return render(request, 'main/blog-grid.html')
def blogSingle(request) :
    return render(request, 'main/blog-single.html')
def property1(request) :
    return render(request, 'main/property-grid.html')

def propertySingle(request) :
    return render(request, 'main/property-single.html')
def contact(request) :
    return render(request, 'main/contact.html')