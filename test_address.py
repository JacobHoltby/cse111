from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("236 W 3rd S, Rexburg, ID 83440") == "Rexburg"
    
def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("236 W 3rd S, Rexburg, ID 83440") == "ID"

def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("236 W 3rd S, Rexburg, ID 83440") == "83440"

pytest.main(["-v", "--tb=line", "-rN", __file__])