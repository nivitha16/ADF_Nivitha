from django.urls import path
from .views import addinfo,user

urlpatterns = [
    # path('home/',home,name='home'),
    # path('news/',newsp,name='news'),
    # path('contact/',contact,name='cnt'),
    # path('newspage/<int:year>',newspage,name='newspage'),
    path('addinfo/',addinfo,name='addinfo'),
    path('user/',user,name='user'),
]
