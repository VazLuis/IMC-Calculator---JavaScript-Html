def definir_opcao():
    opcao = input("Deseja Criptografar (c) ou Descriptografar (d) ? ")
    if opcao == "c":
        criptografar()
    else:
        descriptografar()
            

def criptografar():
    msg = input("digite sua mensagem: ")
    criptografado = ""
    chave = int(input("Digite o valor da chave (1 - 93): "))
    aux = 0
    while chave <= 0 and chave >= 27:
        chave = int(input("Digite o valor da chave (2-25) "))

    for letra in msg:
        num = ord(letra)
        num = num + chave
        if num > ord("~"):
            num = num - 94
        elif num < ord(" "):
            num = num + 94

        criptografado += chr(num)

    print(criptografado)
    arq = open("arquivo.txt", "w")
    arq.write(criptografado)
    arq.close()


def descriptografar():
    arq = open("arquivo.txt", "r")
    msg = str(arq.read())
    arq.close()

    chave = int(input("Digite o valor da chave: "))

    descriptografado = ""

    for letra in msg:
        num = ord(letra)
        num = num - chave
        if num > ord("~"):
            num = num - 94
        elif num < ord(" "):
            num = num + 94

        descriptografado += chr(num)

    print(descriptografado)
    arq = open("arquivod.txt", "w")
    arq.write(descriptografado)
    arq.close()


definir_opcao()
