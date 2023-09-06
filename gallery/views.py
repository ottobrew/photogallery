from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import PhotoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

class LoginInterfaceView(LoginView):
    template_name = "login.html"

class LogoutInterfaceView(LogoutView):
    template_name = "logout.html"

def gallery(request):
    photos = Photo.objects.all()
    return render(request, "gallery.html", {"photos": photos})
 
@login_required(login_url="login")
def upload_photo(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("gallery")
    else:
        form = PhotoForm()
    return render(request, "upload.html", {"form": form})

@login_required(login_url="login")
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        photo.delete()
        return redirect("gallery")
    return render(request, "confirm_delete.html", {"photo": photo})
