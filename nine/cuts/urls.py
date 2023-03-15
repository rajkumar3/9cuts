from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
	url(r'^$',views.index,name="index"),
    url(r'^login/', login, name="login"),
    url(r'^logout/$', auth_views.logout,{'next_page': '/'}, name='logout'),
    url(r'^signup/',views.register_page, name="signup"),
    url(r'^about/', views.about, name="about"),
    url(r'^cart/', views.cart, name="cart"), 
    url(r'^custom/', views.custom, name="custom"),
    url(r'^guide/', views.guide, name="guide"),
    url(r'^works/', views.works, name="works"),
    url(r'^why/', views.why, name="why"),
    url(r'^profile/', views.get_user_profile, name="profile"),

]
