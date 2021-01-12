from sum import mysum
import pytest


@pytest.mark.parametrize('numbers, output', [
    ([1, 2, 3], 6),
    ([1, 2, 3, 4, 5], 15)
])
# Ajoutez un test pour que la somme des éléments de la liste soit égale à 10
def test_mysum(numbers, output):
    assert mysum(numbers) == output
    assert (len(numbers) % 2) == 1
