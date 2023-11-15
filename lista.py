l1 = ['uva', 'morango', 'banana', 'abacaxi', 'pera']; # criação da lista 1
l2 = ['tomate', 'abobora', 'batata', 'pipino', 'cebola']; # criação da lista 2

l3 = l1+l2; # estou juntando a lista 1 e a lista 2
print(f'lista 1 {l1}');
print('-------------------------------------------------------------');
print(f'lista 2 {l2}');
print('-------------------------------------------------------------');
print(f'Junção da lista 1 com a 2 {l3}');
print('-------------------------------------------------------------');

l1.append('nova frunta') # adiciona elementos a lista '
print(f'lista 1 com nova vruta{l1}');
print('-------------------------------------------------------------');
l1.remove('banana')
print(f'lista 1 com a remoção de banana {l1}')
print('-------------------------------------------------------------');
del(l1) #apaga a lista inteira 

for i in l3: # estou percorrendo a listad 3 que é a junção da l1 com l2     
    print(i)