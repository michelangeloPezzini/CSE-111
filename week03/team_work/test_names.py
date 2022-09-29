from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("mike", "pezzini") == "PEZZINI;MIKE"
    assert make_full_name("Neymar", "Rodrigues") == "RODRIGUES;NEYMAR"
    assert make_full_name(
        "Charlote", "Stemmaguarda") == "STEMMAGUARDA;CHARLOTE"


def test_extract_family_name():
    assert extract_family_name("Pezzini; Mike") == "PEZZINI"
    assert extract_family_name("Smith; Joseph") == "SMITH"
    assert extract_family_name("Monson; Robert") == "MONSON"


def test_extract_given_name():
    assert extract_given_name("Cachapuz; Gabriela") == "GABRIELA"
    assert extract_given_name("Silva; Luana") == "LUANA"
    assert extract_given_name("Medeiros; Sarah") == "SARAH"


pytest.main(["-v", "--tb=line", "-rN", __file__])
