from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def dashboard(request):
    return render(request, "members/dashboard.html")


@login_required
def profile(request):
    return render(request, "members/profile.html", {"profile": request.user.profile})


@login_required
def edit_profile(request):
    if request.method == "POST":
        profile = request.user.profile
        profile.phone = request.POST.get("phone", "")
        profile.address = request.POST.get("address", "")
        profile.save()

        request.user.first_name = request.POST.get("first_name", "")
        request.user.last_name = request.POST.get("last_name", "")
        request.user.email = request.POST.get("email", "")
        request.user.save()

        messages.success(request, "Perfil actualizado correctamente")
        return redirect("members:profile")

    return render(request, "members/edit_profile.html")
