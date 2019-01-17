from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id =user_id)
            if has_contacted:
                messages.error(request, 'You have already enquired about this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        #Send mail
        send_mail(
        'Property Listing Enquiry',
        'There has been an enquiry for ' + listing + '. Sign into the admin panel for more information.',
        'bdickson1212@gmail.com',
        [realtor_email, 'brandybkk@gmail.com'],
        fail_silently=False
        )

        messages.success(request, 'Thank you, a member of our team will be in touch shortly')
        return redirect('/listings/'+listing_id)
