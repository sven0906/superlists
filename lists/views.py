from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .forms import ItemForm
from .models import Item, List


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, id):
    list_ = List.objects.get(id=id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            # Item.objects.create(text=request.POST['text'], list=list_)
            form.save(for_list=list_)
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, 'form': form})


# def new_list(request):
#     list_ = List.objects.create()
#     item = Item.objects.create(text=request.POST['text'], list=list_)
#     try:
#         item.full_clean()
#         item.save()
#         return redirect(list_)
#     except ValidationError:
#         list_.delete()
#         error = "You can't have an empty list item"
#         return render(request, 'home.html', {"error": error})
#     # return redirect('/lists/%d/' % (list_.id,))
#     # return redirect('view_list', list_.id)
#     return redirect(list_)


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        # Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {'form': form})
