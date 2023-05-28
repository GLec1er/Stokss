import random
import requests
import hashlib
from datetime import datetime

# константы для подключения к API Binance
API_KEY = 'ваш API-ключ'
SECRET_KEY = 'ваш секретный ключ'
BASE_URL = 'https://api.binance.com'
HEADERS = {'Content-Type': 'application/x-www-form-urlencoded',
           'X-MBX-APIKEY': API_KEY}


# метод для создания ордеров
def create_orders(volume, number, amountDif, side, priceMin, priceMax):
    total_volume = volume
    for i in range(number):
        # вычисляем объём ордера с учётом разброса amountDif
        order_volume = round(random.uniform(volume / number - amountDif, volume / number + amountDif), 2)
        # вычисляем цену ордера с учётом диапазона цен
        order_price = round(random.uniform(priceMin, priceMax), 6)
        # оставшийся объём после создания ордера
        volume -= order_volume
        # параметры запроса
        params = {
            'symbol': 'BTCUSDT',  # торговая пара
            'side': side,  # сторона торговли
            'type': 'LIMIT',  # тип ордера
            'timeInForce': 'GTC',  # время действия ордера
            'quantity': order_volume,  # объём ордера
            'price': order_price,  # цена ордера
            'timestamp': int(datetime.timestamp(datetime.now()) * 1000)  # метка времени
        }

        # формируем подпись запроса
        query_string = f"symbol={params['symbol']}&side={params['side']}&type={params['type']}&" \
                       f"timeInForce={params['timeInForce']}&quantity={params['quantity']}&price={params['price']}" \
                       f"&timestamp={params['timestamp']}"
        signature = hashlib.sha256((query_string + SECRET_KEY).encode('utf-8')).hexdigest()
        # параметры запроса с подписью
        params['signature'] = signature
        # отправляем запрос на создание ордера
        response = requests.post(f"{BASE_URL}/api/v3/order", headers=HEADERS, params=params)
        if response.status_code == 200:
            # выводим результат создания ордера
            print(f"Ордер создан: #{i + 1}, объём {order_volume}, цена {order_price}")
        else:
            # выводим описание ошибки
            print(f"Ошибка создания ордера: {response.json()['msg']}")
    if volume != 0:
        # если остался неиспользованный объем, выводим предупреждение
        print(f"Неиспользованный объём: {volume}")
    else:
        print("Все ордера созданы")

    # пример использования функции
    orders_data = {
        "volume": 10000.0,
        "number": 5,
        "amountDif": 50.0,
        "side": "SELL",
        "priceMin": 200.0,
        "priceMax": 300.0
    }
    create_orders(**orders_data)
    
