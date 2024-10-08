#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils import timezone
import uuid
from PIL import Image
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


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
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    photo = models.ImageField(upload_to='images/')
    left = models.BooleanField()
    right = models.BooleanField()
    srodek = models.BooleanField()
    bez = models.BooleanField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

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
