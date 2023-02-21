from abc import ABC, abstractmethod

from settings.base import DEFAULT_SCREENING


class Screening(ABC):

    @staticmethod
    def create():
        path = DEFAULT_SCREENING.split('.')
        module_path = '.'.join(path[:-1])
        module = __import__(module_path)
        return getattr(module, path[-1])()

    @abstractmethod
    def get_daily_volatility(self, asset: str):
        pass
