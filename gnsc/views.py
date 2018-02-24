from django.shortcuts import render, get_object_or_404

def gnsc(request):
    return render(request, 'gnsc.html', {})
	
	
def cine(request):
    return render(request, 'cine.html', {})
	

def design(request):
    return render(request, 'design.html', {})
	
	
	
	
def outreach(request):
    return render(request, 'outreach.html', {})
	

def photography(request):
    return render(request, 'photography.html', {})
	
	
def media(request):
    return render(request, 'media.html', {})
	

def animation(request):
    return render(request, 'animation.html', {})


	
