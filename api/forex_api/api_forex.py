# api/views.p

import requests
from rest_framework.response import Response
from rest_framework import status

# here we are calling the external api  
def api_call(url):
    try:
        r = requests.get(url)

        data = r.json()
        print(data)

        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"message": e}, status=status.HTTP_400_BAD_REQUEST)
