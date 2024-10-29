from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpRequest
from django.utils import timezone
from django.urls import reverse
import mysite.settings
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import ServicesForm, QualForm, ContactFormForm, BlogSForm, BlogBWForm, PostSForm, PostBWForm
from BW.models import Services, Qualifications, Contakt, Start, BlogBW, BlogS, PostBW, PostS
import os
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.contrib.auth import login
from django.contrib.auth.models import User
from . import models
from mysite.settings import STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET, ALLOWED_HOSTS

def start(request):
    starts = Start.objects.all().order_by()
    return render(request, 'start.html', {'starts': starts})

def error_404_view(request, exception):
    assert isinstance(request, HttpRequest)
    return render(request, '404.html', None, None, 404)

def qualifications(request):
    quals = Qualifications.objects.all().order_by('-published_date')
    return render(request, 'qualifications.html', {'quals': quals})

def qualifications_new(request):
    if request.method == "POST":
        form = QualForm(request.POST, request.FILES)
        if form.is_valid():
            qual = form.save(commit=False)
            qual.published_date = timezone.now()
            qual.save()
            return redirect('about_us')
    else:
        form = QualForm()
    return render(request, 'qual/qual_new.html', {'form': form})


def qualifications_edit(request, pk):
    qual = get_object_or_404(Qualifications, pk=pk)
    if request.method == "POST":
        form = QualForm(request.POST, request.FILES, instance=qual)
        if form.is_valid():
            qual = form.save(commit=False)
            qual.published_date = timezone.now()
            qual.save()
            return redirect('about_us')
    else:
        form = QualForm(instance=qual)
    return render(request, 'qual/qual_edit.html', {'form': form})

def qualifications_delete(request, pk):
    qual = get_object_or_404(Qualifications, pk=pk)
    qual.delete()
    return redirect(reverse('about_us'))

def services(request):
    services = Services.objects.all().order_by('-published_date')
    return render(request, 'services.html', {'services': services})

def services_new(request):
    if request.method == "POST":
        form = ServicesForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.published_date = timezone.now()
            service.save()
            return redirect('services')
    else:
        form = ServicesForm()
    return render(request, 'serv/serv_new.html', {'form': form})


def services_edit(request, pk):
    service = get_object_or_404(Services, pk=pk)
    if request.method == "POST":
        form = ServicesForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            service = form.save(commit=False)
            service.published_date = timezone.now()
            service.save()
            return redirect('services')
    else:
        form = ServicesForm(instance=service)
    return render(request, 'serv/serv_edit.html', {'form': form})

def services_delete(request, pk):
    service = get_object_or_404(Services, pk=pk)
    service.delete()
    return redirect(reverse('services'))

def post_list_BW(request):
    blogs = BlogBW.objects.all().order_by('-published_date')
    return render(request, 'blogBW.html', {'blogs': blogs})

def post_detail_BW(request, pk):
    blog = get_object_or_404(BlogBW, pk=pk)
    posts = PostBW.objects.filter(blog=blog)

    return render(request, 'BastianWorld/post_detail.html', {
        'blog': blog,
        'posts': posts,
    })

def post_new_BW(request):
    if request.method == "POST":
        form = BlogBWForm(request.POST, request.FILES)
        if form.is_valid():
            blogBW = form.save(commit=False)
            blogBW.published_date = timezone.now()
            blogBW.save()
            return redirect('blog')
    else:
        form = BlogBWForm()
    return render(request, 'BastianWorld/post_new.html', {'form': form})


def post_edit_BW(request, pk):
    blogBW = get_object_or_404(BlogBW, pk=pk)
    if request.method == "POST":
        form = BlogBWForm(request.POST, request.FILES, instance=blogBW)
        if form.is_valid():
            blogBW = form.save(commit=False)
            blogBW.published_date = timezone.now()
            blogBW.save()
            return redirect('blog')
    else:
        form = BlogBWForm(instance=blogBW)
    return render(request, 'BastianWorld/post_edit.html', {'form': form})

def post_delete_BW(request, pk):
    blogBW = get_object_or_404(BlogBW, pk=pk)
    blogBW.delete()
    return redirect(reverse('blog'))

def post_post_new_BW(request, blog_pk):
    blog = get_object_or_404(BlogBW, pk=blog_pk)
    if request.method == "POST":
        form = PostBWForm(request.POST, request.FILES)
        if form.is_valid():
            postBW = form.save(commit=False)
            postBW.blog = blog
            postBW.published_date = timezone.now()
            postBW.save()
            return redirect('post_detail_BW', pk=blog.pk)
    else:
        form = PostBWForm()
    return render(request, 'BastianWorld/post_post_new.html', {'form': form, 'blog': blog})


def post_post_edit_BW(request, blog_pk, pk):
    blog = get_object_or_404(BlogBW, pk=blog_pk)
    postBW = get_object_or_404(PostBW, pk=pk)
    if request.method == "POST":
        form = PostBWForm(request.POST, request.FILES, instance=postBW)
        if form.is_valid():
            postBW = form.save(commit=False)
            postBW.published_date = timezone.now()
            postBW.save()
            return redirect('post_detail_BW', pk=blog.pk)
    else:
        form = PostBWForm(instance=postBW)
    return render(request, 'BastianWorld/post_post_edit.html', {'form': form, 'blog': blog})

def post_post_delete_BW(request, pk):
    postBW = get_object_or_404(PostBW, pk=pk)
    postBW.delete()
    return redirect(reverse('post_detail_BW'))

def post_list_S(request):
    blogs = BlogS.objects.all().order_by('-published_date')
    return render(request, 'blogS.html', {'blogs': blogs})


def post_detail_S(request, pk):
    blog = get_object_or_404(BlogS, pk=pk)
    posts = PostS.objects.filter(blog=blog)

    return render(request, 'Services/post_detail.html', {
        'blog': blog,
        'posts': posts,
    })


def post_new_S(request):
    if request.method == "POST":
        form = BlogSForm(request.POST, request.FILES)
        if form.is_valid():
            blogS = form.save(commit=False)
            blogS.published_date = timezone.now()
            blogS.save()
            return redirect('blogS')
    else:
        form = BlogSForm()
    return render(request, 'Services/post_new.html', {'form': form})


def post_edit_S(request, pk):
    blogS = get_object_or_404(BlogS, pk=pk)
    if request.method == "POST":
        form = BlogSForm(request.POST, request.FILES, instance=blogS)
        if form.is_valid():
            blogS = form.save(commit=False)
            blogS.published_date = timezone.now()
            blogS.save()
            return redirect('blogS')
    else:
        form = BlogSForm(instance=blogS)
    return render(request, 'Services/post_edit.html', {'form': form})

def post_delete_S(request, pk):
    blogS = get_object_or_404(BlogS, pk=pk)
    blogS.delete()
    return redirect(reverse('blogS'))

def post_post_new_S(request,blog_pk):
    blog = get_object_or_404(BlogS, pk=blog_pk)
    if request.method == "POST":
        form = PostSForm(request.POST, request.FILES)
        if form.is_valid():
            postS = form.save(commit=False)
            postS.blog = blog
            postS.published_date = timezone.now()
            postS.save()
            return redirect('post_detail_S', pk=blog.pk)
    else:
        form = PostBWForm()
    return render(request, 'Services/post_post_new.html', {'form': form, 'blog': blog})


def post_post_edit_S(request, blog_pk, pk):
    blog = get_object_or_404(BlogS, pk=blog_pk)
    postS = get_object_or_404(PostS, pk=pk)
    if request.method == "POST":
        form = PostSForm(request.POST, request.FILES, instance=postS)
        if form.is_valid():
            postS = form.save(commit=False)
            postS.published_date = timezone.now()
            postS.save()
            return redirect('post_detail_S', pk=blog.pk)
    else:
        form = PostSForm(instance=postS)
    return render(request, 'Services/post_post_edit.html', {'form': form, 'blog': blog})

def post_post_delete_S(request, pk):
    postS = get_object_or_404(PostS, pk=pk)
    postS.delete()
    return redirect(reverse('post_detail_S'))


def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact_email_created(contact)  # Zmieniamy na przekazanie obiektu
            messages.success(request, 'Wiadomość została wysłana. Skontaktujemy się z Tobą!')
            return redirect('contact.html')
    else:
        form = ContactFormForm()

    contacts = Contakt.objects.all()
    return render(request, 'contact.html', {'form': form, 'contacts': contacts})


def contact_email_created(contact):
    formatted_date = contact.created_date.strftime('%d-%m-%Y')

    subject = f'BastianWorld - Zapytanie - {contact.temat}'
    message = f"""Imię i nazwisko: {contact.dane}
Numer telefonu: {contact.nrtel}
Email: {contact.email}

Wiadomość: {contact.wiadomosc}

Data: {formatted_date}
"""

    subject_client = f'BastianWorld - Potwierdzenie wysłania wiadomości'
    message_client = f""" Witam, poniżej przesyłam potwierdzenie wysłania wiadomości do BastianWorld.

Szczegóły:

Temat: {contact.temat}
Imię i nazwisko: {contact.dane}
Numer telefonu: {contact.nrtel}
Email: {contact.email}

Wiadomość: {contact.wiadomosc}

Data: {formatted_date}

Skontaktujemy się z Państwem drogą mailową albo telefoniczną najszybciej jak to będzie możliwe.

Miłego dnia
Zespół BastianWorld


Wiadomość została wygenerowana automatycznie.
    """

    email = EmailMessage(
        subject,
        message,
        mysite.settings.DEFAULT_FROM_EMAIL,
        ['paszko08042004@gmail.com']
    )

    email_client = EmailMessage(
        subject_client,
        message_client,
        mysite.settings.DEFAULT_FROM_EMAIL,
        [contact.email]
    )

    email.send()
    email_client.send()



def send_question_email_view(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact = form.save()  # Save the form and create the contact object
            contact_email_created(contact)  # Pass the contact object here
            messages.success(request, 'Wiadomość została wysłana do BastianWorld. Skontaktujemy się z Tobą!')
            return redirect('contact')
        else:
            print(form.errors)  # Debugging - print any form errors to the console
    else:
        form = ContactFormForm()

    return render(request, 'contact.html', {'form': form})



DOMAIN = ALLOWED_HOSTS
stripe.api_key = STRIPE_SECRET_KEY


def subscribe(request) -> HttpResponse:
    # We login a sample user for the demo.
    user, created = User.objects.get_or_create(
        username='AlexG', email="alexg@example.com"
    )
    if created:
        user.set_password('password')
        user.save()
    login(request, user)
    request.user = user

    return render(request, 'profile.html')


def cancel(request) -> HttpResponse:
    return render(request, 'Profil/cancel.html')


def success(request) -> HttpResponse:

    print(f'{request.session = }')

    stripe_checkout_session_id = request.GET['session_id']

    return render(request, 'Profil/success.html')


def create_checkout_session(request) -> HttpResponse:
    price_lookup_key = request.POST['price_lookup_key']
    try:
        prices = stripe.Price.list(lookup_keys=[price_lookup_key], expand=['data.product'])
        price_item = prices.data[0]

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {'price': price_item.id, 'quantity': 1},
                # You could add differently priced services here, e.g., standard, business, first-class.
            ],
            mode='subscription',
            success_url=DOMAIN + reverse('success') + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=DOMAIN + reverse('cancel')
        )

        # We connect the checkout session to the user who initiated the checkout.
        models.CheckoutSessionRecord.objects.create(
            user=request.user,
            stripe_checkout_session_id=checkout_session.id,
            stripe_price_id=price_item.id,
        )

        return redirect(
            checkout_session.url,  # Either the success or cancel url.
            code=303
        )
    except Exception as e:
        print(e)
        return HttpResponse("Server error", status=500)


def direct_to_customer_portal(request) -> HttpResponse:
    """
    Creates a customer portal for the user to manage their subscription.
    """
    checkout_record = models.CheckoutSessionRecord.objects.filter(
        user=request.user
    ).last()  # For demo purposes, we get the last checkout session record the user created.

    checkout_session = stripe.checkout.Session.retrieve(checkout_record.stripe_checkout_session_id)

    portal_session = stripe.billing_portal.Session.create(
        customer=checkout_session.customer,
        return_url=DOMAIN + reverse('subscribe')  # Send the user here from the portal.
    )
    return redirect(portal_session.url, code=303)


@csrf_exempt
def collect_stripe_webhook(request) -> JsonResponse:
    """
    Stripe sends webhook events to this endpoint.
    We verify the webhook signature and updates the database record.
    """
    webhook_secret = STRIPE_WEBHOOK_SECRET
    signature = request.META["HTTP_STRIPE_SIGNATURE"]
    payload = request.body

    try:
        event = stripe.Webhook.construct_event(
            payload=payload, sig_header=signature, secret=webhook_secret
        )
    except ValueError as e:  # Invalid payload.
        raise ValueError(e)
    except stripe.error.SignatureVerificationError as e:  # Invalid signature
        raise stripe.error.SignatureVerificationError(e)

    _update_record(event)

    return JsonResponse({'status': 'success'})


def _update_record(webhook_event) -> None:
    """
    We update our database record based on the webhook event.

    Use these events to update your database records.
    You could extend this to send emails, update user records, set up different access levels, etc.
    """
    data_object = webhook_event['data']['object']
    event_type = webhook_event['type']

    if event_type == 'checkout.session.completed':
        checkout_record = models.CheckoutSessionRecord.objects.get(
            stripe_checkout_session_id=data_object['id']
        )
        checkout_record.stripe_customer_id = data_object['customer']
        checkout_record.has_access = True
        checkout_record.save()
        print('🔔 Payment succeeded!')
    elif event_type == 'customer.subscription.created':
        print('🎟️ Subscription created')
    elif event_type == 'customer.subscription.updated':
        print('✍️ Subscription updated')
    elif event_type == 'customer.subscription.deleted':
        checkout_record = models.CheckoutSessionRecord.objects.get(
            stripe_customer_id=data_object['customer']
        )
        checkout_record.has_access = False
        checkout_record.save()
        print('✋ Subscription canceled: %s', data_object.id)


@login_required
def profile(request):
    try:
        subscription = models.CheckoutSessionRecord.objects.filter(user=request.user).latest('created_at')
    except models.CheckoutSessionRecord.DoesNotExist:
        subscription = None

    return render(request, 'profile.html', {
        'subscription': subscription,
    })