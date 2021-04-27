from django.shortcuts import render
from .models import Contact
# Create your views here.
def index(request):
	return render(request,'index.html')

def contact(request):
	
	Contact.objects.create(
			name=request.POST['name'],
			email=request.POST['email'],
			subject=request.POST['subject'],
			message=request.POST['message']
		)
	msg="Contact Saved Successfully. Will Reach You Very Soon."
	return render(request,'index.html',{'msg':msg})