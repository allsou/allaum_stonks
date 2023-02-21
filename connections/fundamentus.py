uimport pandas as pd
import requests

from settings.base import LOGGER

from .screening import Screening


class Fundamentus(Screening):
    base_url = 'http://fundamentus.com.br'
    headers = {
        'User-agent':
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
            'Accept': 'text/html, text/plain, text/css, text/sgml, */*;q=0.01',
            'Accept-Encoding': 'gzip, deflate'
    }

    def get_daily_volatility(self, asset: str):
        LOGGER.info(f'Getting asset {asset} daily variantion')
        url = f'{self.base_url}/detalhes.php?papel={asset}'

        response = requests.get(url, headers=self.headers)
        LOGGER.debug(f'Request status code: {response.status_code}')
        tables_html = pd.read_html(response.text, decimal=",", thousands='.')
        return asset, self.__parse_percent_to_float(tables_html[2][1][1])

    def __parse_percent_to_float(self, value: str) -> float:
        value = value.replace('%', '')
        return float(value.replace(',', '.'))
