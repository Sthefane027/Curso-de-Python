#DESAFIO 01 

nome= input("Digite seu nome:")
nome_maicuslo= nome.upper()
print (f'Meu nome maiúsculo é {nome_maicuslo}')

nomeMinusculos= nome.lower()
print (f'Meu nome minusculoSthefane é {nomeMinusculos}')

troca_palavra= nome.replace(" ","")
print(f'Meu nome juntado é {troca_palavra}')

split=nome.split()
primeiroNome= split[0]
print (f'O primeiro {nome} tem {len(primeiroNome)} caracteres')




#DESAFIO 02
palvra= "Santo"
cidade=input("Digite o nome da cidade:")
verifica_palavra = palvra in cidade
print (f'A Palavra {palvra} está no texto ?{verifica_palavra}')



#DESAFIO 03 

palavra= "Silva"
nome=input("Digite o nome de uma pessoa:")
verifica_palavra = palvra in nome
print (f'A Palavra {palvra} está no Nome ?{verifica_palavra}')



#DESAFIO 04

frase= input("Digite uma frase:")
qtdLetras=frase.count("a")
print (f"Na frase {frase} temos {qtdLetras} A")












