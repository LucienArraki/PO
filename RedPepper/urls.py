from django.conf.urls import url
from . import views

app_name = 'list'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
        url(r'^zamowienie$', views.order, name='order' ),
]