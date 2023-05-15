def ler(texto):
   lido=texto.read()
   return lido

with open('BreakMyStride.txt', 'r') as arquivo:


    resp=input(f'''o que deseja fazer?
    1- Ler o arquivo
    2- Mostrar o arquivo
    3- Fechar o programa''')
    if resp =="1":
            ler(arquivo)
    elif resp == "2":
             aux=ler(arquivo)
             print(aux)
    elif resp == "3":
        loop=False

