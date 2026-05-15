import pytest
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING
from database import Database
from burger import Burger

@pytest.fixture
def bun():
    return Bun("Проверочная", 150.99)

@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE_FILLING, "сыр", 100)

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def burger():
    return Burger()
