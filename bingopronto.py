import numpy
c1 = 0
c2 = 0
c3 = 0
a = 1
pedrasSorteadasHex = numpy.chararray(144, itemsize=2, unicode=True)
pedrasSorteadas = numpy.zeros(144, dtype = int)
contaPedra = 0

# Criação de cartela com verificação inserida:
def criarCartela():
    vetor = numpy.zeros(16, dtype = int)
    a = 1
    vetor[0] = numpy.random.randint(16, 160)
    while a != 16:
        flag = True
        termo = numpy.random.randint(16, 160)
        if termo in vetor:
            flag = False
        if flag:
            vetor[a] = termo
            a += 1

    return vetor

def sortearPedra():
    sorteiaPedra = numpy.random.randint(16, 160, dtype = int)
    return sorteiaPedra

def exibirCartelaHex(vetorDecimal):
    d = numpy.chararray(16, itemsize=2, unicode=True)
    for r in range (16):
        d[r] = converteIntHex(vetorDecimal[r])
    matriz = numpy.reshape(d, (4, 4))
    return matriz

def converteIntHex(n):
    inteiro = (n // 16)
    x = (n % 16)
    if (x == 10):
        x = "A"
    if (x == 11):
        x = "B"
    if (x == 12):
        x = "C"
    if (x == 13):
        x = "D"
    if (x == 14):
        x = "E"
    if (x == 15):
        x = "F"
    return (str(inteiro) + str(x))

def conferirPedra(sortearPedra):
    pedra = sortearPedra
    if pedra in sortearPedra:
        sortearPedra()
        
def pontuacao(pedraSorteada, cartela, c):
    if pedraSorteada in cartela:
        return True
    else:
        return False
    
def exibirpontuacao(c):
    print(f'O jogador tem {c} pontos')

# Exibir Vencedor/Premiação
def calculaPremio(cartela1, cartela2, cartela3, contaPedra, c1, c2, c3):
    if c1 == 16:
        print(f'{nome1} venceu!')
        premio = 100 + max(cartela1) - contaPedra
        print(f'A premiação é de R${premio},00')
    if c2 == 16:
        print(f'{nome2} venceu!')
        premio = 100 + max(cartela2) - contaPedra
        print(f'A premiação é de R${premio},00')
    if c3 == 16:
        print(f'{nome3} venceu!')
        premio = 100 + max(cartela3) - contaPedra
        print(f'A premiação é de R${premio},00')

print("Bingo Nerd!!!")
nome1 = input(str("Digite o nome do primeiro jogador: "))
nome2 = input(str("Digite o nome do segundo jogador: "))
nome3 = input(str("Digite o nome do terceiro jogador: "))
print(" ")
print("Opção 1: Criar/Exibir cartela")
print("Opção 2: Sortear/Exibir pedra")
print("Opção 3: Exibir pedras sorteadas")
print("Opção 4: Exibir pontuação")
print("Opção 0: Sair do programa")

while True:
    cartela1 = (criarCartela())
    cartela2 = (criarCartela())
    cartela3 = (criarCartela())
    if c1 == 16 or c2 == 16 or c3 == 16:
        calculaPremio(cartela1, cartela2, cartela3, contaPedra, c1, c2, c3)
        break
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            break
        except:
            print("Digite uma opção válida!")
    if opcao == 0:
        print("Você saiu do bingo!")
        break
    elif (opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4):
        print("Você escolheu uma opção inválida! Escolha outra opção.")
    elif (opcao == 1):
        print("As 3 cartelas são:")
        cartela1 = (criarCartela())
        cartela2 = (criarCartela())
        cartela3 = (criarCartela())
        print(nome1 + ":")
        print(exibirCartelaHex(cartela1))
        print(" ")
        print(nome2 + ":")
        print(exibirCartelaHex(cartela2))
        print(" ")
        print(nome3 + ":")
        print(exibirCartelaHex(cartela3))
    elif (opcao == 2):
        while True:
            pedra = (sortearPedra())
            if pedra not in pedrasSorteadas:
                pedrasSorteadas[contaPedra] = pedra
                pedrasSorteadasHex[contaPedra] = converteIntHex(pedra)
                print (converteIntHex(pedra))
                contaPedra += 1
                if pontuacao(pedra, cartela1, c1):
                    c1 += 1
                if pontuacao(pedra, cartela2, c2):
                    c2 += 1
                if pontuacao(pedra, cartela3, c3):
                    c3 += 1
                break
            
    elif (opcao == 3):
        print(sorted(pedrasSorteadas))
    elif (opcao == 4):
        print(f'Pontuação de {nome1}:')
        exibirpontuacao(c1)
        print(f'Pontuação de {nome2}:')
        exibirpontuacao(c2)
        print(f'Pontuação de {nome3}:')
        exibirpontuacao(c3)