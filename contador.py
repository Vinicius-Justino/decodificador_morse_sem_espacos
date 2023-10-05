from math import ceil

# Recebe a frase
frase = input("Digite um morse sem espacos: ")

# Calcula e anota todas as possibilidades plausiveis de espacamento
with open("possibilidades_plausiveis.txt", "w") as possibilidades:
    # Escreve a frase no topo do arquivo para os proximos programas
    possibilidades.write(f"{frase}\n")
    
    arvore = [[len(frase)]]
    #cont = 0
    while True:
        galhos_novos = []

        # Cria as ramificacoes de cada galho
        while len(arvore) > 0:
            galho = arvore.pop(0)
            ponta = galho.pop(len(galho) - 1)

            # Anota e quebra o galho, se ja estiver pronto ou apenas quebra se estiver ficando muito longo
            if ponta == 0:
                if len(galho) > 1:
                    galho.pop(len(galho) - 1)

                possibilidades.write(f"{galho}\n")

                #cont += 1
                #print(cont)
                continue
            elif len(galho) == ceil(len(frase) / 2):
                continue
            elif (len(galho) > 4 and galho[len(galho) - 5 :] == [1, 1, 1, 1, 1]) or (len(galho) > 3 and galho[len(galho) - 4 : ] == [4, 4, 4, 4]):
                continue
            
            # Cria as 4 ramificacoes de cada galho
            for espaco in range(1, 5):
                potencial_galho = galho.copy()

                # Verifica se e possível dar o espacamento desejado
                if ponta - espaco >= 0:
                    potencial_galho.extend([espaco, ponta - espaco])

                    galhos_novos.append(potencial_galho.copy())
                else:
                    # Se nao e mais possivel dar espaço, vai para o proximo galho
                    break

        if galhos_novos != []:
            arvore = galhos_novos.copy()
        else:
            possibilidades.write("[]\n")
            print("Possibilidades registradas!")
            break
