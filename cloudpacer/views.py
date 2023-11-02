from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url = "/login/")
def home(request):
    peoples = [
        {'name': 'Umer', 'age' : 26},
        {'name': 'Hamza', 'age' : 24},
        {'name': 'Ali', 'age' : 17},
        {'name': 'Muhammad', 'age' : 16},
        {'name': 'Syed', 'age' : 28}
    ]

    text = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        """

    fruits = ['Apple', 'Mango', 'Orange', 'Grape', 'Pineapple']

    return render(request, "index.html", context = {'page' : 'Home', 'peoples' : peoples, 'text' : text, 'fruits' : fruits})

def about_us(request):
    context = {'page' : 'About Us'}
    return render(request, "about_us.html", context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "contact.html", context)
