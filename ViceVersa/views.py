from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	words_count = len(user_text.split())
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html',{'usertext':user_text,
		'reversed_text':reversed_text,'words_count':words_count})