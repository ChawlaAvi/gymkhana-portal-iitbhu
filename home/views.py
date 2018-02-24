from django.shortcuts import render, get_object_or_404

def contact(request):
    return render(request, 'contact.html', {})

	
def gallery(request):
    return render(request, 'gallery.html', {})
	

def home(request):
    return render(request, 'home.html', {})
	
	
def credits(request):
    return render(request, 'credits.html', {})


	
