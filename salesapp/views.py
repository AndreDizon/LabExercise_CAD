from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

# --- NEW LOGIC FOR LAB 2 ---

def login_view(request):
    # If the request is POST, the user submitted the form
    if request.method == 'POST':
        username_data = request.POST.get('username')
        password_data = request.POST.get('password')
        
        # Validate credentials using Django's built-in auth
        user = authenticate(request, username=username_data, password=password_data)
        
        if user is not None:
            # Login successful
            login(request, user)
            return redirect('user_list') # Redirect to the User List page
        else:
            # Login failed
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    # If request is GET, just show the login page
    return render(request, 'login.html')

@login_required(login_url='login') # This protects the view!
def user_list_view(request):
    # Fetch all users from the database
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})