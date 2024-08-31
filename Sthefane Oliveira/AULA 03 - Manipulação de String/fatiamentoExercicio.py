#Quantidade de Caractertes:

nome= "Sthefane dos santos de oliveira"

qtdCaracteres= len(nome)
print (f"O Nome {nome} tem {qtdCaracteres} caracteres")



#Quantidade de Letras A:

qtd_Letras = nome.count ("a")
print (f" No nome {nome} temos {qtd_Letras} letras a")

#Onde inicia seu ultimo nome:

texto= "oliveira"
ultimo_nome= nome.find(texto)
print (f" O nome {texto} inicia na posição {ultimo_nome}")


#Verifica se você tem os seguintes sobrenome:

texto1= "Silva"
verifica= texto1 in nome
print(f"O nome {texto1} está no texto? {verifica}")

texto1= "Souza"
verifica= texto1 in nome
print(f"O nome {texto1} está no texto? {verifica}")

texto1= "santos"
verifica= texto1 in nome
print(f"O nome {texto1} está no texto? {verifica}")