from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
urlpatterns=[
    path('aboutus/',views.aboutus,name='aboutus'),
    path('appoinment/',views.appoinment,name='appoinment'),
    path('cats/',views.cats,name='cats'),
    path('contactus/',views.contactus,name='contactus'),
    path('doctor/',views.doctor,name='doctor'),
    path('food/',views.food,name='food'),
    path('homepg/',views.homepg,name='homepg'),
    path('login/',views.login,name='login'),
    # path('payment/',views.payment,name='payment'),
    path('register/',views.register,name='register'),
    path('toys/',views.toys,name='toys'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout,name='logout'),
    path('aboutusl/',views.aboutusl,name='aboutusl'),
    path('catsl/',views.catsl,name='catsl'),
    path('contactusl/',views.contactusl,name='contactusl'),
    path('doctorl/',views.doctorl,name='doctorl'),
    path('foodl/',views.foodl,name='foodl'),
    path('homepgl/',views.homepgl,name='homepgl'),
    path('toysl/',views.toysl,name='toysl'),
    path('tablea/',views.tablea,name='tablea'),
    path('tablep/',views.tablep,name='tablep'),
    path('add-to-cart/<str:model_name>/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('book_appo/',views.book_appo,name='book_appo'),
    # path('direct_purchase/<int:item_id>/<str:item_type>/', views.direct_purchase, name='direct_purchase'),
    # path('cart_purchase/', views.cart_purchase, name='cart_purchase'),
    path('cancel_appointment/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('payment/<str:item_type>/<int:item_id>/', views.payment, name='payment'),

]


