# Avaliação sobre conhecimento em Pythom em Curso Livre/IFES
#Função geradora:
def contador(max): #Ao escolher o valor max, eu estabeleço até que número eu quero criar em uma sequencia de números; 
    n = 5 #Ao escolher o valor de n, eu defino a partir de qual número essa sequencia será criada;
    while n <= max: #Aqui eu estabeleço o limite ou fim da sequencia criada, n menor ou igual ao valor max;
        yield n #O yield faz com que a função se torne um gerador;
        n += 5 #O valor n vai aumentar duas unidades(ou outro valor escolhido) enquanto while não chegar ao valor max;
# Usando o gerador
for numero in contador(25): #Aqui eu escolhi o valor max como 11;
    print(numero) #A sequencia aparecerá no terminal;
