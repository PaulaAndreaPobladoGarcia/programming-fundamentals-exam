medidasTriangulo = float(input("ingrese la medida de su cuadro equilatero: "))
lado = medidasTriangulo * medidasTriangulo
r = 1.73
area = lado * r / 4
totalArea = area

if totalArea > 1000:
    print(f"Datos no validos")

else:
    print(f"el area de su rectangulo es {totalArea}")
