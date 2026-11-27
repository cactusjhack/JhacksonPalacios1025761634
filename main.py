from datetime import datetime
from edad import calcular_edad

if __name__ == "__main__":
    texto = input("Fecha de nacimiento (AAAA-MM-DD): ")
    fecha = datetime.strptime(texto, "%Y-%m-%d").date()
    print(f"Tienes {calcular_edad(fecha)} años")