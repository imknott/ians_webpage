from django.shortcuts import render

# Create your views here.
def index(request):
    """The homepage for ians_py_page"""
    return render(request, '/Users/ianknott/Desktop/ians_webpage/ians_py_page/templates/index.html')