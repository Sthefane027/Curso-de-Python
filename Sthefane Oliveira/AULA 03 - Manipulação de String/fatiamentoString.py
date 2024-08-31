texto= "curso de python"

setima_posicao_texto= texto[6]
print (setima_posicao_texto)

texto_curso= texto [0:5]
print(texto_curso)

texto_python = texto[9:]

#Conta o número de caracteres dentro do texto

qtdChar= len(texto)
print (f"na frase {texto} temos {qtdChar} caracteres")

#Contar um número especifico de letras em um texto

qtd_letras_o = texto.count ("o")
print (f" na frase {texto} temos {qtd_letras_o} letras o")

#Identifica a posição onde inicia uma palavra 

palavra = "python"

posicao_palavra = texto.find(palavra)
print (f" a palavra {palavra} inicia na posição {posicao_palavra}")

#Identifica se existe a palavra no texto. 
palavra= "python"
verifica_palavra = palavra in texto
print(f"A palavra {palavra} esta no texto? {verifica_palavra}")
 