from binance.client import Client

api_key = 'your-api-key'
api_secret = 'your-api-secret'

client = Client(api_key, api_secret)


import random
from binance.enums import *
from binance.exceptions import *

def create_orders(data):
    # Извлечение данных из словаря
    volume = data['volume']
    number = data['number']
    amountDif = data['amountDif']
    side = data['side']
    priceMin = data['priceMin']
    priceMax = data['priceMax']

    # Разбиение объема на равные части
    amount = volume / number

    orders = []
    for i in range(number):
        # Вычисляем цену внутри диапазона
        price = round(random.uniform(priceMin, priceMax), 2)

        # Вычисляем разброс объема
        amountDelta = round(random.uniform(-amountDif, amountDif), 2)

        # Вычисляем объем
        amountFinal = round(amount + amountDelta, 2)

        # Создаем ордер
        try:
            order = client.create_test_order(
                symbol='ETHUSDT',
                side=side,
                type=ORDER_TYPE_LIMIT,
                price=str(price),
                quantity=str(amountFinal))
                
            orders.append(order)
     except BinanceAPIException as e:
        print(f'Binance API error: {e}')
    except BinanceOrderException as e:
        print(f'Binance order error: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')

    return orders

        
def create_orders(data):
    # Извлечение данных из словаря
    volume = data['volume']
    number = data['number']
    amountDif = data['amountDif']
    side = data['side']
    priceMin = data['priceMin']
    priceMax = data['priceMax']

    # Разбиение объема на равные части
    amount = volume / number

    orders = []
    try:
        for i in range(number):
            # Вычисляем цену внутри диапазона
            price = round(random.uniform(priceMin, priceMax), 2)

            # Вычисляем разброс объема
            amountDelta = round(random.uniform(-amountDif, amountDif), 2)

            # Вычисляем объем
            amountFinal = round(amount + amountDelta, 2)

            # Создаем ордер
            order = client.create_test_order(
                symbol='ETHUSDT',
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                price=str(price),
                quantity=str(amountFinal))

            orders.append(order)
            
    except BinanceAPIException as e:
        print(f'Binance API error: {e}')
    except BinanceOrderException as e:
        print(f'Binance order error: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')

    return orders
