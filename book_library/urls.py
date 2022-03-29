from django.urls import path
from ariadne.contrib.django.views import GraphQLView
from .resolvers import schema
urlpatterns = [
    path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),
    path('', GraphQLView.as_view(schema=schema), name='graphql'),
]