from django.shortcuts import render, redirect
from .forms import WishesForm
from .models import Wishes

def memories(request):
    wishes = Wishes.objects.all().order_by('-timestamp')
    if request.POST:
        form = WishesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('memories')
    else:
        form = WishesForm()
    
    context = {
        'form': form,
        'wishes': wishes
    }
    return render(request, 'memories.html', context=context)
