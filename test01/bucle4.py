# Uso de continue
# Esta instruccion se salta a la sigueinte 
# vuelta del ciclo cuando la instruccion es alcanzada
# Output 0,1,2,3,5,6,8,9

limite = 10
#limite = 19

for index in range(limite) : 
    if index == 7 :
        continue
    print(index)

### Uso del else en el for 
# se ejecuta cuando el ciclo termian correctamente.
for index in range(limite) : 
    if index == 15 :
        break
    print(index)
else:
    print('Else ejecutado')
print('Flujo normal')


