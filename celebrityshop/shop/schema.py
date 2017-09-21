import graphene
from graphene_django.types import DjangoObjectType

from celebrityshop.shop.models import Item, Celebrity


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


class CelebrityType(DjangoObjectType):
    class Meta:
        model = Celebrity
        exclude_fields = ['visibility']


class Query(graphene.AbstractType):
    list_items = graphene.List(ItemType)
    list_celebrities = graphene.List(CelebrityType)

    def resolve_list_items(self, info):
      if info.context.user.is_authenticated():
        return Item.objects.all()
      return Item.objects.filter(visibility=Item.VISIBILITY_PUBLIC)

    def resolve_list_celebrities(self, info):
      return Celebrity.objects.all()