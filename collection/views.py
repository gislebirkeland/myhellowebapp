from django.shortcuts import render

# Create your views here.
def index(request):
	# defining the variable
	thing = "gisle birkeland"
	# this is your new view
	return render(request, 'index.html', {
		'thing': thing,
		})