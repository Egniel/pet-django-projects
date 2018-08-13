from django.shortcuts import render

# Create your views here.
BASE_API_URL = 'https://www.alphavantage.co/query?'
API_KEY = '1HSO32YSXNYE4S6F'

function = 'DIGITAL_CURRENCY_INTRADAY'
symbol = 'BTC'
market = 'ETH'
interval = '60min'
query_example = (  # make as params
    f'function={function}&symbol={symbol}&market={market}&apikey={API_KEY}'
    f'&interval={interval}'
)



