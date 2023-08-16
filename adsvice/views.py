from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

# Replace with your actual Facebook access token
ACCESS_TOKEN = 'your_access_token_here'

@api_view(['GET'])
def get_metrics(request):
    try:
        ad_account_id = request.query_params.get('ad_account_id')
        metrics = ['cpa', 'ctr', 'cpc']  # Add more metrics as needed

        params = {
            'access_token': ACCESS_TOKEN,
            'fields': ','.join(metrics)
        }

        response = requests.get(f'https://graph.facebook.com/v14.0/{ad_account_id}', params=params)
        data = response.json()

        # Process the data and extract metrics
        cpa = data.get('cpa', 0)
        ctr = data.get('ctr', 0)
        cpc = data.get('cpc', 0)

        result = {
            'cpa': cpa,
            'ctr': ctr,
            'cpc': cpc
        }

        return Response(result, status=200)

    except Exception as e:
        return Response({'error': str(e)}, status=500)
