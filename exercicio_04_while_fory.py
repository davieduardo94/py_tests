# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
popA=int(input('Digite a populacao de A: '))
popB=int(input('Digite a populacao de B: '))
taxA=float(input('Digite a taxa de A: '))
taxB=float(input('Digite a taxa de B: '))
count = 0
if(taxA>taxB and popA<popB):
    while(popA<popB):
        popA= int(popA * (1+(taxA/100)))
        popB= int(popB * (1+(taxB/100)))
        print("Ano %d:" % count)
        print("Populaçao A: %d" % popA)
        print("População B: %d\n\n" % popB)
        count+=1
    print('\nAnos para ultrapassar a população de B:', count, 'anos')
else:
    print('A taxa de crescimento de A é menor que B,portanto nunca será possivel alcançar a mesma população.')