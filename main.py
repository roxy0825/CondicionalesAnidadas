#1. Hacer un algoritmo que lea el nombre de una persona, el número de horas que
#estudia en la semana y muestre el porcentaje de tiempo que dedica a estudiar y la
#cantidad de minutos que dedica a estudiar.

("""nombre=input("Ingrese nombre: ")
horas_semana=float(input("Ingreses las horas estudiadas en la semana: "))

porcentaje_tiempo= horas_semana * 168 / 100
can_minutos= horas_semana * 60

print(nombre + " el porcentaje de tiempo que dedicas al estudio es: " + str(porcentaje_tiempo)+
      " y la cantidad de minutos estuadiados en la semana es de "+ str(can_minutos))
print("-"*60)""")

#2. Hacer un algoritmo que lea el nombre de un animal, la comida preferida, el número
#de porciones que come al día, el valor de la porción y muestre el nombre del animal
#y el costo de alimentarlo en el día.

("""nombre=input("Ingrese nombre: ")
comida=input("Ingrese comida: ")
com_preferida=input("Ingrese comida preferida: ")
porciones=int(input("Ingrese el numero de porciones: "))
valor_porcion=float(input("Ingrese valor de la porcion: "))

costo=porciones*valor_porcion
print("-"*60)
print("Mi mascosa se llama "+str(nombre))
print("El costo de su alimentacion a la semana es de "+ str(costo))
print("-"*60)""")

#3. Escribir un algoritmo donde el usuario pueda ingresar el nombre y la edad de una
#persona y el computador le muestre el nombre y un mensaje que diga si la persona
#es mayor o menor de edad.


("""nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese edad:"))

if edad >= 18:
    print(nombre + " eres mayor de edad")
else:
    print(nombre+" eres menor de edad")
print("-"*60)""")

#4. Se debe crear un algoritmo que imprima el nombre del estudiante, el valor de la
#matrícula, el valor del descuento, el valor del recargo y el valor neto a pagar
#sabiendo que se debe regir por la siguiente tabla:
#ESTRATO DESCUENTO RECARGO
#   1       40%      0%
#   2       30%      0%
#   3       10%      0%
#   4       0%       10%
#   5       0%       20%
#   6       0%       40%

("""nombre_estudiante = input("Ingrese el nombre del estudiante: ")
valor_matricula = float(input("Ingrese el valor de la matrícula: "))
estrato = int(input("Ingrese el estrato del estudiante: "))

descuento = 0
recargo = 0

if estrato == 1:
    descuento = 0.4
elif estrato == 2:
    descuento = 0.3
elif estrato == 3:
    descuento = 0.1
elif estrato == 4:
    recargo = 0.1
elif estrato == 5:
    recargo = 0.2
elif estrato == 6:
    recargo = 0.4

valor_descuento = valor_matricula * descuento
valor_recargo = valor_matricula * recargo
valor_neto = valor_matricula - valor_descuento + valor_recargo

print("Nombre del estudiante: ", nombre_estudiante)
print("Valor de la matrícula: ", valor_matricula)
print("Valor del descuento: ", valor_descuento)
print("Valor del recargo: ", valor_recargo)
print("Valor neto a pagar: ", valor_neto)
print("-"*60)""")

#5. Un administrador de vehículos necesita un programa donde pueda ingresar los datos
#de un vehículo así: Placa, el tipo (1= bus, 2= buseta, 3= colectivo, 4= Automóvil) y el
#número de pasajeros transportados. Elabore un algoritmo que muestre la placa, el
#dinero recolectado y el pago para el conductor que es el 20 % del total recolectado.
#También tenga en cuenta que el precio del pasaje en Bus es de $2200.oo, en Buseta
#es de $ 2500.oo, en Colectivos es de $3500.oo. y en automóvil a $5500.oo

("""placa = input("Ingrese la placa del vehículo: ")
tipo = int(input("Ingrese el tipo de vehículo (1=bus, 2=buseta, 3=colectivo, 4=automóvil): "))

while tipo < 1 or tipo > 4:
    print("Tipo de vehículo inválido. Ingrese un valor válido.")
    tipo = int(input("Ingrese el tipo de vehículo (1=bus, 2=buseta, 3=colectivo, 4=automóvil): "))

num_pasajeros = int(input("Ingrese el número de pasajeros transportados: "))


if tipo == 1:
    precio_pasaje = 2200
elif tipo == 2:
    precio_pasaje = 2500
elif tipo == 3:
    precio_pasaje = 3500
else:
    precio_pasaje = 5500

dinero_recolectado = precio_pasaje * num_pasajeros
pago_conductor = dinero_recolectado * 0.2
print("-"*60)
print("Placa del vehículo:", placa)
print("Dinero recolectado:", dinero_recolectado)
print("Pago para el conductor:", pago_conductor)
print("-"*60)""")

#6.Realizar un algoritmo que lea dos números cualquiera e imprima cual es el mayor o
#imprimir si los números son iguales.

("""numero1=int(input("Ingrese primer numero: "))
numero2=int(input("Ingrese segundo numero: "))

if numero1 > numero2:
    print("El numero mayor es el primero: " + str(numero1))
elif numero1 == numero2:
    print("Los numero son iguales")
else:
    print("El numero mayor es el segundo: " + str(numero2))
print("-"*60)""")

#7. El precio normal de un pantalón es de 60.000 pesos, pero debido a una
#promoción, si se compran 12 a más, se hará un descuento del 20% sobre el precio
#total, pero si se compran más de 6 pero menos de 12, sólo el 10%, de lo contrario,
#no hay descuento. Generar un programa que, dada la cantidad de pantalones, me
#diga cuanto ganaré de descuento y cuál sería el precio final a pagar.

("""cantidad_pantalones=int(input("Ingrese cantidad de pantalones: "))

precio_total=60.000
descuento = 0
tiene_descuento = False

if cantidad_pantalones >= 12:
    descuento= 0.2
    tiene_descuento = True
elif cantidad_pantalones > 6:
    descuento= 0.1
    tiene_descuento = True

precio_total = precio_total * cantidad_pantalones
valor_descuento = precio_total * descuento
precio_final = precio_total - valor_descuento

if tiene_descuento:
    print(f"El valor del descuento es de {valor_descuento:,} pesos")
else:
    print("No hay descuento")

print(f"El precio final a pagar es de {precio_final:,} pesos")
print("-"*60)""")

#8. Construir un programa que calcule el índice de masa corporal de una persona ( IMC
#=peso [kg] / altura2 [m]) e imprima el estado del DIAGNOSTICO en el que se
#encuentra esa persona en función del valor de IMC
("""peso=float(input("Ingrese su peso: "))
altura=float(input("Ingrese su altura: "))

imc= peso / (altura ** 2)

if imc < 16:
    print("Su masa corporal es " + str(imc) + " Criterio de ingreso en hospital")
elif imc >= 16 and imc <= 17:
    print("Su masa corporal es " + str(imc) + " Infrapeso")
elif imc >= 17 and imc <= 18:
    print("Su masa corporal es " + str(imc) + " Bajo peso")
elif imc >= 18 and imc <= 25:
    print("Su masa corporal es " + str(imc) + " Peso normal (saludable)")
elif imc >= 25 and imc <= 30:
    print("Su masa corporal es " + str(imc) + " Sobrepeso (Obesidad de grado I)")
elif imc >= 30 and imc <= 35:
    print("Su masa corporal es " + str(imc) + " Sobrepeso cronico (Obesidad de grado II)")
elif imc >= 35 and imc <= 40:
    print("Su masa corporal es " + str(imc) + " Obesidad premorbida (Obesidad de grado III)")
else:
    print("Su masa corporal es " + str(imc) + " Obesidad morbida (obesidad de grado IV)")
print("-"*60)""")

#9. Un supermercado ha puesto en oferta la venta al por mayor de cierto producto,
#ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso
#contrario. Además, por la compra de más de 3 docenas se obsequia una unidad del
#producto por cada docena en exceso sobre 3. Diseñe un algoritmo que determine el
#monto de la compra, el monto del descuento, el monto a pagar y el número de
#unidades de obsequio por la compra de cierta cantidad de docenas del producto.

("""cantidad_docenas = int(input("Ingrese la cantidad de docenas compradas: "))
precio_unitario = 10000  # si no hay precio unitario no es posible calcular

if cantidad_docenas > 3:
    descuento = 0.15
    unidades_obsequio = cantidad_docenas - 3
else:
    descuento = 0.1
    unidades_obsequio = 0

precio_total = cantidad_docenas * precio_unitario * (1 - descuento)
monto_descuento = precio_total * descuento
monto_a_pagar = precio_total - monto_descuento

print(f"Monto de la compra: {precio_total:,} pesos")
print(f"Monto del descuento: {monto_descuento:,} pesos")
print(f"Monto a pagar: {monto_a_pagar:,} pesos")
print(f"Unidades de obsequio: {unidades_obsequio}")
print("-"*60)""")


#10.Una compañía dedicada al alquiler de automoviles cobra un monto fijo de $300000
#para los primeros 300 km de recorrido. Para más de 300 km y hasta 1000 km, cobra
#un monto adicional de $ 15.000 por cada kilómetro en exceso sobre 300. Para más
#de 1000 km cobra un monto adicional de $ 10.000 por cada kilómetro en exceso
#sobre 1000. Los precios ya incluyen el 20% del impuesto general a las ventas, IVA.
#Diseñe un algoritmo que determine el monto a pagar por el alquiler de un vehículo y
#el monto incluido del impuesto.

("""km=int(input("Ingrese kilometros recorridos: "))

if km <= 300:
    costo_total = 300000
elif km > 300 and km <= 1000:
    km_adicionales = km - 300
    costo_total = 300000 + (km_adicionales * 15000)
else:
    km_adicionales_1 = 700
    km_adicionales_2 = km - 1000
    costo_total = 300000 + (km_adicionales_1 * 15000) + (km_adicionales_2 * 10000)

impuesto = costo_total * 0.2
costo_final = costo_total + impuesto

print("El costo total del alquiler es de $", costo_total)
print("El impuesto (IVA) incluido es de $", impuesto)
print("El costo final del alquiler es de $", costo_final)
print("-"*60)""")

#11.Realizar un algoritmo que solicite el nombre, el estrato, la edad, la escolaridad, el
#género, el Sisbén. Dependiendo de las siguientes condiciones que imprima si tiene
#derecho o no una beca.
#Estrato 2
#edad >=16
#escolaridad 10
#genero Femenino


("""nombre=input("Ingrese nombre: ")
estrato=int(input("ingrese estrato: "))
edad=int(input("Ingrese su edad: "))
escolaridad=int(input("Ingrese escolaridad (1-11): "))
genero=input("Ingrese genero (Masculino/Femenino): ")
sisben=input("Ingrese su puntaje de sisben: ")

if estrato == 2 and edad >= 16 and escolaridad == 10 and genero.lower() == "femenino":
    print("Felicidades, " + nombre + ", tiene derecho a una beca.")
else:
    print("Lo siento, " + nombre + ", no tiene derecho a una beca.")
print("-"*60)""")

#12.Realizar un algoritmo que lea el nombre de un empleado, su salario, el número de
#meses trabajados, el numero de hijos y el estrato. El empleado recibirá unas
#bonificaciones dependiendo del siguiente cuadro

#Bonificacion 1  2,8% del salario mes si tiene mayor o igual a 3 hijos, sino cero
#Bonificacion 2  4,0% del salario mes si el numero de meses es mayor de 10 de lo contrario 1,5%
#Bonificacion 3  8,0% del salario mes si el estrato es mayor de 4, sino el 15%

#Tener en cuenta que el empleado puede recibir una  o varias bonificaciones.
#Imprimir el nombre el salario, el número de meses trabajados, el número de hijos y el
#estrato, el valor de cada bonificación y el total a pagar (salario + bonificaciones).


("""def calcular_bonificaciones(salario, meses_trabajados, num_hijos, estrato):
    bonificaciones = {}
    bonificaciones["Bonificación 1"] = salario * 0.028 if num_hijos >= 3 else 0
    bonificaciones["Bonificación 2"] = salario * 0.04 if meses_trabajados > 10 else salario * 0.015
    bonificaciones["Bonificación 3"] = salario * 0.08 if estrato > 4 else salario * 0.15
    return bonificaciones

# Lectura de datos del empleado
nombre = input("Ingrese el nombre del empleado: ")
salario = float(input("Ingrese el salario del empleado: "))
meses_trabajados = int(input("Ingrese el número de meses trabajados: "))
num_hijos = int(input("Ingrese el número de hijos: "))
estrato = int(input("Ingrese el estrato: "))

# Cálculo de las bonificaciones
bonificaciones = calcular_bonificaciones(salario, meses_trabajados, num_hijos, estrato)

# Cálculo del total a pagar
total_a_pagar = salario + sum(bonificaciones.values())

# Impresión de resultados
print("Nombre:", nombre)
print("Salario: $", salario)
print("Meses trabajados:", meses_trabajados)
print("Número de hijos:", num_hijos)
print("Estrato:", estrato)
for bonificacion, valor in bonificaciones.items():
    print(bonificacion + ": $", valor)
print("Total a pagar: $", total_a_pagar)
print("-"*60)""")

#13. La Institución educativa CESDE, se encuentra realizando un descuento para el curso
#de Desarrollo de Software, para lo cual se desean los siguientes datos.
# Nombre, edad, si es o no estudiante, si tiene afiliación a la Caja de Compensación Familiar Comfama.
# Para acceder a la beca debe cumplir los siguientes requisitos.
#a. Si la persona es menor de Edad, Estudia y Afilado a Comfama, Valor Boleta : GRATIS.
#b. Si la persona es menor de Edad, No Estudia y Afilado a Comfama, Valor beca: $ 400.000.
#c. 3. Si la persona es mayor de Edad y Afilado a Comfama, Valor Beca : $300.000.
#d. En cualquier otro caso Valor beca: $ 50.000.
#Imprima el nombre y el valor de la beca

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
es_estudiante = input("¿Es estudiante? (S/N): ").lower() == "s"
afiliacion_comfama = input("¿Tiene afiliación a Comfama? (S/N): ").lower() == "s"

if edad < 18 and es_estudiante and afiliacion_comfama:
    valor_beca = 0
elif edad < 18 and not es_estudiante and afiliacion_comfama:
    valor_beca = 400000
elif afiliacion_comfama:
    valor_beca = 300000
else:
    valor_beca = 50000

print(f"Nombre: {nombre}")
print(f"Valor de la beca: ${valor_beca}")




















