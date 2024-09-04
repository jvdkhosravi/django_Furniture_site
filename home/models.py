from audioop import reverse

from django.contrib.auth.models import User
from django.db import models


class Testimonial(models.Model):
    quote = models.TextField()
    author_name = models.CharField(max_length=100)
    author_title = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.quote

    class Meta:
        verbose_name = 'گواهینامه'
        verbose_name_plural = 'گواهینامه ها'


class NewsletterSubscription(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)


class WhyChooseUs(models.Model):
    icon = models.ImageField(upload_to='why-choose-us-icons')
    title = models.CharField(max_length=100)
    description = models.TextField()
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering']


class WhyChooseUsImage(models.Model):
    image = models.ImageField(upload_to='why-choose-us-images')
    alt_text = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.alt_text or f'Why Choose Us Image {self.pk}'


class WeHelpSection(models.Model):
    grid_1_image = models.ImageField(upload_to='we-help-section-images')
    grid_2_image = models.ImageField(upload_to='we-help-section-images')
    grid_3_image = models.ImageField(upload_to='we-help-section-images')
    title = models.CharField(max_length=100)
    description = models.TextField()
    list_item_1 = models.CharField(max_length=100)
    list_item_2 = models.CharField(max_length=100)
    list_item_3 = models.CharField(max_length=100)
    list_item_4 = models.CharField(max_length=100)

