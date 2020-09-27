import graphene
from graphene_django import DjangoObjectType

from .models import URL


class URLType(DjangoObjectType):
    class Meta:
        model = URL


class Query(graphene.ObjectType):
    """"Создает список типа URLType, resolve_urls возвращает все URL'ы из базы данных"""
    urls = graphene.List(URLType)

    def resolve_urls(self, info, **kwargs):
        return URL.objects.all()


class CreateURL(graphene.Mutation):
    """Возвращает содержимое url после мутации(запроса)"""
    url = graphene.Field(URLType)

    class Arguments:
        full_url = graphene.String()

    def mutate(self, info, full_url):
        url = URL(full_url=full_url)
        url.save()


class Mutation(graphene.ObjectType):
    """хранит все мутации"""
    create_url = CreateURL.Field()
