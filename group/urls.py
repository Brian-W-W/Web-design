from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main, name='main'),
    path('group/master', views.master, name="master"),
    path('', views.navigation, name="nav" ),
    path('group_one/', views.index, name='index'),
    path('group_one/details/<int:id>', views.details, name='details'),
    ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)