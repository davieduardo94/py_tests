# Exemplos de funçoes com listas em Pythob
semana=['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo' ]

print('Tamanho:', len(semana))
print('repetiçoes:', semana.count('primeiro'))
print('Lista:',semana)

semana.append('Folga')
print('Adicinar:', semana)

semana.insert(0,'Teste')
print('Insert:',semana)

semana.remove('Teste')
print('Remove:',semana)

semana.pop(7)
print('Pop:', semana)

semana.reverse()
print('Reverse:',semana)
