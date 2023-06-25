import concurrent.futures

from connections.screening import Screening
from settings.base import LOGGER


class Price:
    def __init__(self) -> None:
        self.connection = Screening.create()

    async def get_assets_to_buy(self, assets: list):
        """
        Look to assets daily variation and if it's below 0,
        returns the asset to buy.

        In future will be more user friendly.
        """
        LOGGER.info("Getting assets to buy")
        assets_to_buy = {}
        futures = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            for asset in assets:
                futures.append(
                    executor.submit(self.connection.get_daily_volatility, asset=asset)
                )

            for future in concurrent.futures.as_completed(futures):
                asset, value = future.result()
                if value > 0:
                    LOGGER.debug(f"Asset {asset} stonks, discarding from list")
                    continue
                LOGGER.debug(f"Asset {asset} not stonks, oportunity to buy for less")
                assets_to_buy[asset] = value

        if not assets_to_buy:
            LOGGER.info("Not today young man, not today...")

        LOGGER.info(assets_to_buy)
