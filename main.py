from assets import ASSETS
from services.price import Price


def main():
    price = Price()
    price.get_assets_to_buy(ASSETS)


if __name__ == '__main__':
    main()
