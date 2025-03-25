from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages


def register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("manager:index")
        else:
            form = UserRegisterForm()
    else:
        return redirect('profile')

    return render(
        request,
        "registration/register.html",
        context={
            "form": form
        }
    )


@login_required
def profile(request):
    # Pass objects to the context (for statictics)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully!')
            return redirect("profile")
        else:
            messages.error(request, 'Couldn\'t save the data')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(
        request,
        "registration/profile.html",
        context={'form': form}
    )


def custom_403_handler(request, exception):
    return render(
        request,
        '403.html',
        status=403
    )
