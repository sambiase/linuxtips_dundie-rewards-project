from subprocess import check_output
import pytest
@pytest.mark.integration
@pytest.mark.medium
def test_load():
    res = check_output(['dundie', 'load', '../tests/assets/people.csv']).decode('utf-8').split('\n')
    assert len(res) == 2
