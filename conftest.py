import pytest
from helpers import register_new_courier, delete_courier


@pytest.fixture(scope='function')
def courier():
    credentials = register_new_courier()
    yield credentials
    delete_courier(credentials)
