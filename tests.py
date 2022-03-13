import pytest
import api


@pytest.fixture(name='Авторизация', scope='function', )
def auth():
    api.authotization()
    yield


def test_auth():
    assert api.authotization() == 200


@pytest.mark.usefixtures('Авторизация')
def test_en_ru():
    assert api.translate_en_ru('dog') == 'собака'


@pytest.mark.usefixtures('Авторизация')
def test_ru_en():
    assert api.translate_ru_en('собака') == 'dog'
