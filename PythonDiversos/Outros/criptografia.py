alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l',
         'm','n','o','p','q','r','s','t','u','v','w','x',
         'y','z']

frase = input(str("Frase para criptografia: "))
def trocaVogal(palavra,vogal,numero):
  palavra = palavra.replace(vogal,numero)
  return palavra
  
def criptografaVogais(alfabeto,palavra):
  criptografada=palavra
  for i in range(0,len(alfabeto)):
    criptografada=trocaVogal(criptografada,alfabeto[i],str(i+1)+"'")    
  return criptografada
  
print(criptografaVogais(alfabeto,frase))
