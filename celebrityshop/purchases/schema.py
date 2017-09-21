import graphene
from django.contrib.auth.models import User

from graphene_django.types import DjangoObjectType

from celebrityshop.honey.models import Costume
from celebrityshop.purchases.models import Purchase


class PurchaseType(DjangoObjectType):
    """
    Purchase Type
    """
    class Meta:
        model = Purchase


class CreatePurchase(graphene.Mutation):
    """
    Create Purchase
    """
    costume = graphene.Int()
    user = graphene.Int()
    quantity = graphene.Int()

    class Arguments:
        costume = graphene.Int()
        user = graphene.Int()
        quantity = graphene.Int()

    @staticmethod
    def mutate(self, info, *args, **kwargs):
        if info.context.user.is_authenticated():
            costume = kwargs.get('costume')
            user = kwargs.get('user')
            quantity = kwargs.get('quantity')
            costume = Costume.objects.get(id=costume)
            user = User.objects.get(id=user)
            differ = costume.quantity - quantity
            if differ > 0:
                purchase = Purchase(costume=costume, user=user, quantity=quantity)
                purchase.save()
                costume.quantity = differ
                costume.save()

                return CreatePurchase(costume=costume.id, user=user.id, quantity=quantity)
            else:
                # TODO: information to user about it does not exist enough costume.
                pass
        else:
            # TODO: Return error mesage about user has no permission
            pass


class PurchaseMutation(graphene.ObjectType):
    """
    Purchase Mutation
    """
    purchase = CreatePurchase.Field()


class Query(graphene.AbstractType):
    """
    Abstract Query for Purchase Model
    """
    purchase = graphene.Field(PurchaseType, id=graphene.Int())

    def resolve_purchase(self, info, *args, **kwargs):
        if info.context.user.is_authenticated():
            return Purchase.objects.filter(user=info.context.user)
        return None
