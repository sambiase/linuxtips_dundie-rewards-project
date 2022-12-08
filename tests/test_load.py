import uuid
from dundie.core import load
from .constants import PEOPLE_FILE
import pytest


@pytest.mark.unit
@pytest.mark.high
def test_load():
    with open(f'arquivo_indesejado {uuid.uuid4()}', 'w') as file_:
        file_.write('dados uteis somente para os testes')

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'A'
