from operadores import soma, sub
from pytest import approx
import pytest


def test_soma():
    teste_soma = soma(5, 6.2)
    assert teste_soma == approx(11.2)


def test_sub():
    assert sub(10, 5) == approx(4)


pytest.main(["-v", "--tb=line", "-rN", __file__])
