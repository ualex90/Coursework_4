import pytest

from src.api.headhunter_api import HeadHunterAPI
from src.api.superjob_api import SuperJobAPI


@pytest.fixture
def hh():
    return HeadHunterAPI()


@pytest.fixture
def sj():
    return SuperJobAPI()
