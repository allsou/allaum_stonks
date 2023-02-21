import asyncio
import time

from assets import ASSETS
from services.price import Price
from settings.base import LOGGER


def main():
    start_at = time.time()
    LOGGER.info('Starting allaum assets to buy')
    price = Price()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(
        price.get_assets_to_buy(ASSETS)
    )
    LOGGER.info(f'Took {time.time() - start_at}')


if __name__ == '__main__':
    main()
