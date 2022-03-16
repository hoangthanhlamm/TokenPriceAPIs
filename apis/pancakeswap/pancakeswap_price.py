import time

import requests

from utils.logger_utils import get_logger

logger = get_logger('PancakeSwap API')

base_url = 'https://api.pancakeswap.info/api/v2/tokens/'


def get_price(token_address):
    start_time = time.time()
    url = base_url + token_address
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise requests.RequestException()

        data = response.json()
    except Exception as ex:
        logger.exception(ex)
        return

    price = float(data['data']['price'])
    updated_at = int(data['updated_at'] / 1000)
    logger.info(data)
    logger.info(f'Time exe: {round(time.time() - start_time, 3)}s')
    return {'price': price, 'updated_at': updated_at}


if __name__ == '__main__':
    info = get_price('0x21d5Fa5ECf2605c0E835Ae054AF9bbA0468e5951')
    print(info)
