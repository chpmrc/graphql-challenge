from django.db import models


class Celebrity(models.Model):
    """
    Celebrity model.
    """
    name = models.CharField(verbose_name='Name', max_length=255)
    age = models.IntegerField(verbose_name='Age')

    class Meta:
        verbose_name = 'Celebrity'
        verbose_name_plural = 'Celebrities'

    def __str__(self):
        return self.name


class Costume(models.Model):
    """
    Costume model.
    """
    VISIBILITY_PUBLIC_CHOICE = ('public', 'Public')
    VISIBILITY_PRIVATE_CHOICE = ('private', 'Private')
    VISIBILITY_CHOICES = (
        VISIBILITY_PUBLIC_CHOICE,
        VISIBILITY_PRIVATE_CHOICE
    )

    name = models.CharField(verbose_name='Name', max_length=255)
    price = models.FloatField(verbose_name='Price')
    celebrities = models.ManyToManyField(Celebrity, related_name='costumes', verbose_name='celebrities',
                                         blank=True, null=True)
    quantity = models.IntegerField(verbose_name='Quantity')
    visibility = models.CharField(verbose_name='Visibility', max_length=255,
                                  choices=VISIBILITY_CHOICES, default=VISIBILITY_PUBLIC_CHOICE)

    class Meta:
        verbose_name = 'Costume',
        verbose_name_plural = 'Costumes'

    def __str__(self):
        return self.name


