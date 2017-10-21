from django.shortcuts import render
from django.views.generic import DetailView
from portfolio.models import Portfolio

# Create your views here.


# TODO: class기반의 view로 바꿔주면 백단에서 더욱편함.
# 현재는 프론트단을 위해 임시로 def를 만든 것.
def portfolioIndexView(request):
    return render(request, 'portfolio/index.html')
def portfolioBaseView(request):
    return render(request, 'portfolio/base.html')


def portfolio_main_view(request, pk):
    portfolio = Portfolio.objects.get(id=pk)
    return render(request, 'portfolio/index.html', {'user': request.user, 'portfolio': portfolio})

def activity(request):
    return render(request, 'portfolio/activity.html')