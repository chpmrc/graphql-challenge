import graphene

from graphene_django.types import DjangoObjectType

from celebrityshop.honey.models import Celebrity, Costume


class CostumeType(DjangoObjectType):
    """
    Costume Type
    """
    class Meta:
        model = Costume


class CelebrityType(DjangoObjectType):
    """
    Celebrity Type.
    """
    class Meta:
        model = Celebrity


class Query(graphene.AbstractType):
    """
    Abstract Query for Costume and Celebrity Models
    """
    costume = graphene.Field(CostumeType,
                             id=graphene.Int(),
                             name=graphene.String())
    all_costumes = graphene.List(CostumeType)
    celebrity = graphene.Field(CelebrityType,
                               id=graphene.Int(),
                               name=graphene.String())
    all_celebrities = graphene.List(CelebrityType)

    def resolve_all_costumes(self, info, *args, **kwargs):
        if info.context.user.is_authenticated():
            return Costume.objects.all()
        else:
            return Costume.objects.filter(visibility=Costume.VISIBILITY_PUBLIC_CHOICE[0])

    def resolve_all_celebrities(self, *args, **kwargs):
        return Celebrity.objects.all()

    def resolve_costume(self, info, *args, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            obj = Costume.objects.get(pk=id)
            if obj.visibility == Costume.VISIBILITY_PUBLIC_CHOICE[0]:
                return obj
            elif obj.visibility == Costume.VISIBILITY_PRIVATE_CHOICE[0] and \
                    info.context.user.is_authenticated():
                return obj
            else:
                return None

        if name is not None:
            obj = Costume.objects.get(name=name)
            if obj.visibility == Costume.VISIBILITY_PUBLIC_CHOICE[0]:
                return obj
            elif obj.visibility == Costume.VISIBILITY_PRIVATE_CHOICE[0] and \
                    info.context.user.is_authenticated():
                return obj
            else:
                return None

    def resolve_celebrity(self, *args, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Celebrity.objects.get(pk=id)

        if name is not None:
            return Celebrity.objects.filter(name__icontains=name)

        return None
