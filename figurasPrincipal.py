import pandas as pd
from funciones import triangulo, rectangulo, circulo

dataFile = pd.read_csv("figuras.csv")

print("Procesando figuras ...\n")

areas = []
perimetros = []

for index, row in dataFile.iterrows():
   if row['FIGURA'] == 't':
      area = triangulo(int(row['MEDIDA1']), int(row['MEDIDA2']))
   elif row['FIGURA'] == 'r':
      area = rectangulo(int(row['MEDIDA1']), int(row['MEDIDA2']))
   elif row ['FIGURA'] == 'c':
      area = circulo(float(row['MEDIDA1']))
   print(f"Fila{index}: FIGURA={row['FIGURA']}, Medida1={row['MEDIDA1']}, Medida2={row['MEDIDA2']}, Area={area}")

