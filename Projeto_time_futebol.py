def verificar(nome, Time):
    for x in Time:
        for y in Time[x]:
            if y[2].lower() == nome:
                return True
    return False

#troca

def valdiarParametros(jogador, Time):
    aux = Time[jogador[1]]
    nome = jogador[0].lower()
    for x in aux:
        if x[2].lower() == nome and x[0] == jogador[2]:
            return False
    return True

def validandoJogadorAtual(jogador, Time):
    if not verificar(jogador[0].lower(), Time):
        return True
    elif jogador[1] not in Time.keys():
        return True
    elif valdiarParametros(jogador, Time):
        return True
    else:
        return False


def removeJogador(aux, atual):
    for x in aux:
        if x[2].lower() == atual[0].lower():
            a = x
    aux.remove(a)
    return aux

def apresentarPossicao(jogadores, esquema):
    if(esquema == 2):
        return ('|{:^20}{:^20}|\n'.format(jogadores[0][2], jogadores[1][2]))
    if(esquema == 3):
        return ("|{:^13}{:^13}{:^13} |\n".format(jogadores[0][2], jogadores[1][2],jogadores[2][2]))
    if(esquema == 4):
        return ("|{:^10}{:^10}{:^10}{:^10}|\n".format(jogadores[0][2], jogadores[1][2],jogadores[2][2], jogadores[3][2]))
    
def pontinhos(esquema):
    if(esquema == 2):
        return (f"|{' ' * 9}o{' ' * 19}o{' ' * 10}|\n")
    if(esquema == 3):
        return (f"|{' ' * 5}o{' ' * 12}o{' ' * 12}o{' ' * 8}|\n")
    if(esquema == 4):
        return(f"|{' ' * 4}o{' ' * 9}o{' ' * 9}o{' ' * 9}o{' ' * 5}|\n")

def ApresenteTime(Time, Formacao):
    padrao = "|                                        |\n"
    campo = ""
    campo +="+----------------------------------------+\n"
    campo +="|              |          |              |\n"
    campo +="|               ----------               |\n"
    campo += padrao
    campo += apresentarPossicao(Time["atacante"], Formacao[2])
    campo += pontinhos(Formacao[2])
    campo += padrao
    campo += apresentarPossicao(Time["meia"], Formacao[1])
    campo += pontinhos(Formacao[1])
    campo += "|                  (  )                  |\n"
    campo += padrao
    campo += padrao
    campo += apresentarPossicao(Time["defensor"], Formacao[0])
    campo += pontinhos(Formacao[0])
    campo += padrao
    campo += "|               ----o-----               |\n"
    campo += ("|              |{:^10}|              |\n".format(Time["goleiro"] [0][2]))
    campo +="+----------------------------------------+"
    return campo



def validandoFormacao(aux):
    validas = [2,3,4]
    ans = 0
    for x in aux:
        ans += x
        if x not in validas:
            print("Cada posição deve conter entre 2 e 4 jogadores")
            return False

    if ans != 10:
        print("A soma das posições deve totalizar 10 jogadores")
        return False
    else:
        return True
    


#main
HabilidadesValidas = [0,1,2,3,4,5,6,7,8,9,10]
Time = {'goleiro': [], 'defensor': [], 'meia': [], 'atacante': []}
formacao = []
contador = 0
while True:
    escolha = int(input())
    if escolha == 1:
        jogador = input().split(" ")
        jogador[0] = jogador[0][:8]
        jogador[2] = int(jogador[2])
        if verificar(jogador[0].lower(), Time):
            print("Jogador já está no time")
        elif jogador[1] not in Time.keys():
            print('A posição informada não existe' )
        elif jogador[2] not in HabilidadesValidas:
            print("A habilidade do jogador deve estar entre 0 e 10")
        else:
            aux = (jogador[2], contador+1, jogador[0])
            ans = Time[jogador[1]]
            ans.append(aux)
            Time[jogador[1]] = sorted(ans, key=lambda x: (-x[0], x[1]))
            contador += 1
    if escolha == 2:
        jogadores =  input().split(" x ")
        atual, subs = jogadores[0], jogadores[1]
        atual = atual.split(" ")
        subs = subs.split(" ")
        atual[0] = atual[0][:8]
        atual[2] = int(atual[2])
        subs[0] = subs[0][:8]
        subs[2] = int(subs[2])
        if validandoJogadorAtual(atual, Time):
            print("Jogador não está no time ")
        elif verificar(subs[0].lower(), Time):
            print("Jogador já está no time")
        elif subs[1] not in Time.keys():
            print('A posição informada não existe' )
        elif subs[2] not in HabilidadesValidas:
            print("A habilidade do jogador deve estar entre 0 e 10")
        else:
            aux = (subs[2], contador+1, subs[0])
            ans = Time[subs[1]]
            ans.append(aux)
            Time[subs[1]] = sorted(ans, key=lambda x: (-x[0], x[1]))
            Time[atual[1]] = removeJogador(Time[atual[1]], atual)
            contador += 1
    if escolha == 3:
        aux =[int (x) for x in input().split(" ")]
        if validandoFormacao(aux):
            formacao = aux
    if escolha == 4:
        if len(formacao) == 0:
            print("O Esquema tático deve ser estabelecido antes de montar o time")
        else:
            primeira = True
            padrao  = "Estão faltando jogadores no time:"
            if len(Time["goleiro"]) < 1:
                if primeira:
                    print(padrao)
                    primeira = False
                print("1 goleiro")
            if len(Time["defensor"]) < formacao[0]:
                aux = formacao[0] - len(Time["defensor"])
                if primeira:
                    print(padrao)
                    primeira = False
                print(f"{aux} defensores")
            if len(Time["meia"]) < formacao[1]:
                aux = formacao[1] - len(Time["meia"])
                if primeira:
                    print(padrao)
                    primeira = False
                print(f"{aux} meias")
            if len(Time["atacante"]) < formacao[2]:
                aux = formacao[1] - len(Time["atacante"])
                if primeira:
                    print(padrao)
                    primeira = False
                print(f"{aux} atacantes")
            if primeira:
                print(ApresenteTime(Time, formacao))
    if escolha == 5:
       break