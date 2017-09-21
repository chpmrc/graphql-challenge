import graphene
from graphene_django.types import DjangoObjectType

from celebrityshop.shop.models import Item, Celebrity, Purchase


class ItemType(DjangoObjectType):
    remaining = graphene.Int(source='remaining')

    class Meta:
        model = Item


class CelebrityType(DjangoObjectType):
    class Meta:
        model = Celebrity
        exclude_fields = ['visibility']


class PurchaseType(DjangoObjectType):
    class Meta:
        model = Purchase


class Query(graphene.AbstractType):
    list_items = graphene.List(ItemType)
    list_celebrities = graphene.List(CelebrityType)
    retrieve_item = graphene.Field(ItemType, pk=graphene.Int())

    def resolve_list_items(self, info):
      if info.context.user.is_authenticated():
        return Item.objects.all()
      return Item.objects.filter(visibility=Item.VISIBILITY_PUBLIC)

    def resolve_list_celebrities(self, info):
      return Celebrity.objects.all()

    def resolve_retrieve_item(self, info, pk=None):
      if not pk:
        return None
      return Item.objects.get(pk=pk)


class PurchaseInput(graphene.InputObjectType):
      item = graphene.Int(required=True)
      quantity = graphene.Int(required=True)


class CreatePurchase(graphene.Mutation):
    class Arguments:
      purchase_data = PurchaseInput(required=True)

    purchase = graphene.Field(PurchaseType)

    @staticmethod
    def mutate(root, info, purchase_data=None):
      buyer = info.context.user
      item = Item.objects.get(pk=purchase_data['item'])
      quantity = purchase_data['quantity']
      purchase = Purchase.objects.create(buyer=buyer, item=item, quantity=quantity)
      return CreatePurchase(purchase=purchase)


class Mutation(graphene.AbstractType):
  create_purchase = CreatePurchase.Field()
