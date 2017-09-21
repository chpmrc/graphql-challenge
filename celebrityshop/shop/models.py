from django.db import models
from django.contrib.auth.models import User


class Celebrity(models.Model):
  name = models.TextField()
  age = models.IntegerField()

  def __str__(self):
    return self.name


class Item(models.Model):
  VISIBILITY_PUBLIC = "public"
  VISIBILITY_AUTHENTICATED = "authenticated"
  VISIBILITY_CHOICES = (
    (VISIBILITY_PUBLIC, VISIBILITY_PUBLIC),
    (VISIBILITY_AUTHENTICATED, VISIBILITY_AUTHENTICATED)
  )

  name = models.TextField()
  quantity = models.IntegerField()
  price = models.FloatField()
  visibility = models.TextField(choices=VISIBILITY_CHOICES, default=VISIBILITY_PUBLIC)
  celebrities = models.ManyToManyField("Celebrity", related_name="items")

  @property
  def remaining(self):
    return self.quantity - Purchase.objects.filter(item__pk=self.pk).count()

  def __str__(self):
      return self.name


class Purchase(models.Model):
  buyer = models.ForeignKey(User)
  item = models.ForeignKey("Item")
  quantity = models.IntegerField()

  def __str__(self):
    return '%s bought %d of %s' % (self.buyer, self.quantity, self.item)
