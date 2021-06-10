from django.shortcuts import render

# Create your views here.
def index(request):
    """The homepage for ians_py_page"""
    return render(request, 'ians_py_page/index.html')