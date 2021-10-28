semana=['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo' ]

print('Tamanho:', len(semana))
print('repetiçoes:', semana.count('primeiro'))
print('Lista:',semana)

print('Fracionando 1: até fim', semana[1:])
print('Fracionando :5 até começo', semana[:5])
print('Fracionando 0:3', semana[0:3])


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


# unsando IN
# SE 'Sexta' está na lista semana
if 'Sexta' in semana:
    print("Sim, ", 'Sexta'," está na lista")
else:
    print("Não está")
    

#usando NOT IN
# SE 'Domingo' não está na lista semana
if 'Domingo' not in semana:
    print("Não, ", 'Domingo'," não está na lista")
else:
    print("Está na lista")
