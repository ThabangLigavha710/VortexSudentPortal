from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'richfieldVSP/base.html')

def sign_up(request):
	return render(request, 'richfieldVSP/sign_up.html')

def log_in(request):
	return render(request, 'richfieldVSP/log_in.html')