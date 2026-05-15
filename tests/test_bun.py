import pytest
from bun import Bun

class TestBun:

    def test_get_bun_name(self, bun):
        assert bun.get_name() == "Проверочная"

    def test_get_bun_price(self, bun):
        assert bun.get_price() == 150.99
