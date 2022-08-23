from django.urls import path, include
from store.views import *
handler404 = view_404
urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout_use, name='logout'),
    path('addproduct', AddProduct.as_view(), name="addproduct"),
    path('order/<int:id>', order, name='order'),
    path('add_games', AddGames.as_view(), name = 'addgame')

]