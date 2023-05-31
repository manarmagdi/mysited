from django.urls import path
from . import views





urlpatterns = [
    path("home/", views.Home, name="home"),
    path("shopnow", views.Shopnow, name="shopnow"),
    path("login", views.Login, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup, name="signup"),
    path("cart", views.cart, name="cart"),
    path("profile", views.Pro, name="profile"),
    path("hijab", views.Hijab, name="hijab"),
    path("hali", views.HALI, name="hali"),
    # path("<int:product_id>", views.Add_to_cart, name="add"),

]
