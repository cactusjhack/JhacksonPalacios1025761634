from datetime import date
import pytest
from edad import calcular_edad, es_mayor_de_edad

HOY = date(2026, 11, 26) # fecha fija para que el test nunca cambie

def test_ya_cumplio_anos():
    assert calcular_edad(date(2005, 3, 10), HOY) == 21

def test_aun_no_cumple_anos():
    assert calcular_edad(date(2005, 12, 25), HOY) == 20

def test_cumple_hoy():
    assert calcular_edad(date(2000, 11, 26), HOY) == 26

def test_nacido_29_febrero():
    assert calcular_edad(date(2000, 2, 29), date(2023, 2, 28)) == 22
    assert calcular_edad(date(2000, 2, 29), date(2023, 3, 1)) == 23

def test_fecha_futura():
    with pytest.raises(ValueError):
        calcular_edad(date(2030, 1, 1), HOY)

def test_mayor_de_edad():
    assert es_mayor_de_edad(date(2000, 1, 1), HOY) is True
    assert es_mayor_de_edad(date(2015, 1, 1), HOY) is False