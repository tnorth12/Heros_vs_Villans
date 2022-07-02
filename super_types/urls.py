from django.urls import path
from . import views
# import super_types

urlpatterns = [
    path('', views.supertypes_list),
    # path('<int:pk>/', views.supertypes_detail)

]