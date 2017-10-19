from django.shortcuts import render

# 메인 홈페이지
def home(request):
    return render(request, 'portfolio/home.html')
