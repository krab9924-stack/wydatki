class BladAnalizatora(Exception):
    """Bazowy wyjątek aplikacji."""

class BladFormatu(BladAnalizatora):
    """Brak kolumn lub uszkodzony plik."""

class BladDanych(BladAnalizatora):
    """Niepoprawna data lub kwota w wierszu."""