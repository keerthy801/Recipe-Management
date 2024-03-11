"""
URL configuration for recipemanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views as rviews  #Module import aliasing

from  recipemanagementapp.views import (
    RecipeListCreateView,RecipeRetrieveUpdateDeleteView,RecipeSearchView,
    CreateUser,user_logout,ReviewCreateView,ReviewListView,)
from django.contrib import admin
from recipemanagementapp import views

router = SimpleRouter()
router.register('user', views.CreateUser)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', rviews.obtain_auth_token, name='api-token-auth'),
    path('logout/', user_logout.as_view(), name='logout'),
    path('recipe/', RecipeListCreateView.as_view(), name='create-review'),
    path('recipe/<int:pk>/', RecipeRetrieveUpdateDeleteView.as_view(), name='recipe-details'),
    path('recipe/search/', RecipeSearchView.as_view(), name='search-review'),
    path('recipe/<int:recipe_id>/reviews/', ReviewListView.as_view(), name='list-review'),
    path('recipe/<int:recipe_id>/reviews/create/', ReviewCreateView.as_view(), name='create-review'),
]
