from django.shortcuts import render, get_object_or_404, redirect
from .models import Menu, Review
from .forms import ReviewForm

# Create your views here.

def detalle_menu(request, id_menu):
    menu = get_object_or_404(Menu, id=id_menu)
    reviews = menu.reviews.all()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.menu = menu
            review.user - request.user
            review.save()
            return redirect('detalle_menu', id_menu=id.menu)
    else:
        form = ReviewForm()

    return render(request, 'detalle_menu.html', {'menu': menu, 'reviews': reviews, 'form':form})