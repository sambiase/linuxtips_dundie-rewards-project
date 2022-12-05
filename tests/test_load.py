from dundie.core import load
from .constants import PEOPLE_FILE
import pytest

@pytest.mark.unit
@pytest.mark.high
def test_length_load():
    assert len(load(PEOPLE_FILE)) == 2

@pytest.mark.unit
def test_item_load():
    assert load(PEOPLE_FILE)[0][0] == 'A'
