from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .forms import ItemForm
from .models import Item, List


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, id):
    list_ = List.objects.get(id=id)
    error = None
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            # return redirect('/lists/%d/' % (list_.id,))
            return redirect(list_)
        except ValidationError:
            error = "빈 아이템을 등록할 수 없습니다."
    return render(request, 'list.html', {'list': list_, 'error': error})


def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "빈 아이템을 등록할 수 없습니다."
        return render(request, 'home.html', {"error": error})
    # return redirect('/lists/%d/' % (list_.id,))
    # return redirect('view_list', list_.id)
    return redirect(list_)



