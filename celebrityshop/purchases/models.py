from django.db import models
from django.contrib.auth.models import User

from celebrityshop.honey.models import Costume


class Purchase(models.Model):
    """
    Purchase model for costume.
    """
    costume = models.ForeignKey(Costume, related_name='purchase_items', verbose_name='Costume')
    user = models.ForeignKey(User, related_name='purchase_items', verbose_name='User')
    quantity = models.IntegerField(verbose_name='Quantity', default=1)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

    def __str__(self):
        return '{user} - {item}'.format(user=self.user, item=self.costume)
