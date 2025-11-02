import pandas as pd

# Crear un DataFrame con las calificaciones
calificaciones = pd.DataFrame({'Estudiante': ['A', 'B', 'C'], 'Calificación': [85, 90, 78]})

# Calcular la calificación promedio
promedio = calificaciones['Calificación'].mean()
print("La calificación promedio es:", promedio)
