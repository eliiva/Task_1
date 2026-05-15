from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

buns_list = [
    [0, "black bun", 100],
    [1, "white bun", 200],
    [2, "red bun", 300]
]

ingredients_list = [
    [0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
    [1, INGREDIENT_TYPE_SAUCE, "sour cream", 200],
    [2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
    [3, INGREDIENT_TYPE_FILLING, "cutlet", 100],
    [4, INGREDIENT_TYPE_FILLING, "dinosaur", 200],
    [5, INGREDIENT_TYPE_FILLING, "sausage", 300]
]

receipt = (
    "(==== пшеничная ====)\n"
    "= filling айсберг =\n"
    "= filling индейка =\n"
    "= sauce песто =\n"
    "(==== пшеничная ====)\n"
    "\n"
    "Price: 700"
)
