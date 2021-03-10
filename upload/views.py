from django.shortcuts import render
from .models import ImageUpload
from upload.forms import ImageForm
def showIndex(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    image = ImageUpload.objects.all()
    return render(request,"home.html",{'image':image,'form':form})
