# from pyexpat.errors import messages
# from django.shortcuts import render, redirect
# from .models import users, post
# from django.contrib.auth.hashers import make_password, check_password
# from django.http import HttpResponseRedirect, HttpResponse
# from django.template import loader
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required

# from PIL import Image

# def signup(request):
#     msg = None  # Initialize msg to None

#     if request.method == 'POST':
#         # Retrieve form data
#         username1 = request.POST.get('signupUserName')
#         name1 = request.POST.get('signupUserName')
#         email1 = request.POST.get('signupEmail')
#         password1 = request.POST.get('signupPassword')
#         rePassword1 = request.POST.get('signupConfirmPassword')


#         if password1 == rePassword1:
#             # Create a new Member and save it to the database
#             user = users(username=username1, name = name1, email=email1, password=make_password(password1))
#             user.save()
#             msg = True
#         else:
#             msg = False
        
#     context = {'message': msg}
#     return render(request, 'signup.html', context)

# # def login_page(request):
# #     msg = None
# #     if request.method == 'POST':
# #         userLogin = request.POST.get('username')
# #         passLogin = request.POST.get('pass')
# #         print(f"Username: {userLogin}, Password: {passLogin}")
# #         try:
# #             user = users.objects.get(username=userLogin)
# #             print(f"User found: {user.username}")
# #             if check_password(passLogin, user.password):
# #                 user = authenticate(request, username=userLogin, password=passLogin)
# #                 if user is not None:
# #                     login(request, user)
# #                     print("User authenticated and logged in")
# #                     return redirect('/home')
# #                 else:
# #                     msg = "Invalid username or password"
# #                     print("Authentication failed")
# #             else:
# #                 msg = "Invalid username or password"
# #                 print("Password check failed")
# #         except users.DoesNotExist:
# #             msg = "User does not exist"
# #             print("User does not exist")
    
# #     context = {'message': msg}
# #     return render(request, 'login.html', context)


# @login_required
# def home(request):
#     # Retrieve all posts from the database
#     feedx = post.objects.all()

#     # Pass the posts to the template context
#     context = {'postx': feedx}

#     # Load the template named 'feeds.html'
#     template = loader.get_template('index.html')

#     # Render the template with the context
#     return HttpResponse(template.render(context, request))



# def profile(request):
#     return render(request, 'profile.html')




# def login_page(request):
#     msg = None
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('pass')

#         # Check if a user with the provided username exists
#         try:
#             user = users.objects.get(username=username)
#         except users.DoesNotExist:
#             # Display an error message if the username does not exist
#             messages.error(request, 'Invalid Username')
#             return redirect('/login/')
         
#         # Check if the hashed password matches
#         if check_password(password, user.password):
#             # Log in the user and redirect to the home page upon successful login
#             # login(request, user)
#             print("User authenticated and logged in")
#             # return redirect('')     
#             return redirect('/home/')

#         else:
#             # Display an error message if authentication fails (invalid password)
#             messages.error(request, "Invalid Password")
#             return redirect('/login/')
     
#     # Render the login page template (GET request)
#     return render(request, 'login.html')

# def newPost(request):
#     msg = None
#     if request.method == 'POST':
#         caption = request.POST.get('caption') 
#         photo = request.FILES.get('photo') 

#         if photo:
#             new_image = Image.open(photo)
#             new_image.save(f'static/post/{photo.name}')  # Adjust the path as needed

#             new_post = post(user_id=1, post_caption=caption, post_image=f'static/post/{photo.name}', post_likes=2)
#             new_post.save()
#             msg = True

#             return HttpResponseRedirect('/home/')

#     context = {
#         'message': msg,
#     }

#     return render(request, 'submit_post.html', context)

# # def feedDisplay(request):
# #     # Retrieve all posts from the database
# #     feedx = post.objects.all()

# #     # Pass the posts to the template
# #     context = {'postx': feedx}
# #     template = loader.get_template('feeds.html')  # Adjust the template name as needed
# #     return HttpResponse(template.render(context, request))


# def usernames(request):
#     usr = users.objects.all()
#     context = {'usrx': usr}
#     return render(request, 'index.html', context)


from django.shortcuts import render, redirect
from .models import CustomUser as users, Post
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from PIL import Image

def signup(request):
    msg = None
    if request.method == 'POST':
        username1 = request.POST.get('signupUserName')
        name1 = request.POST.get('signupName')  # Ensure this matches form input
        email1 = request.POST.get('signupEmail')
        password1 = request.POST.get('signupPassword')
        rePassword1 = request.POST.get('signupConfirmPassword')

        if password1 == rePassword1:
            user = users(username=username1, name=name1, email=email1, password=make_password(password1))
            user.save()
            msg = True
        else:
            msg = False

    context = {'message': msg}
    return render(request, 'signup.html', context)


def login_page(request):
    msg = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        try:
            user = users.objects.get(username=username)
            print(user.username)
            print(user.password)
        except users.DoesNotExist:
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
         
        if check_password(password, user.password):
            print('helloworld')
            user = authenticate(request, username=username, password= password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('/home/')
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect('/login/')
        else:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
     
    return render(request, 'login.html')

@login_required
def home(request):
    feedx = Post.objects.all()
    context = {'postx': feedx}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def profile(request):
    return render(request, 'profile.html')

def newPost(request):
    msg = None
    if request.method == 'POST':
        caption = request.POST.get('caption') 
        photo = request.FILES.get('photo') 

        if photo:
            new_image = Image.open(photo)
            new_image.save(f'static/post/{photo.name}') 

            new_post = Post(user_id=1, post_caption=caption, post_image=f'static/post/{photo.name}', post_likes=2)
            new_post.save()
            msg = True

            return HttpResponseRedirect('/home/')

    context = {'message': msg}
    return render(request, 'submit_post.html', context)

def usernames(request):
    usr = users.objects.all()
    context = {'usrx': usr}
    return render(request, 'index.html', context)
