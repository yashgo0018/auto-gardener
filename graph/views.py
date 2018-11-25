import json
import sqlite3

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


"""
def home(request):
    context = {}
    return render(request, 'index.html', context)
"""
class get_data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        data = cur.execute('SELECT * FROM maindata').fetchall()
        conn.close()
        return Response(data)
