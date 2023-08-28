"""Restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView
from app.forms import MyPasswordChangeForm
from app.forms import UserLogin, MyPasswordResetForm
from app import views
from app.views import ResetPassView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('profile/', views.profile, name='profile'),
    path('update_customer_profile/', views.update_customer_profile, name='update_customer_profile'),
    path('biodata/', views.ProfileForm.as_view(), name='biodata'),
    path('about/', views.about, name='about'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('menu/<int:pk>', views.FoodDetailView.as_view(), name='menu'),
    path('salad/', views.salad, name='salad'),
    path('starter/', views.starter, name='starter'),
    path('speciality/', views.speciality, name='speciality'),
    path('special/', views.Special.as_view(), name='special'),
    path('event/', views.EventsView.as_view(), name='event'),
    path('chef/', views.ChefsView.as_view(), name='chef'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('book_a_table/', views.Book_a_table.as_view(), name='book_a_table'),

#------------------Cart-----------------------Cart----------------Cart----------------
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_to_cart, name='showcart'),
    path('checkout/', views.checkout, name='checkout'),
    path('address/', views.address, name='address'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('order/', views.orders, name='order'),

    path('increase-cart-quantity/<int:cart_id>/', views.plus_cart, name='increase_cart_quantity'),
    path('decrease-cart-quantity/<int:cart_id>/', views.minus_cart, name='decrease_cart_quantity'),
    path('remove-from-cart/<int:cart_id>/', views.remove_cart, name='remove_from_cart'),


    #......authenticationFrom............
    path('signup/', views.SignupForm.as_view(), name='signup'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html', authentication_form=UserLogin), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

  #  path('pass_change/', views.ResetPassView.as_view(template_name='reset_pass.html', form_class=MyPasswordChangeForm), name='pass_change'),
    path('pass_change/', views.ResetPassView.as_view(), name='pass_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    #path('password_reset/', MyPasswordResetForm.as_view(), name='password_reset'),
    #path('password_reset_confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    #path('password_reset_done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)















