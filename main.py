from assets import ASSETS
from services.price import Price
from settings.base import LOGGER


def main():
    LOGGER.info('Starting allaum assets to buy')
    price = Price()
    price.get_assets_to_buy(ASSETS)


if __name__ == '__main__':
    main()
