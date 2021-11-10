from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import WishesForm
from .models import Wishes


def memories(request):
    wishes = Wishes.objects.all().order_by('-timestamp')

    paginator = Paginator(wishes, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    if request.POST:
        form = WishesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('memories')
    else:
        form = WishesForm()

    context = {
        'form': form,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,

    }
    return render(request, 'memories.html', context=context)
