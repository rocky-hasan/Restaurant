from django.contrib import admin
from app.models import AboutModel, AllFood, SectionModel, EventsModel, ChefsModel, GalleryModel, Cart, OrderPlaced, Customer


# Register your models here.
@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    fields = ['heading', 'line1', 'line2', 'line3', 'desc', 'image']


@admin.register(AllFood)
class AllFoodModelAdmin(admin.ModelAdmin):
    fields = ['food_name', 'desc', 'price', 'category', 'food_image']


@admin.register(SectionModel)
class AllFoodModelAdmin(admin.ModelAdmin):
    fields = ['title', 'desc', 'section_image']


@admin.register(EventsModel)
class EventsModelAdmin(admin.ModelAdmin):
    fields = ['title', 'price', 'desc', 'events_image']


@admin.register(ChefsModel)
class ChefsModelAdmin(admin.ModelAdmin):
    fields = ['name', 'title', 'chefs_image']


@admin.register(GalleryModel)
class GalleryModelAdmin(admin.ModelAdmin):
    fields = ['gallery_image']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    fields = ['user', 'food', 'quantity']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email', 'city', 'house_no', 'zipcode', 'state']


@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'food', 'quantity', 'order_date', 'status']