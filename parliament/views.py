from django.shortcuts import render, get_object_or_404

def parliament(request):
    return render(request, 'parliament_home.html', {})
	
	
def committee(request):
    return render(request, 'parliament_committee.html', {})
	

def elections(request):
    return render(request, 'parliament_elections.html', {})


	
def minutes(request):
	return render(request, 'parliament_minutes.html', {})

	
def feedback(request):
	return render(request, 'parliament_feedback.html', {})