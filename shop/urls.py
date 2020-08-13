from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUS"),
    path("contact/",views.contact,name="ContactUS"),
    path("search/",views.search,name="Search"),
    path("tracker/",views.tracker,name="Tracker"),
    path("products/<int:myid>",views.productView,name="ProductView"),
    path("checkout",views.checkout,name="Checkout"),

]
