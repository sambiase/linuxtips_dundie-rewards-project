from dundie.core import load
from contants import PEOPLE_FILE


def test_load():
    assert load(PEOPLE_FILE)[0][0] == 'J'