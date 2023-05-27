import unittest

class TestCreateOrders(unittest.TestCase):
    def setUp(self):
        # Инициализация клиента Binance API
        self.client = BinanceClient(api_key='your_api_key', api_secret='your_api_secret')

    def test_create_orders(self):
        data = {
            "volume": 10000.0,
            "number": 5,
            "amountDif": 50.0,
            "side": "SELL",
            "priceMin": 200.0,
            "priceMax": 300.0
        }

        orders = create_orders(data)
        self.assertEqual(len(orders), data['number'])

    def test_invalid_data(self):
        # Проверяем обработку ошибок, если данные неверны
        data = {
            "volume": -10000.0,
            "number": 5,
            "amountDif": 50.0,
            "side": "SELL",
            "priceMin": 200.0,
            "priceMax": 300.0
        }

        orders = create_orders(data)
        self.assertEqual(len(orders), 0)
