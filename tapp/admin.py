from django.contrib import admin

from tapp.models import Profile, Cat, Kitten, Doctor, Food, Foodk, Toy, Aboutus, Contactus, Payment, Appointment, \
    CartItem

# Register your models here.
admin.site.register(Profile)
admin.site.register(Cat)
admin.site.register(Kitten)
admin.site.register(Doctor)
admin.site.register(Food)
admin.site.register(Foodk)
admin.site.register(Toy)
admin.site.register(Aboutus)
admin.site.register(Contactus)
admin.site.register(Payment)
admin.site.register(Appointment)
admin.site.register(CartItem)