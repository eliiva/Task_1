import pytest
from data import buns_list, ingredients_list

class TestDatabase:

    @pytest.mark.parametrize('index, name, price', buns_list)
    def test_get_available_buns(self, index, name, price, database):
        database_buns = database.available_buns()

        assert database_buns[index].get_name() == name
        assert database_buns[index].get_price() == price

    @pytest.mark.parametrize('index, type, name, price', ingredients_list)
    def test_get_available_ingredients(self, index, type, name, price, database):
        database_ingredients = database.available_ingredients()

        assert database_ingredients[index].get_name() == name
        assert database_ingredients[index].get_price() == price
        assert database_ingredients[index].get_type() == type
