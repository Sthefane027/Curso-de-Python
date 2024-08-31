#TROCANDO UMA PALAVRA DENTRO DO TEXTO

texto="STHEFANE OLIVEIRA"
troca_palavra= texto.replace("OLIVEIRA","Santos")
print (troca_palavra)


#DEIXANDO TODOS OS CARACTERES EM MAIÚSCULO

texto="SthEFaNe@GMail.Br"
print(texto.upper())


#DEIXANDO TODOS OS CARACTERES EM MINÚSCULO 

texto_minusculo= texto.lower()
print (texto_minusculo)


#DEIXANDO A PRIMEIRA LETRA DE CADA PALAVRA EM MAIÚSCULO

texto= "Meu segundo curso no senai"
texto_title= texto.title()
print(texto_title)

#DEIXANDO A PRIMEIRA LETRA DO TEXTO PALAVRA EM MAIÚSCULO

texto_capitalize= texto.capitalize()
print (texto_capitalize)


#ELIMINA ESPAÇOS INÚTEIS

texto= "      SENAI   "
print(f'A palavra {texti} tem {len(texto)} caracteres')
texto_strip= texto.strip()

print(f'A palavra {texto_strip} tem {len(texto_strip)} caracteres')

