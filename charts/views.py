from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()


#### 16:50


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 123, 325, 431, 134, 144]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)
