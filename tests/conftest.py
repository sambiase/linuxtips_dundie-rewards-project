MARKER = """\
unit: Marker unit tests
high: High Priority 
medium: Medium Priority 
low: Low Priority 
"""


# funcao que faz com que possamos rodar os marcadores via CLI: pytest -s -v -m "medium"
def pytest_configure(config):
    for line in MARKER.split('\n'):
        config.addinivalue_line('markers', line)
