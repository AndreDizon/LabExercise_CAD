from django.shortcuts import render

# View for the Homepage
def homepage(request):
    return render(request, 'home.html')

# View for the Login Page
def login_view(request):
    return render(request, 'login.html')

# View for the About Us Page
def about_view(request):
    return render(request, 'about.html')

# View for the Contact Us Page
def contact_view(request):
    return render(request, 'contact.html')