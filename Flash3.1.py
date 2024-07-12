#1 Lists --La lista va entre corchetes y cada elemento de la lista va entre comillas
vowels = ['e','i','o']

#1 con numeros se levanta un elemento de la lista.

print(vowels[0])
print(vowels[-1])
print(vowels[1])
print(vowels[0],vowels[-1],vowels[1])

#Los elementos de una lista van separados por una coma y cada elemetno va entre comillas simples


#2 append()-- agrega un elemento al final de la lista 
vowels.append('u')
print(vowels)

#3 insert() -- agrega un elemento a la lista pero se le agrega primero la ubicacion

#averiguar si append y insert son methods o que carajo son

vowels.insert(0,'a')

print(vowels)

vowels[-1] = 'y'

print(vowels)

