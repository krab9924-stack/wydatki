import pytest
from wydatki.bledy import BladAnalizatora, BladDanych

def test_blad_danych_jest_bladem_analizatora():
    with pytest.raises(BladAnalizatora):
        raise BladDanych("Zła kwota w wierszu 3")