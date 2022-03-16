import json

from pycoingecko import CoinGeckoAPI


class MarketService:
    def __init__(self):
        self.coingecko = CoinGeckoAPI()
        self.coingecko.request_timeout = 15
        self.currency = 'usd'

    def get_market_info(self, coin_id):
        data = self.coingecko.get_coins_markets(vs_currency=self.currency, ids=[coin_id])
        price = data[0]['current_price'] if data else 0
        market_cap = data[0]['market_cap'] if data else 0
        trading_volume = data[0]['total_volume'] if data else 0
        return {
            'price': price,
            'market_cap': market_cap,
            'trading_volume': trading_volume
        }

    def get_history_market_info(self, coin_id, days=30):
        data = self.coingecko.get_coin_market_chart_by_id(coin_id, self.currency, days=days)
        result = {}
        for key, logs in data.items():
            change_logs = {}
            for x in logs:
                t = int(x[0] / 1000)
                change_logs[t] = x[1]
            result[key] = change_logs
        return result


if __name__ == '__main__':
    market_service = MarketService()
    market_info = market_service.get_market_info('trava-finance')
    history_market_info = market_service.get_history_market_info('trava-finance')

    print(market_info)
    with open('../../data/history_market_info.json', 'w') as f:
        json.dump(history_market_info, f)
