import graphene
from graphene_django import DjangoObjectType


from .models import URL


class URLType(DjangoObjectType):
    class Meta:
        model = URL


class Query(graphene.ObjectType):
    """"Создает список типа URLType, resolve_urls возвращает все URL'ы из базы данных"""
    """Creating a list with type URLType, resolve_urls return all URL's from database"""
    urls = graphene.List(URLType)

    def resolve_urls(self, info,):
        return URL.objects.all()


class URLCreator(graphene.Mutation):
    """Возвращает содержимое url после мутации(запроса)"""
    """Returns url after mutation"""
    url = graphene.Field(URLType)

    class Arguments:
        full_url = graphene.String()

    def mutate(self, info, full_url):
        url = URL(full_url=full_url)
        url.save()

        return URLCreator(url=url)

class Mutation(graphene.ObjectType):
    """хранит все мутации"""
    create_url = URLCreator.Field()
