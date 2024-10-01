from django.urls import path 
from .import views


urlpatterns = [
  path("", views.index, name="index"),
  path("final", views.final, name="final"),
  path("signup/",views.signup,name="signup"),
  path("login/",views.login, name="login"),
  path("logout/",views.logout, name="logout"),
  path("milk",views.milk, name="milk"),
  path("curd",views.curd, name="curd"),
  path("butter",views.butter, name="butter"),
  path("cheese",views.cheese, name="cheese"),
  path("buttermilk",views.buttermilk, name="buttermilk"),
  path("ghee",views.ghee, name="ghee"),
  path("condensed",views.condensed, name="condensed"),
  path("yogurt",views.yogurt, name="yogurt"),
  path('pay/', views.initiate_payment, name='initiate_payment'),
  path('payment/callback/', views.payment_callback, name='payment_callback'),
]
