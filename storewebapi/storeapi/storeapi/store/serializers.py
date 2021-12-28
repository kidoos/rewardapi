# -*- coding: utf-8 -*-
""" Name : serializers.py.py. 
    Author : Nirav 
"""

from rest_framework import serializers
from .models import *


class TransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionDetail
        fields = '__all__'
