from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from userprofile.forms import EditProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, password_validation as pv

from signupLogin.models import Profile
from django.core.exceptions import ValidationError


from signupLogin.models import Profile
from django.contrib.auth.models import User
from django.core.files.images import ImageFile

# Create your views here.
# @login_required

@login_required(login_url='/login')
def home(request):
    return render(request, 'userprofile/home.html')

@login_required(login_url='/login')
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'userprofile/profile.html', args)

# @login_required(login_url='/login')
# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             return redirect('/userprofile/')
#
#     else:
#         form = EditProfileForm(instance=request.user)
#         args = {'form': form}
#         return render(request, 'userprofile/edit_profile.html', args)

@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/userprofile/')
        else:
            args = {'error': 'error'}
            messages.warning(request, 'Please check your password again.')
            return redirect('/userprofile/change-password')
            #return render(request, 'userprofile/change_password.html', args)

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'userprofile/change_password.html', args)

@login_required(login_url='/login')
def edit_profile(request):
    # return render(request, 'userprofile/edit_profile2.html')
    user = User.objects.get(username=request.user.username)
    userReq = request.user
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        telephone = request.POST['telephone']
        email = request.POST['email']
        bankaccount = request.POST['bankaccount']
        birthday = request.POST['birthday']
        try:
            imageFound = True
            profile_image = ImageFile(request.FILES['profile_image'])
        except:
            imageFound = False

        p = Profile()
        p.user = user
        if firstname != "":
            user.first_name = firstname

        if lastname != "":
            user.last_name = lastname

        if address != "":
            p.address = address
        else:
            p.address = userReq.profile.address

        if telephone != "":
            p.telephone = telephone
        else:
            p.telephone = userReq.profile.telephone

        if email != "":
            user.email = email

        if bankaccount != "":
            p.bankaccount = bankaccount
        else:
            p.bankaccount = userReq.profile.telephone

        if birthday != "":
            p.birthday = birthday
        else:
            p.birthday = userReq.profile.birthday

        if imageFound:
            p.image = profile_image
        else:
            p.image = userReq.profile.image

        user.save()
        p.save()
        return redirect('/userprofile/')

    return render(request, 'userprofile/edit_profile.html', {'firstname':user.first_name, 'lastname':user.last_name, 'address':user.profile.address, 'telephone':user.profile.telephone, 'email':user.email, 'bankaccount':user.profile.bankaccount, 'birthday':user.profile.birthday})
