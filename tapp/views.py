from decimal import Decimal

from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


from proj import settings
from tapp.models import Profile, Cat, Kitten, Doctor, Food, Foodk, Toy, Contactus, Aboutus, Payment, Appointment, \
    CartItem


# Create your views here.
def aboutus(request):
    about = Aboutus.objects.all()
    return render(request, 'aboutus.html', {'about': about})


def appoinment(request):
    if request.method == 'POST':
        owner_name = request.POST['owner_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        preferred_date = request.POST['preferred_date']
        preferred_time = request.POST['preferred_time']
        doctor = request.POST['doctor']

        # Save to the database
        Appointment.objects.create(
            user=request.user,
            owner_name=owner_name,
            email=email,
            phone_number=phone_number,
            preferred_date=preferred_date,
            preferred_time=preferred_time,
            doctor=doctor
        )
        return redirect('book_appo')  # Reload the page to show the updated table
    return render(request, 'appoinment.html')


def cancel_appointment(request, appointment_id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
        appointment.delete()
        return redirect('tablea')  # Redirect to the appointments table after cancellation


def cats(request):
    cats = Cat.objects.all()
    kittens = Kitten.objects.all()
    return render(request, 'cats.html', {'cats': cats, 'kittens': kittens})


def contactus(request):
    contact = Contactus.objects.all()
    return render(request, 'contactus.html', {'contact': contact})


def doctor(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor.html', {'doctors': doctors})


def food(request):
    foods = Food.objects.all()
    foodk = Foodk.objects.all()
    return render(request, 'food.html', {'foods': foods, 'foodk': foodk})


def homepg(request):
    return render(request, 'homepg.html')


# def payment(request):
#     # If it's a POST request, process the form submission
#     if request.method == 'POST':
#         # Retrieve data from the form submission (POST)
#         price = request.POST.get('amount', 0)  # Use amount from form, as price was passed to the form
#         item_id = request.POST.get('item_id')  # Retrieve item_id from the form submission
#
#         name_on_card = request.POST.get('name_on_card')
#         card_number = request.POST.get('card_number')
#         expiry_date = request.POST.get('expiry_date')
#         cvv = request.POST.get('cvv')
#
#         # Ensure amount is a decimal
#         try:
#             amount = Decimal(price)  # Convert price to decimal for storage
#         except:
#             amount = Decimal(0)  # Default to 0 if there's an error
#
#         # Check for missing fields
#         if not name_on_card or not card_number or not expiry_date or not cvv:
#             return render(request, 'payment.html', {'error': 'Please fill in all required fields.', 'price': price, 'item_id': item_id})
#
#         # Save payment to the database, linked to the logged-in user
#         Payment.objects.create(
#             user=request.user,  # Associate with the logged-in user
#             name_on_card=name_on_card,
#             card_number=card_number,
#             expiry_date=expiry_date,
#             cvv=cvv,
#             amount=amount  # Store the amount as a decimal
#         )
#
#         # Mark the cart item as purchased if an item ID is provided
#         if item_id:
#             cart_item = CartItem.objects.filter(id=item_id, user=request.user).first()
#             if cart_item:
#                 cart_item.purchased = True  # Set purchased to True
#                 cart_item.save()
#
#         # Redirect to a success page
#         return redirect('payment_success')
#
#     # If the request method is GET, render the payment page with the price
#     price = request.GET.get('price', 0)  # Use GET to pass price
#     item_id = request.GET.get('item_id', '')  # Item ID passed via GET
#     return render(request, 'payment.html', {'price': price, 'item_id': item_id})

# def payment(request):
#     if request.method == 'POST':
#         # Retrieve data from the form submission
#         name_on_card = request.POST.get('name_on_card')
#         card_number = request.POST.get('card_number')
#         expiry_date = request.POST.get('expiry_date')
#         cvv = request.POST.get('cvv')
#
#         # Calculate the total price from the user's cart items
#         cart_items = CartItem.objects.filter(user=request.user, purchased=False)
#         total_price = sum(item.content_object.price * item.quantity for item in cart_items)
#
#         # Ensure the amount is a decimal
#         try:
#             amount = Decimal(total_price)
#         except:
#             amount = Decimal(0)
#
#         # Check for missing fields
#         if not name_on_card or not card_number or not expiry_date or not cvv:
#             return render(request, 'payment.html', {'error': 'Please fill in all required fields.', 'total_price': total_price})
#
#         # Save the payment to the database
#         Payment.objects.create(
#             user=request.user,
#             name_on_card=name_on_card,
#             card_number=card_number,
#             expiry_date=expiry_date,
#             cvv=cvv,
#             amount=amount
#         )
#
#         # Mark the cart items as purchased
#         if cart_items:
#             for cart_item in cart_items:
#                 cart_item.purchased = True
#                 cart_item.save()
#
#         # Redirect to a success page
#         return redirect('payment_success')
#
#     # Handle GET request and calculate the total price dynamically
#     cart_items = CartItem.objects.filter(user=request.user, purchased=False)
#     total_price = sum(item.content_object.price * item.quantity for item in cart_items)
#
#     return render(request, 'payment.html', {'total_price': total_price})


# def payment(request):
#     total_price = Decimal(0)  # Initialize the total price
#     item_id = request.GET.get('item_id')  # Get item ID for direct purchase
#     item_type = request.GET.get('item_type')  # Get item type for direct purchase (cat, kitten, toy)
#
#     if item_id and item_type:
#         if item_type == 'cat':
#             item = get_object_or_404(Cat, id=item_id)
#             total_price = item.price
#         elif item_type == 'kitten':
#             item = get_object_or_404(Kitten, id=item_id)
#             total_price = item.price
#         elif item_type == 'toy':
#             item = get_object_or_404(Toy, id=item_id)
#             total_price = item.price
#         elif item_type == 'food':
#             item = get_object_or_404(Food, id=item_id)
#             total_price = item.price
#         else:
#             return render(request, 'payment.html', {'error': 'Invalid item type'})
#
#     if request.method == 'POST':
#         # Handle the payment form submission
#         name_on_card = request.POST.get('name_on_card')
#         card_number = request.POST.get('card_number')
#         expiry_date = request.POST.get('expiry_date')
#         cvv = request.POST.get('cvv')
#
#         # Handle missing form fields
#         if not name_on_card or not card_number or not expiry_date or not cvv:
#             return render(request, 'payment.html',
#                           {'error': 'Please fill in all required fields.', 'total_price': total_price})
#
#         # Save the payment record
#         Payment.objects.create(
#             user=request.user,
#             name_on_card=name_on_card,
#             card_number=card_number,
#             expiry_date=expiry_date,
#             cvv=cvv,
#             amount=total_price
#         )
#
#         # Redirect to a success page after payment
#         return redirect('payment_success')
#
#     return render(request, 'payment.html', {'total_price': total_price, 'item_id': item_id, 'item_type': item_type})
#


# def direct_purchase(request, item_id, item_type):
#     total_price = Decimal(0)  # Initialize total_price as 0
#
#     # Handle the direct purchase based on the item type (cat, kitten, toy)
#     if item_type == 'cat':
#         item = get_object_or_404(Cat, id=item_id)
#         total_price = item.price  # Set total price to the cat's price
#     elif item_type == 'kitten':
#         item = get_object_or_404(Kitten, id=item_id)
#         total_price = item.price  # Set total price to the kitten's price
#     elif item_type == 'toy':
#         item = get_object_or_404(Toy, id=item_id)
#         total_price = item.price  # Set total price to the toy's price
#
#     # Handle the payment form submission (POST)
#     if request.method == 'POST':
#         name_on_card = request.POST.get('name_on_card')
#         card_number = request.POST.get('card_number')
#         expiry_date = request.POST.get('expiry_date')
#         cvv = request.POST.get('cvv')
#
#         # Ensure total_price is a Decimal
#         total_price = Decimal(total_price)
#
#         # Handle missing form fields
#         if not name_on_card or not card_number or not expiry_date or not cvv:
#             return render(request, 'payment.html',
#                           {'error': 'Please fill in all required fields.', 'total_price': total_price})
#
#         # Save payment record
#         Payment.objects.create(
#             user=request.user,
#             name_on_card=name_on_card,
#             card_number=card_number,
#             expiry_date=expiry_date,
#             cvv=cvv,
#             amount=total_price
#         )
#
#         # Redirect to a success page after payment
#         return redirect('payment_success')
#
#     return render(request, 'payment.html', {'total_price': total_price, 'item_id': item_id, 'item_type': item_type})
#
#
# def cart_purchase(request):
#     if request.method == 'POST':
#         # Retrieve data from the form submission
#         name_on_card = request.POST.get('name_on_card')
#         card_number = request.POST.get('card_number')
#         expiry_date = request.POST.get('expiry_date')
#         cvv = request.POST.get('cvv')
#
#         # Calculate the total price from the user's cart items
#         cart_items = CartItem.objects.filter(user=request.user, purchased=False)
#         total_price = Decimal(0)
#
#         # Sum the price for each cart item based on its quantity and type
#         for cart_item in cart_items:
#             if isinstance(cart_item.content_object, Cat):
#                 total_price += cart_item.content_object.price * cart_item.quantity
#             elif isinstance(cart_item.content_object, Kitten):
#                 total_price += cart_item.content_object.price * cart_item.quantity
#             elif isinstance(cart_item.content_object, Toy):
#                 total_price += cart_item.content_object.price * cart_item.quantity
#
#         # Ensure the amount is a decimal
#         try:
#             amount = Decimal(total_price)
#         except:
#             amount = Decimal(0)
#
#         # Handle missing fields
#         if not name_on_card or not card_number or not expiry_date or not cvv:
#             return render(request, 'payment.html', {'error': 'Please fill in all required fields.', 'total_price': total_price})
#
#         # Save the payment to the database
#         Payment.objects.create(
#             user=request.user,
#             name_on_card=name_on_card,
#             card_number=card_number,
#             expiry_date=expiry_date,
#             cvv=cvv,
#             amount=amount
#         )
#
#         # Mark the cart items as purchased
#         if cart_items:
#             for cart_item in cart_items:
#                 cart_item.purchased = True
#                 cart_item.save()
#
#         # Redirect to a success page
#         return redirect('payment_success')
#
#     # Handle GET request and calculate the total price dynamically
#     cart_items = CartItem.objects.filter(user=request.user, purchased=False)
#     total_price = Decimal(0)
#
#     # Sum the price for each cart item based on its quantity and type
#     for cart_item in cart_items:
#         if isinstance(cart_item.content_object, Cat):
#             total_price += cart_item.content_object.price * cart_item.quantity
#         elif isinstance(cart_item.content_object, Kitten):
#             total_price += cart_item.content_object.price * cart_item.quantity
#         elif isinstance(cart_item.content_object, Toy):
#             total_price += cart_item.content_object.price * cart_item.quantity
#
#     return render(request, 'payment.html', {'total_price': total_price})

def toys(request):
    toys = Toy.objects.all()
    return render(request, 'toys.html', {'toys': toys})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('psswd')
        cpsswd = request.POST.get('cpsswd')
        if password == cpsswd:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                return redirect("register")
            else:
                lk = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )

                

                ok = Profile()
                ok.jk = lk
                ok.phone = request.POST['phone']
                ok.gender = request.POST['gender']
                ok.save()
                return redirect("login")
        else:
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psswd')
        if User.objects.filter(username=username).exists():
            k = User.objects.get(username=username)
            if k.check_password(password):
                if k:
                    auth.login(request, k)
                    return redirect('dashboard')
                else:
                    return render(request, 'login.html', {'error': "user does not exist"})
            else:
                return render(request, 'login.html', {'error': "password is incorrect"})
        else:
            return render(request, 'login.html', {'error': "username already exists"})
    else:
        return render(request, 'login.html', {'error': 'method is not post'})


def dashboard(request):
    return render(request, 'dashboard.html', {'username': request.user.username})


def logout(request):
    auth.logout(request)
    return redirect('register')


def aboutusl(request):
    about = Aboutus.objects.all()
    return render(request, 'aboutusl.html', {'about': about})


def catsl(request):
    cats = Cat.objects.all()
    kittens = Kitten.objects.all()
    return render(request, 'catsl.html', {'cats': cats, 'kittens': kittens})


def contactusl(request):
    contact = Contactus.objects.all()
    return render(request, 'contactusl.html', {'contact': contact})


def doctorl(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctorl.html', {'doctors': doctors})


def foodl(request):
    foods = Food.objects.all()
    foodk = Foodk.objects.all()
    return render(request, 'foodl.html', {'foods': foods, 'foodk': foodk})


def homepgl(request):
    return render(request, 'homepgl.html', {'username': request.user.username})


def toysl(request):
    toys = Toy.objects.all()
    return render(request, 'toysl.html', {'toys': toys})


def tablea(request):
    appointments = Appointment.objects.filter(user=request.user)  # Fetch all appointments
    return render(request, 'tablea.html', {'appointments': appointments})


def tablep(request):
    if request.user.is_authenticated:
        # Fetch only the logged-in user's payments, ordered by date (most recent first)
        payments = Payment.objects.filter(user=request.user, amount__isnull=False).order_by('-created_at')
        return render(request, 'tablep.html', {'payments': payments})
    else:
        # Redirect to login if user is not authenticated
        return redirect('login')


def add_to_cart(request, model_name, item_id):
    if request.user.is_authenticated:
        # Get the content type for the specified model
        content_type = ContentType.objects.get(model=model_name.lower())

        # Fetch the actual item object (e.g., Cat, Toy, etc.)
        item_model = content_type.model_class()  # Get the model class (Cat, Toy, etc.)
        item = get_object_or_404(item_model, id=item_id)

        # Debugging print to check the item and content type
        print(f"Adding item: {item}")
        print(f"Content Type: {content_type}")

        # Check if the item already exists in the cart for the user
        cart_item = CartItem.objects.filter(user=request.user, content_type=content_type, object_id=item.id).first()

        if cart_item:
            # If item exists in the cart, increment the quantity
            cart_item.quantity += 1
            cart_item.save()
            print(f"Item already in cart, new quantity: {cart_item.quantity}")
        else:
            # If item doesn't exist, create a new cart item
            CartItem.objects.create(
                user=request.user,
                content_type=content_type,
                object_id=item.id,
                quantity=1
            )
            print(f"Item added to cart: {item}")

        return redirect('cart')  # Redirect to the cart page
    else:
        return redirect('login')


def cart(request):
    if request.user.is_authenticated:
        # Fetch all cart items for the user
        cart_items = CartItem.objects.filter(user=request.user, purchased=False)

        # Debug: Print the content type and resolved content_object for all items
        print("Cart Items Fetched:")
        for item in cart_items:
            print(f"Item: {item.content_object}, Content Type: {item.content_type}, Quantity: {item.quantity}")

        # Calculate total price
        total_price = sum(item.content_object.price * item.quantity for item in cart_items)

        return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
    else:
        return redirect('login')




# def cart(request):
#     if request.user.is_authenticated:
#         # Fetch all cart items for the logged-in user
#         cart_items = CartItem.objects.filter(user=request.user)
#         return render(request, 'cart.html', {'cart_items': cart_items})
#     else:
#         return redirect('login')


def remove_from_cart(request, cart_item_id):
    if request.user.is_authenticated:
        CartItem.objects.filter(id=cart_item_id, user=request.user).delete()
        return redirect('cart')
    else:
        return redirect('login')


def payment_success(request):
    return render(request, 'payment_success.html')


def book_appo(request):
    return render(request, 'book_appo.html')


# def payment(request):
#     total_price = Decimal(0)  # Default total price
#
#     if request.method == 'POST':
#         # Handle the payment form submission
#         name_on_card = request.POST.get('name_on_card')
#         card_number = request.POST.get('card_number')
#         expiry_date = request.POST.get('expiry_date')
#         cvv = request.POST.get('cvv')
#
#         # Get the total price from the form submission (either from cart or direct)
#         total_price = request.POST.get('total_price')
#         if total_price:
#             total_price = Decimal(total_price)
#
#         # Handle missing form fields
#         if not name_on_card or not card_number or not expiry_date or not cvv:
#             return render(request, 'payment.html', {'error': 'Please fill in all required fields.', 'total_price': total_price})
#
#         # Save payment record
#         Payment.objects.create(
#             user=request.user,
#             name_on_card=name_on_card,
#             card_number=card_number,
#             expiry_date=expiry_date,
#             cvv=cvv,
#             amount=total_price
#         )
#
#         # Redirect to a success page after payment
#         return redirect('payment_success')
#
#     return render(request, 'payment.html', {'total_price': total_price})

#########################################################################################
# def payment(request):
#     total_price = Decimal(0)  # Default total price
#
#     if request.method == 'POST':
#         # Handle the payment form submission
#         name_on_card = request.POST.get('name_on_card')
#         card_number = request.POST.get('card_number')
#         expiry_date = request.POST.get('expiry_date')
#         cvv = request.POST.get('cvv')
#
#         # Get the total price from the form submission (either from cart or direct)
#         total_price = request.POST.get('total_price')
#         if total_price:
#             total_price = Decimal(total_price)
#
#         # Handle missing form fields
#         if not name_on_card or not card_number or not expiry_date or not cvv:
#             return render(request, 'payment.html',
#                           {'error': 'Please fill in all required fields.', 'total_price': total_price})
#
#         # Save payment record
#         Payment.objects.create(
#             user=request.user,
#             name_on_card=name_on_card,
#             card_number=card_number,
#             expiry_date=expiry_date,
#             cvv=cvv,
#             amount=total_price
#         )
#
#         # Redirect to a success page after payment
#         return redirect('payment_success')
#
#     return render(request, 'payment.html', {'total_price': total_price})
#
#
# def direct_purchase(request, item_id=None, item_type=None):
#     total_price = Decimal(0)
#     item = None
#
#     if item_id and item_type:
#         if item_type == 'cat':
#             item = get_object_or_404(Cat, id=item_id)
#         elif item_type == 'kitten':
#             item = get_object_or_404(Kitten, id=item_id)
#         elif item_type == 'toy':
#             item = get_object_or_404(Toy, id=item_id)
#         else:
#             return HttpResponse("Invalid item type.", status=400)
#
#         total_price = item.price  # Get the price for the direct purchase
#
#     # If the item was not found or item_id/item_type is missing
#     if not item:
#         return HttpResponse("Item not found or invalid item.", status=400)
#
#     # Process the form if it's a POST request
#     if request.method == 'POST':
#         name_on_card = request.POST.get('name_on_card')
#         card_number = request.POST.get('card_number')
#         expiry_date = request.POST.get('expiry_date')
#         cvv = request.POST.get('cvv')
#
#         # Validate form fields
#         if not all([name_on_card, card_number, expiry_date, cvv]):
#             return render(request, 'payment.html', {
#                 'error': 'Please fill in all required fields.',
#                 'total_price': total_price,
#                 'item_id': item_id,
#                 'item_type': item_type
#             })
#
#         # Save the payment record to the database
#         Payment.objects.create(
#             user=request.user,  # Assuming you have user authentication
#             name_on_card=name_on_card,
#             card_number=card_number,
#             expiry_date=expiry_date,
#             cvv=cvv,
#             amount=total_price
#         )
#
#         # Redirect to a success page after payment
#         return redirect('payment_success')
#
#     # Render the payment page initially
#     return render(request, 'payment.html', {
#         'total_price': total_price,
#         'item_id': item_id,  # Pass item_id here
#         'item_type': item_type  # Pass item_type here
#     })
#
#
# def cart_purchase(request):
#     if request.method == 'POST':
#         # Retrieve data from the form submission
#         name_on_card = request.POST.get('name_on_card')
#         card_number = request.POST.get('card_number')
#         expiry_date = request.POST.get('expiry_date')
#         cvv = request.POST.get('cvv')
#
#         # Calculate the total price from the user's cart items
#         cart_items = CartItem.objects.filter(user=request.user, purchased=False)
#         total_price = Decimal(0)
#
#         # Sum the price for each cart item based on its quantity and type
#         for cart_item in cart_items:
#             if isinstance(cart_item.content_object, Cat):
#                 total_price += cart_item.content_object.price * cart_item.quantity
#             elif isinstance(cart_item.content_object, Kitten):
#                 total_price += cart_item.content_object.price * cart_item.quantity
#             elif isinstance(cart_item.content_object, Toy):
#                 total_price += cart_item.content_object.price * cart_item.quantity
#
#         # Ensure the amount is a decimal
#         try:
#             amount = Decimal(total_price)
#         except:
#             amount = Decimal(0)
#
#         # Handle missing fields
#         if not name_on_card or not card_number or not expiry_date or not cvv:
#             return render(request, 'payment.html',
#                           {'error': 'Please fill in all required fields.', 'total_price': total_price})
#
#         # Save the payment to the database
#         Payment.objects.create(
#             user=request.user,
#             name_on_card=name_on_card,
#             card_number=card_number,
#             expiry_date=expiry_date,
#             cvv=cvv,
#             amount=amount
#         )
#
#         # Mark the cart items as purchased
#         if cart_items:
#             for cart_item in cart_items:
#                 cart_item.purchased = True
#                 cart_item.save()
#
#         # Redirect to a success page
#         return redirect('payment_success')
#
#     # Handle GET request and calculate the total price dynamically
#     cart_items = CartItem.objects.filter(user=request.user, purchased=False)
#     total_price = Decimal(0)
#
#     # Sum the price for each cart item based on its quantity and type
#     for cart_item in cart_items:
#         if isinstance(cart_item.content_object, Cat):
#             total_price += cart_item.content_object.price * cart_item.quantity
#         elif isinstance(cart_item.content_object, Kitten):
#             total_price += cart_item.content_object.price * cart_item.quantity
#         elif isinstance(cart_item.content_object, Toy):
#             total_price += cart_item.content_object.price * cart_item.quantity
#
#     return render(request, 'payment.html', {'total_price': total_price})

#########################################################################################################

def payment(request, item_id=None, item_type=None):
    # Check if the request is for a cart payment
    if item_type == 'cart':
        cart_items = CartItem.objects.filter(user=request.user, purchased=False)
        total_price = sum(item.content_object.price * item.quantity for item in cart_items)
    else:
        # Your existing logic for handling individual item payment
        ITEM_MODELS = {
            'cat': Cat,
            'kitten': Kitten,
            'toy': Toy,
            'food': Food,
            'foodk': Foodk,
        }

        if not item_id or not item_type:
            return HttpResponse("Missing item ID or type.", status=400)

        model = ITEM_MODELS.get(item_type)
        if not model:
            return HttpResponse("Invalid item type.", status=400)

        item = get_object_or_404(model, id=item_id)
        total_price = round(Decimal(item.price), 2)

    if request.method == 'POST':
        # Get payment details from the form
        name_on_card = request.POST.get('name_on_card')
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')

        # Debugging print statements
        print(f"Name on card: {name_on_card}")
        print(f"Card number: {card_number}")
        print(f"Expiry date: {expiry_date}")
        print(f"CVV: {cvv}")

        # Check if any of the required fields are missing
        if not all([name_on_card, card_number, expiry_date, cvv]):
            messages.error(request, "Please fill in all required fields.")
            return redirect(request.path)

        # Basic validation for CVV and expiry date format (You can add more regex checks here)
        if len(cvv) != 3:  # CVV is typically 3 digits for most card types
            messages.error(request, "Invalid CVV.")
            return redirect(request.path)

        # Validate if the total price is valid
        if total_price <= 0:
            messages.error(request, "Invalid price.")
            return redirect(request.path)

        # Mask the card number (for security)
        masked_card_number = card_number[-4:].rjust(len(card_number), "*")  # Mask all but last 4 digits

        # Save the payment details
        payment = Payment.objects.create(
            user=request.user,
            name_on_card=name_on_card,
            card_number=masked_card_number,
            expiry_date=expiry_date,
            cvv=cvv,  # Don't store CVV, it should be handled by a secure gateway
            amount=total_price
        )

        # Handle cart items payment (if it's a cart)
        if item_type == 'cart':
            for cart_item in cart_items:
                # You can create a payment entry for each cart item or just process the total amount
                cart_item.purchased = True
                cart_item.save()

        # Show success message
        messages.success(request, "Payment successful!")
        return redirect('payment_success')

    return render(request, 'payment.html', {
        'total_price': total_price,
        'cart_items': cart_items if item_type == 'cart' else None,
    })
