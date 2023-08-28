from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app.forms import UserRegistrationForm, ContactForm, MyPasswordChangeForm, CustomerProfileForm, BookingForm
from .models import AboutModel, AllFood, EventsModel, ChefsModel, GalleryModel, Customer, Cart, OrderPlaced


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    ab = AboutModel.objects.all()
    return render(request, 'about.html', {'ab': ab})


class Menu(View):
    def get(self, request):
        food = AllFood.objects.all()
        return render(request, 'menu.html', {'food': food})


class FoodDetailView(View):
    def get(self, request, pk):
        food = AllFood.objects.get(pk=pk)  # Retrieve the specific AllFood object based on pk
        item_already_in_cart = False

        # Check if the user is authenticated and if the product is in the user's cart
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(food=food) & Q(user=request.user)).exists()
        return render(request, 'food_detail.html', {'food': food, 'item_already_in_cart': item_already_in_cart})


def salad(request, data=None):
    if data is None:
        food = AllFood.objects.filter(category='SL')
    return render(request, 'salad.html', {'food': food})


def speciality(request, data=None):
    if data is None:
        food = AllFood.objects.filter(category='SP')
    return render(request, 'speciality.html', {'food': food})


def starter(request, data=None):
    if data is None:
        food = AllFood.objects.filter(category='ST')
    return render(request, 'starter.html', {'food': food})


@method_decorator(login_required, name='dispatch')
class Contact(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Thanks For Reaching Us! We will get back to you soon....")
        return redirect('contact')


class Special(View):
    def get(self, request):
        return render(request, 'special.html')


class EventsView(View):
    def get(self, request):
        events = EventsModel.objects.all()
        return render(request, 'event.html', {'events': events})


class ChefsView(View):
    def get(self, request):
        chefs = ChefsModel.objects.all()
        return render(request, 'chefs.html', {'chefs': chefs})


class GalleryView(View):
    def get(self, request):
        gallery = GalleryModel.objects.all()
        return render(request, 'gallery.html', {'gallery_img': gallery})


@method_decorator(login_required, name='dispatch')
class Book_a_table(View):
    def get(self, request):
        form = BookingForm()
        return render(request, 'book_a_table.html', {'form': form})

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Booking completed...')
            form.save()
        return render(request, 'book_a_table.html', {'form': form})


@login_required
def profile(request):
    if request.user.is_authenticated:
        customers = Customer.objects.filter(
            user=request.user)  # Retrieve all Customer objects that belong to the logged-in user
        if customers.exists():  # Check if any Customer objects exist for the user
            customer = customers.first()
        else:
            customer = None
        return render(request, 'profile.html', {'customer': customer})
    else:
        return HttpResponseRedirect('/login/')


@login_required
def update_customer_profile(request):
    user = request.user  # Assuming the user is authenticated
    try:
        customer = Customer.objects.filter(user=user).first()  # Get the first matching customer
    except Customer.DoesNotExist:
        # Handle the case where the customer doesn't exist for the user
        messages.warning(request, 'Customer profile does not exist.')
        return redirect('home')  # Redirect to a relevant URL

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile updated successfully!!!')
            return redirect('profile')  # Redirect to a relevant URL after successful update
    else:
        form = CustomerProfileForm(instance=customer)

    context = {
        'form': form,
    }
    return render(request, 'update_profile.html', context)


@method_decorator(login_required, name='dispatch')
class ProfileForm(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'biodata.html', {'form': form})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user  # Associate the user
            customer.save()
            messages.success(request, 'Information entry completed!!!')
        return render(request, 'biodata.html', {'form': form})


class SignupForm(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registration completed')
            form.save()
        return render(request, 'signup.html', {'form': form})


class Forget_pass(CreateView):
    def get(self, request):
        return render(request, 'forget_pass.html')


class ResetPassView(View):
    def get(self, request):
        form = MyPasswordChangeForm(user=request.user)
        return render(request, 'reset_pass.html', {'form': form})

    def post(self, request):
        form = MyPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully!')
            # You might want to redirect the user to a different page after a successful password change
            return redirect('pass_change')
        else:

            return render(request, 'reset_pass.html', {'form': form})


@login_required
def add_to_cart(request):
    user = request.user
    food_id = request.GET.get('food_id')
    Cart(user=user, food=food_id).save()
    return redirect('/cart')


@login_required
def show_to_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        print(cart)
        amount = 0.0
        shipping_amount = 70.0
        totalamount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.food.price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'add_to_cart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount})
        else:
            return render(request, 'empty_cart.html')


def plus_cart(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('showcart')  # Redirect back to the cart page


def remove_cart(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    cart_item.delete()
    return redirect('showcart')


def minus_cart(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('showcart')  # Redirect back to the cart page


@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_item = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.food.price)
            amount += tempamount
        totalamount = amount + shipping_amount
    return render(request, 'checkout.html', {'add': add, 'cart_item': cart_item, 'totalamount': totalamount})


@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'address.html', {'add': add, 'active': 'btn-dark'})


@login_required
def payment_done(request):
    if request.method == 'GET':
        user = request.user
        custid = request.GET.get('custid')
        customer = Customer.objects.get(id=custid)
        cart = Cart.objects.filter(user=user)
        for c in cart:
            OrderPlaced(user=user, customer=customer, food=c.food, quantity=c.quantity).save()
            c.delete()
        return redirect('order')


@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'order.html', {'order_placed': op})

