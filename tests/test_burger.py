import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from bun import Bun
from data import receipt

class TestBurger:

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)

        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self, burger):
        ingredient0 = Ingredient(INGREDIENT_TYPE_FILLING, "айсберг", 150)
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, "индейка", 150)
        burger.add_ingredient(ingredient0)
        burger.add_ingredient(ingredient1)

        burger.remove_ingredient(0)

        assert burger.ingredients[0] == ingredient1

    def test_move_ingredient(self, burger):
        ingredient0 = Ingredient(INGREDIENT_TYPE_FILLING, "айсберг", 150)
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, "индейка", 150)
        ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "песто", 200)

        burger.add_ingredient(ingredient0)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(2,0)

        assert burger.ingredients[0] == ingredient2

    def test_get_burger_price(self, burger):
        bun = Bun("пшеничная", 100)
        ingredient0 = Ingredient(INGREDIENT_TYPE_FILLING, "айсберг", 150)
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, "индейка", 150)
        ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "песто", 200)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient0)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
    
        assert burger.get_price() == 700

    def test_get_burger_receipt(self, burger):
        bun = Bun("пшеничная", 100)
        ingredient0 = Ingredient(INGREDIENT_TYPE_FILLING, "айсберг", 150)
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, "индейка", 150)
        ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "песто", 200)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient0)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
    
        assert burger.get_receipt() == receipt
