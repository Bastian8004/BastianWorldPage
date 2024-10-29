#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils import timezone
import uuid
from django.conf import settings
from PIL import Image
from django.db import models
from django.contrib.auth.models import User


class BlogBW(models.Model):
    tytul = models.CharField(max_length=70, blank=True, null=True)
    opis = models.TextField(max_length=1024, blank=True, null=True)
    zdjecie = models.ImageField(upload_to='albums', blank=True, null=True)
    lewo = models.BooleanField()
    prawo = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.tytul if self.tytul else 'Bez tytułu'

    def data(self):
        if self.created_date:
            return self.created_date.strftime('%d-%m-%Y, %H:%M')
        return "Brak daty"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.zdjecie:
            img = Image.open(self.zdjecie.path)

            # Ustal maksymalną szerokość i wysokość
            max_width = 800
            max_height = 600

            # Sprawdź, czy obraz wymaga zmiany rozmiaru
            if img.height > max_height or img.width > max_width:
                output_size = (max_width, max_height)
                img.thumbnail(output_size)  # Zmienia rozmiar z zachowaniem proporcji
                img.save(self.zdjecie.path)

class PostBW(models.Model):
    blog = models.ForeignKey(BlogBW, on_delete=models.CASCADE)
    tytul = models.CharField(max_length=70, blank=True, null=True, default="")
    opis = models.TextField(max_length=2048, blank=True, null=True)
    zdjecie = models.ImageField(upload_to='albums', blank=True, null=True)
    lewo = models.BooleanField()
    prawo = models.BooleanField()
    srodek = models.BooleanField()
    bez = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.tytul if self.tytul else ''

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.zdjecie:
            img = Image.open(self.zdjecie.path)

            # Ustal maksymalną szerokość i wysokość
            max_width = 800
            max_height = 600

            # Sprawdź, czy obraz wymaga zmiany rozmiaru
            if img.height > max_height or img.width > max_width:
                output_size = (max_width, max_height)
                img.thumbnail(output_size)  # Zmienia rozmiar z zachowaniem proporcji
                img.save(self.zdjecie.path)


class BlogS(models.Model):
    tytul = models.CharField(max_length=70, blank=True, null=True)
    opis = models.TextField(max_length=1024, blank=True, null=True)
    zdjecie = models.ImageField(upload_to='albums', blank=True, null=True)
    lewo = models.BooleanField()
    prawo = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.tytul if self.tytul else 'Bez tytułu'

    def data(self):
        if self.created_date:
            return self.created_date.strftime('%d-%m-%Y, %H:%M')
        return "Brak daty"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.zdjecie:
            img = Image.open(self.zdjecie.path)

            # Ustal maksymalną szerokość i wysokość
            max_width = 800
            max_height = 600

            # Sprawdź, czy obraz wymaga zmiany rozmiaru
            if img.height > max_height or img.width > max_width:
                output_size = (max_width, max_height)
                img.thumbnail(output_size)  # Zmienia rozmiar z zachowaniem proporcji
                img.save(self.zdjecie.path)


class PostS(models.Model):
    blog = models.ForeignKey(BlogS, on_delete=models.CASCADE)
    tytul = models.CharField(max_length=70, blank=True, null=True, default="")
    opis = models.TextField(max_length=2048, blank=True, null=True)
    zdjecie = models.ImageField(upload_to='albums', blank=True, null=True)
    lewo = models.BooleanField()
    prawo = models.BooleanField()
    srodek = models.BooleanField()
    bez = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.tytul if self.tytul else ''

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.zdjecie:
            img = Image.open(self.zdjecie.path)

            # Ustal maksymalną szerokość i wysokość
            max_width = 800
            max_height = 600

            # Sprawdź, czy obraz wymaga zmiany rozmiaru
            if img.height > max_height or img.width > max_width:
                output_size = (max_width, max_height)
                img.thumbnail(output_size)  # Zmienia rozmiar z zachowaniem proporcji
                img.save(self.zdjecie.path)


class Services(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True)
    photo = models.ImageField(upload_to='albums', blank=True, null=True)
    left = models.BooleanField()
    right = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Qualifications(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, default="")
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    lewo = models.BooleanField()
    prawo = models.BooleanField()
    srodek = models.BooleanField(null=True, blank=True, default=False)
    bez = models.BooleanField(null=True, blank=True, default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        if self.title:  # Sprawdzenie, czy tytuł nie jest pusty
            return self.title
        elif self.published_date:  # Jeśli tytuł jest pusty, ale jest data publikacji
            return str(self.published_date)
        else:
            return "Brak tytułu i daty publikacji"

class Contakt(models.Model):
    Nazwa = models.CharField(max_length=70,blank=True, null=True)
    NrTel = models.CharField(max_length=70,blank=True, null=True)
    EMail = models.CharField(max_length=70,blank=True, null=True)
    GitHub = models.CharField(max_length=200,blank=True, null=True)
    LinkedIn = models.CharField(max_length=200,blank=True, null=True)
    Facebook = models.CharField(max_length=200,blank=True, null=True)

class ContaktForm(models.Model):
    dane = models.CharField(max_length=100,blank=True, null=True)
    temat = models.CharField(max_length=200,blank=True, null=True)
    nrtel = models.CharField(max_length=70,blank=True, null=True)
    email = models.CharField(max_length=70,blank=True, null=True)
    wiadomosc = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def send(self):
        self.created_date = timezone.now()
        self.save()


class Start(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True)

class CheckoutSessionRecord(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text="The user who initiated the checkout."
    )
    stripe_customer_id = models.CharField(max_length=255)
    stripe_checkout_session_id = models.CharField(max_length=255)
    stripe_price_id = models.CharField(max_length=255)
    has_access = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)  # Add this line

    def __str__(self):
        return f"Subskrypcja - {self.user}"
