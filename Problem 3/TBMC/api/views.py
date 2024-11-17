from django.http import JsonResponse
from django.views import View
import requests
from requests.exceptions import RequestException
import random, string

# Create your views here.

class TransactionClient:
    BROADCAST_URL = "https://mock-node-wgqbnxruha-as.a.run.app/broadcast"
    CHECK_URL = "https://mock-node-wgqbnxruha-as.a.run.app/check/{}"

class PostPayloadView(View) :   
    def get(self, request) :
        try:
            symbol = "".join(random.choices(string.ascii_uppercase, k=3))
            price = random.randrange(1,100001)
            timestamp = random.randrange(1000000000,10000000000)

            jsonPayload = {
                'symbol': symbol,
                'price': price,
                'timestamp': timestamp
            }

            print(jsonPayload)
            
            response = requests.post(TransactionClient.BROADCAST_URL, json=jsonPayload)
            response.raise_for_status()
            print(response.json()["tx_hash"])
            
            return JsonResponse(response.json())
            
        except RequestException as e:
            return JsonResponse({'error': str(e)})
    
class GetTransactionView(View) :
    def get(self, request, tx_hash):
        try:
            if not tx_hash:
                return JsonResponse({'error': 'Transaction hash required'}, status=400)

            response = requests.get(TransactionClient.CHECK_URL.format(tx_hash))
            response.raise_for_status()

            print(response.json())

            return JsonResponse(response.json())
            
        except RequestException as e:
            return JsonResponse({'error': str(e)})