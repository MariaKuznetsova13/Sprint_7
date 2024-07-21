import pytest
from helpers import register_new_courier, delete_courier


@pytest.fixture(scope='function')
def courier():
    try:
        credentials = register_new_courier()
        yield credentials
    finally:
        delete_courier(credentials)
