import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING

class TestIngredient:

    def test_get_ingredient_price(self, ingredient):
        assert ingredient.get_price() == 100

    def test_get_ingredient_name(self, ingredient):
        assert ingredient.get_name() == "сыр"

    def test_get_ingredient_type(self, ingredient):
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
