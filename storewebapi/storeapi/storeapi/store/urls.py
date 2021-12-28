# -*- coding: utf-8 -*-
""" Name : urls.py.py. 
    Author : Nirav 
"""


from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('rewardDetailApi',views.Transaction.as_view())

urlpatterns = [
    path('', include(router.urls)),
    path('rewardapi/',views.Transaction.as_view())

]
