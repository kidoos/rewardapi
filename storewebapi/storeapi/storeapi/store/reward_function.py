# -*- coding: utf-8 -*-
""" Name : reward_function.py.py.
    Author : Nirav 
"""


def reward_point(data):
    if data['Purchase Amount'] > 50 and data['Purchase Amount'] <= 100:
        return data['Purchase Amount'] - 50
    elif data['Purchase Amount'] > 100:
        return (data['Purchase Amount'] - 100) * 2 + 50
    else:
        return 0
