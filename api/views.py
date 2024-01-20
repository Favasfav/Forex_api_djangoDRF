from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import environ
from api.forex_api.api_forex import api_call

from dotenv import load_dotenv

# loads the configs from .env
load_dotenv()
import os

# here we are filternig the query_params and set to defined urls, passing the url to function api_call() for getting data from alphavantage
class CurrencyExchange(APIView):
    def get(self, request, *args, **kwargs):
        function_type = request.query_params.get("function", "")
        symbol_from = request.query_params.get("from_symbol", "")
        symbol_to = request.query_params.get("to_symbol", "")
        interval = request.query_params.get("interval", "")

        api_key = str(os.getenv("apikey"))

        if function_type and symbol_from and symbol_to and interval:
            url = f"https://www.alphavantage.co/query?function={function_type}&from_symbol={symbol_from}&to_symbol={symbol_to}&interval={interval}&apikey={api_key}"
            return api_call(url)
        elif function_type and symbol_from and symbol_to:
            print("hhhhhhhhh")
            url = f"https://www.alphavantage.co/query?function={function_type}&from_symbol={symbol_from}&to_symbol={symbol_to}&apikey={api_key}"
            return api_call(url)
        else:
            # we can call any set url to get default api like ?function=FX_MONTHL&from_symbol=EUR&to_symbol=USD i provided here
            # if url dont have sufficient params then giving default url shownig FX_DAILY,EUR,USD as params
            url = "https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey=demo&apikey={api_key}"
            return api_call(url)

