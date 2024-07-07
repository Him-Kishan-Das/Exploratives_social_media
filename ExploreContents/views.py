from django.shortcuts import render, redirect
from .models import users, post
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect

from PIL import Image

# Create your views here.
def home(request):
    return render(request, 'index.html')



def profile(request):
    return render(request, 'profile.html')


def signup(request):
    msg = None  # Initialize msg to None

    if request.method == 'POST':
        # Retrieve form data
        username1 = request.POST.get('signupUserName')
        name1 = request.POST.get('signupUserName')
        email1 = request.POST.get('signupEmail')
        password1 = request.POST.get('signupPassword')
        rePassword1 = request.POST.get('signupConfirmPassword')


        if password1 == rePassword1:
            # Create a new Member and save it to the database
            user = users(username=username1, name = name1, email=email1, password=make_password(password1))
            user.save()
            msg = True
        else:
            msg = False
        
    context = {'message': msg}
    return render(request, 'signup.html', context)


def login(request):
    msg = None
    # context = {'csrf_token': csrf(request)['csrf_token'],}
    if request.method == 'POST':
        userLogin = request.POST.get('username')
        passLogin = request.POST.get('pass')

        check_user = users.objects.get(username=userLogin)
        # Check if the hashed password matches
        if check_password(passLogin, check_user.password):
            request.session['user'] = userLogin
            msg = True
            return redirect('/home', msg)
            
        else:
            msg = False
            print("Please enter valid username and password")
    context = {
        'message': msg,
    }
    return render(request, 'login.html', context)


def newPost(request):
    msg = None
    if request.method == 'POST':
        caption = request.POST.get('caption')  # Correct parameter name
        photo = request.FILES.get('photo')  # Correct parameter name for file upload

        # Save the image to the media directory
        if photo:
            # Process the image if needed (e.g., resizing, cropping)
            # Save it to the media directory
            new_image = Image.open(photo)
            new_image.save(f'media/post/{photo.name}')  # Adjust the path as needed

            # Create a new post instance
            new_post = post(user_id=1, post_caption=caption, post_image=f'media/post/{photo.name}', post_likes=2)
            new_post.save()
            msg = True

            # Redirect to the home page (adjust the URL name as needed)
            return HttpResponseRedirect('/home/')

    context = {
        'message': msg,
    }

    return render(request, 'submit_post.html', context)