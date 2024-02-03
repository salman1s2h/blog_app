from django.shortcuts import render,redirect
from django.contrib.auth import login ,authenticate,logout
from  .forms import SignUpForm ,LoginForm
from django.contrib import messages
from django.urls import reverse



def signup(request):
    if request.user.is_authenticated:
        print('already login------------------------>')
        return redirect('core:home')
    

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Congratulations, you are now a registered user!")
            return redirect('core:home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def log_in(request):
    print("print in login page---------------->")
    if request.user.is_authenticated:
        print('already login------------65------------>')
        return redirect('core:home')
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        print("login form ------------------------>",form)
        if form.is_valid():
            print("is valid form ------------------------>")
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            # We check if the data is correct
            user = authenticate(email=email, password=password)
            if user:  # If the returned object is not None
                login(request, user)  # we connect the user
                return redirect('core:home')
            else:  # otherwise an error will be displayed
                print("user---------is---not-valid------->")
                messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect(reverse('users:login'))

