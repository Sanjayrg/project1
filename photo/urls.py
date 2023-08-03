from django.urls import path
from photo import views

app_name='photo'
urlpatterns = [
    path('index', views.index, name = "index"),
    path('contact', views.contact, name = "contact"),
    path('team', views.team, name = "team"),
    path('portfolio', views.portfolio, name = "portfolio"),
    path('about', views.about, name = "about"),
    
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login_reg'),
    path('logout', views.logoutuser, name = 'logout'),

    path('product', views.product, name='product'),
    path('products', views.products, name='products'),
    path('order/<int:id>', views.order, name='order'),
    path('kart', views.kart  , name='kart '),
]