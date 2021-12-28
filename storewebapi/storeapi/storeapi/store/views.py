# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
import pandas as pd
import json
from rest_framework.response import Response


def reward_point(data):
    if data['Purchase Amount'] > 50 and data['Purchase Amount'] <= 100:
        return data['Purchase Amount'] - 50
    elif data['Purchase Amount'] > 100:
        return (data['Purchase Amount'] - 100) * 2 + 50
    else:
        return 0


class Transaction(APIView):

    def get(self, request):
        field_value  = request.data.get("field_value")
        if field_value:
            data = pd.read_csv('store\\testdata\\customer_transcation_data.txt')

            data['Reward Points'] = data.apply(lambda data: reward_point(data), axis=1)
            data = data.sort_values(field_value)
            response_data = json.dumps(json.loads(data.to_json(orient="records")))
            return Response(data=response_data)
        else:
            data = pd.read_csv('store\\testdata\\customer_transcation_data.txt')

            data['Reward Points'] = data.apply(lambda data: reward_point(data), axis=1)
            response_data = json.dumps(json.loads(data.to_json(orient="records")))
            return Response(data=response_data)



        # customer_name = request.data.get("customer_name")
        # purchase_amount = request.data.get("puchase_amount")

        # if customer_id and customer_name and purchase_amount:
