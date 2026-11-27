from datetime import date

def calcular_edad(fecha_nacimiento, hoy=None):
    """Devuelve la edad en años cumplidos a la fecha 'hoy'."""
    if hoy is None:
        hoy = date.today()
    if fecha_nacimiento > hoy:
        raise ValueError("La fecha de nacimeinto no puede estar en el futuro")

    edad = hoy.year - fecha_nacimiento.year
    # Si aún no ha cumplido años este año, se resta uno
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    return edad