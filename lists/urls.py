from django.urls import path
from .views import view_list, new_list

urlpatterns = [
    path('<int:id>/', view_list, name='view_list'),
    path('new', new_list, name='new_list'),
    # path('admin/', admin.site.urls),
]