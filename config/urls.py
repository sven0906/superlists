from django.contrib import admin
from django.urls import path, include
from lists.views import home_page, view_list, new_list

urlpatterns = [
    path('', home_page, name='home'),
    # path('lists/<int:id>/', view_list, name='view_list'),
    # path('lists/new', new_list, name='new_list'),
    path('lists/', include('lists.urls'))
    # path('admin/', admin.site.urls),
]
