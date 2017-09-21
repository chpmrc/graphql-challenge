import graphene
from graphene_django.types import DjangoObjectType

from celebrityshop.shop.models import Item, Celebrity


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


class CelebrityType(DjangoObjectType):
    class Meta:
        model = Celebrity


class Query(graphene.AbstractType):
    list_items = graphene.List(ItemType)