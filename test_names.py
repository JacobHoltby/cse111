from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_names():
    assert make_full_name("Ava", "Smith-Jones") == "Smith-Jones; Ava"
    assert make_full_name("Madison", "Reynolds") == "Reynolds; Madison"
    assert make_full_name("BJ", "P") == "P; BJ"
    assert make_full_name ("", "") == "; "

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Reynolds; Madison") == "Reynolds"
    assert extract_family_name("P; BJ") == "P"
    assert extract_family_name(" ; ") == " "

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Reynolds; Madison") == "Madison"
    assert extract_given_name("P; BJ") == "BJ"
    assert extract_given_name("; ") == ""
    

pytest.main(["-v", "--tb=line", "-rN", __file__])