tabela_morse = {
    ".": "E",
    "-": "T",
    ".-": "A",
    "..": "I",
    "--": "M",
    "-.": "N",
    "-..": "D",
    "--.": "G",
    "-.-": "K",
    "---": "O",
    ".-.": "R",
    "...": "S",
    "..-": "U",
    ".--": "W",
    "-...": "B",
    "-.-.": "C",
    "..-.": "F",
    "....": "H",
    ".---": "J",
    ".-..": "L",
    ".--.": "P",
    "--.-": "Q",
    "...-": "V",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z"
}

with open("potenciais_frases.txt", "w") as frases:
    with open("possibilidades_plausiveis.txt") as possibilidades:
        # Carrega a mensagem
        mensagem = possibilidades.readline()

        while True:
            # Carrega as possibilidades
            possibilidade = eval(possibilidades.readline())
            if possibilidade == []:
                print("Todas as possibilidades traduzidas!")
                break

            posicao_espaco = 0
            frase = ""
            frase_possivel = True
            for espaco in possibilidade:
                # Aplica os espacos e converte a mensagem para o alfabeto
                try:
                    frase += tabela_morse[mensagem[posicao_espaco : posicao_espaco + espaco]]
                except KeyError:
                    frase_possivel = False
                    break

                
                # Ignora a frase se ela tiver 3 letras iguais consecutivas
                if len(frase) > 2 and frase[len(frase) - 3 : ].count(frase[len(frase) - 1]) == 3:
                    frase_possivel = False
                elif len(frase) > 3:
                    # Ignora a frase se ela tiver 4 consoantes consecutivas
                    frase_possivel = False
                    for letra in frase[len(frase) - 4 : ]:
                        if letra in ["A", "E", "I", "O", "U"]:
                            frase_possivel = True
                            break
                    
                    if frase_possivel and len(frase) > 4:
                        # Ignora a frase se ela tiver 5 vogais consecutivas
                        frase_possivel = False
                        for letra in frase[len(frase) - 5 : ]:
                            if letra not in ["A", "E", "I", "O", "U"]:
                                frase_possivel = True
                                break
                

                if not frase_possivel:
                    #print(frase)
                    break

                posicao_espaco += espaco

            # Anota a frase se ela for possivel
            if frase_possivel:
                try:
                    frase += tabela_morse[mensagem[posicao_espaco : len(mensagem) - 1]]
                except:
                    pass

                # Ignora se tiver 3 letras consecutivas
                if not (len(frase) > 2 and frase[len(frase) - 3 : ].count(frase[len(frase) - 1]) == 3):
                    # Ignora se tiver 3 consoantes consecutivas ou 3 vogais consecutivas
                    if len(frase) > 2:
                        cont_vogais = 0
                        for letra in frase[len(frase) - 3 : ]:
                            if letra in ["A", "E", "I", "O", "U"]:
                                cont_vogais += 1
                        
                        if 0 < cont_vogais < 3:
                            frases.write(f"{frase}\n")
                    else:
                        frases.write(f"{frase}\n")