from django.shortcuts import render

# Create your views here.
def index(request):
    """The homepage for ians_py_page"""
    return render(request, 'templates/ians_py_page/index.html')