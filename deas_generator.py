import csv
import random
import time


tiempo_inicio = time.time()

with open('marcas_deas.csv', newline='') as csvfile:

    reader = csv.reader(csvfile)

    marcas = [row[0] for row in reader]

modelos = []

for i in range(9):

    with open(f'modelos_{i}.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        actual = []
        for row in reader:
            actual.append(row[0])
        modelos.append(actual)

dias_por_mes = {
    1: 31, 
    2: 28,  
    3: 31,  
    4: 30,  
    5: 31,  
    6: 30, 
    7: 31,  
    8: 31,  
    9: 30, 
    10: 31,
    11: 30,
    12: 31
}

nombres = [
    "Planta baja",
    "Piso 1",
    "Piso 2",
    "Piso 3",
    "Piso 4",
    "Piso 5",

]

with open('deas.csv', mode="w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    true_or_false = [True, False]

    for i in range(1000000):

        dea = []
        marca_id = (random.randint(0, 8))
        numero_serie = random.randint(0, 10**11 - 1)
        ano = random.randint(2000, 2022)
        mes = random.randint(1, 12)
        dia = random.randint(1, dias_por_mes[mes])
        ult_mantenimiento =f'{ano}-{mes}-{dia}'


        dea.append(random.choice(nombres))
        dea.append(marcas[marca_id])
        dea.append(modelos[marca_id][random.randint(0, 4)])
        dea.append(f'{numero_serie:011d}')
        dea.append(random.choice(true_or_false))
        dea.append(random.choice(true_or_false))
        dea.append(ult_mantenimiento)

        writer.writerow(dea)


tiempo_fin = time.time()

print(tiempo_fin - tiempo_inicio)