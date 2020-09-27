from django.contrib import admin
from django.urls import path

from django.views.decorators.csrf import csrf_exempt  # allows client to pass the csrf token
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
