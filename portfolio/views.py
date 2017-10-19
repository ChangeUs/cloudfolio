from django.shortcuts import render
from django.views.generic import DetailView

# Create your views here.


# TODO: class기반의 view로 바꿔주면 백단에서 더욱편함.
# 현재는 프론트단을 위해 임시로 def를 만든 것.
def portfolioIndexView(request):
    return render(request, 'portfolio/index.html')
def portfolioBaseView(request):
    return render(request, 'portfolio/base.html')