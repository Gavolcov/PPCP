import os


# Declaração de variaveis, listas e matrizes
Aux: float
AD = 0
Aux_Entrega = 0
jobs = 0
Ocupacao = [0]*jobs
Duracao_Total = [0]*jobs
F = [0]*jobs, [0]*jobs
M = [0]*jobs, [0]*jobs
CJ = [0], [0]
Seq_Inicial = [0]*jobs
Atribuicao = [0]*jobs
Sol = [0]*jobs
Sol_Tarefa = [0]*jobs
Seq_Ini = [0]*jobs
Seq_Ini_Carga = [0]*jobs
Seq_Ini_Tarefa = [0]*jobs
Seq_Aux = [0]*jobs
Resultado_N = [0]*jobs
CN = [0]*jobs, [0]*jobs
Resultado_Parcial = [0]*jobs
i = j = machines = problema = n = maq = N = Resultado = 0
Seq_Inicial_Tarefa = [0]
Seq_Inicial_Maquina = [0]*jobs
Seq_Inicial_Duracao = [0]*jobs
Seq_Inicial_Tarefa = [0]*jobs

class p1:
    def __int__(self):

    # ******************************************************************************
    def Leitura_Regras():  # Leitura do problema.
        os.system('cls')
        print("\n******************************************************************************")
        print("\n*****************| APS EDUCACIONAL - GABRIEL VOLCOV |*************************\n")
        jobs = int(input("\tDigite o numero de tarefas a serem executadas: "))  # leitura do número de máquinas
        print("\n")
        # Definindo tamanho das listas conforme quantidade de tarefas
        TO = [0] * jobs
        TD = [0] * jobs
        TE = [0] * jobs
        Solucao = [0] * jobs
        Tarefas = [0] * jobs
        SF = [0] * jobs
        SA = [0] * jobs
        SD = [0] * jobs
        SE = [0] * jobs
        SO = [0] * jobs

        for i in range(jobs):  # Leitura da linha com as informações das durações
            TO[i] = i
            TD[i] = float(input(f"\tDigite a duracao da tarefa {i + 1}: "))
        print("\n")
        for i in range(jobs):  # Leitura da linha com as informações das durações
            TE[i] = float(input(f"\tDigite o prazo de entrega da tarefa {i + 1}: "))

    def Regras():
        SD = sorted(TD)

        for i in range(jobs):
            SO[i] = TD.index(SD[i])

        Solucao = sum(SD) / len(SD)

        F_MTP = Fluxo_Medio(jobs)
        A_MTP = Atraso_Medio(jobs)

        for i in range(jobs):
            SF[i] = SO[i]
            SA[i] = SD[i]

        Resultado_F = F_MTP
        Metodo_F = "Menor Tempo de Processamento"
        Resultado_A = A_MTP
        Metodo_A = "Menor Tempo de Processamento"

        # Resolvendo os problemas pelo Método Menor Folga
        Menor_Folga(jobs)
        F_MF = Fluxo_Medio(jobs)
        A_MF = Atraso_Medio(jobs)

        if (F_MF < Resultado_F):
            Resultado_F = F_MF
            Metodo_F = "Menor Folga"
            for i in range(jobs):
                SF[i] = Solucao[i]

        if (A_MF < Resultado_A):
            Resultado_A = A_MF
            Metodo_A = "Menor Folga"
            for i in range(jobs):
                SA[i] = Solucao[i]

        for i in range(jobs):
            Solucao[i] = Tarefas[i]

        # Resolvendo os Problemas pelo método da Razão Crítica
        Razao_Critica(jobs)
        F_RC = Fluxo_Medio(jobs)
        A_RC = Atraso_Medio(jobs)

        if (F_RC < Resultado_F):
            Resultado_F = F_RC
            Metodo_F = "Razao Critica"
            for i in range(jobs):
                SF[i] = Solucao[i]

        if (A_RC < Resultado_A):
            Resultado_A = A_RC
            Metodo_A = "Razao Critica"
            for i in range(jobs):
                SA[i] = Solucao[i]

        os.system('cls')
        print("\n******************************************************************************")
        print("*****************| APS EDUCACIONAL - GABRIEL VOLCOV |*************************\n")
        print("\tO APS executa as regras de atribuicao:\n")
        print("\tMenor tempo de processamento (SPT)\n")
        print("\tMenor folga\n\tRazao critica.\n\n")
        print("\tE avalia conforme os criterios:\n\tMenor tempo de processamento\n\tMenor atraso\n")
        # Mostrando o resultado na tela para o Fluxo Médio
        print(f"\tO Menor Fluxo Medio foi {Resultado_F} e o Metodo: ", Metodo_F)
        print("\n\tSolucao do problema de Fluxo Medio: \n")
        print("\tTarefa:\t")
        for i in range(jobs):
            print("\t", SF[i].Operacao + 1)
        print("\n")
        print("\tDuracao:")
        for i in range(jobs):
            print("\t", SF[i].Duracao)
        fluxo = 0
        print("\n")
        print("\tFluxo:\t")
        for i in range(jobs):
            fluxo = fluxo + SF[i].Duracao
            print("\t", fluxo)
        print("\n")
        print("\tEntrega: ")
        for i in range(jobs):
            print("\t", SF[i].Entrega)
        print("\n")
        # Mostrando o resultado na tela para o Atraso Medio
        print(f"\tO menor atraso medio foi {Resultado_A} e o Metodo: ", Metodo_A)
        print("\n\tSolucao do problema de Atraso Medio:\n")
        print("\tTarefa:\t")
        for i in range(jobs):
            print("\t", SA[i].Operacao + 1)
        print("\n")
        print("\tDuracao:")
        for i in range(jobs):
            print("\t", SA[i].Duracao)
        fluxo = 0
        print("\n")
        print("\tFluxo:\t")
        for i in range(jobs):
            fluxo = fluxo + SA[i].Duracao
            print("\t", fluxo)
        print("\n")
        print("\tEntrega:")
        for i in range(jobs):
            print("\t", SA[i].Entrega)
        os.system("pause")
        return jobs

    # ******************************************************************************
    def Fluxo_Medio(jobs):
        F_medio = 0
        C = [0]*jobs
        # Calculando o tempo de conclusao de cada tarefa
        C[0] = SD[0]
        i = 1
        for i in range(jobs):
            C[i] = C[i - 1] + SD[i]
        i = 0
        for i in range(jobs):
            F_medio = F_medio + C[i]
        return (F_medio / jobs)


    # ******************************************************************************
    def Atraso_Medio(jobs):
        A_medio = 0
        C = [0]*jobs
        Atraso = [0]*jobs
        # Calculando o tempo de conclusao de cada tarefa
        C[0] = SD[0]
        i = 1
        for i in range(jobs):
            C[i] = C[i - 1] + SD[i]
        i = 0
        for i in range(jobs):
            Atraso[i] = Maximo(0, C[i] - SE[i])
        for i in range(jobs):
            A_medio = A_medio + Atraso[i]
        return (A_medio / jobs)


    # ******************************************************************************
    def Menor_Folga(jobs):  # Função do Menor Tempo de Processamento
        # Ordenar as tarefas para gerar a sequencia da menor para a maior folga.
        for j in range(jobs):
            Aux = Solucao[j]
            i = j - 1
            while i >= 0 and (SE[i] - SD[i]) > (Aux.Entrega - AD):
                Solucao[i + 1] = Solucao[i]
                Solucao[i] = Aux
                i = i - 1


    # ******************************************************************************
    def Razao_Critica(jobs):  # Função do Menor Tempo de Processamento
        # Ordenar as tarefas para gerar a sequencia da menor para a maior razao crítica.
        for j in range(jobs):
            Aux = Solucao[j]
            i = j - 1
            for i in i >= 0 and (SE[i] / SD[i]) > (Aux.Entrega / AD):
                Solucao[i + 1] = Solucao[i]
                Solucao[i] = Aux
                i = i - 1


    # ******************************************************************************
    def Maximo(a, b):
        if (a > b):
            return a
        else:
            return b


# ******************************************************************************
def Leitura_ID():  # Leitura do problema.
    os.system('cls')
    print("\n******************************************************************************")
    print("*****************| APS EDUCACIONAL - GABRIEL VOLCOV |*************************\n")
    machines = int(input("\n\tDigite o numero de maquinas em paralelo:"))  # leitura do número de máquinas
    jobs = int(input("n\tDigite o numero de tarefas a serem ordenadas:"))  # leitura do número de jobs
    print("\n\tNumero de maquinas:", machines)
    print("\tNumero de Tarefas:", jobs)
    print("\n")
    for i in range(jobs):  # Leitura da linha com as informações das durações
        TO[i] = i
        TD[i] = float(input(f"\tDigite a duracao da tarefa {i + 1}:"))
    print("\n")


# ******************************************************************************
def Fluxo_Medio_ID():
    F_medio = 0
    os.system('cls')
    print("\n******************************************************************************")
    print("*****************| APS EDUCACIONAL - GABRIEL VOLCOV |*************************\n")
    # Mostra o resultado da ordenação inicial
    print("\n\tResultado da Ordenacao por SPT:")
    print("\n\tTarefa:\t")
    for i in range(jobs):
        print("\t%d", SO[i] + 1)
    print("\n")
    print("\tDuracao:")
    for i in range(jobs):
        print("\t%.2f", SD[i])
    print("\n")
    for i in range(maq):
        Ocupacao[i] = 0
        Duracao_Total[i] = 0
    Maquina_Menor = 0
    for j in range(jobs):
        for i in range(maq):
            if (Duracao_Total[i] < Duracao_Total[Maquina_Menor]):
                Maquina_Menor = i
        F[Maquina_Menor][Ocupacao[Maquina_Menor]] = F[Maquina_Menor][Ocupacao[Maquina_Menor] - 1] + SD[j]
        Duracao_Total[Maquina_Menor] = F[Maquina_Menor][Ocupacao[Maquina_Menor]]
        Ocupacao[Maquina_Menor] = Ocupacao[Maquina_Menor] + 1
    print("\n\tOs tempos de conclusao esperados no sistema sao:\n")
    for j in range(maq):
        print("\tMaquina %d:\t", j + 1)
        for i in range(Ocupacao[j]):
            print(F[j][i], SO[i * maq + j] + 1, "\t")
        print("\n")
    for j in range(maq):
        for i in range(Ocupacao[j]):
            F_medio = F_medio + F[j][i]
    return (F_medio / jobs)


# ******************************************************************************
def SPT(self):  # Função do Menor Tempo de Processamento
    # Ordenar as tarefas para gerar a sequencia SPT.
    for j in range(self):
        Aux = Solucao[j]
        i = j - 1
        for i in range(i >= 0 and SD[i] > AD):  # i >= 0 and
            Solucao[i + 1] = Solucao[i]
            Solucao[i] = Aux
            i = i - 1


# ******************************************************************************
def Leitura_IDMAX():  # Leitura do problema.
    os.system('cls')
    print("\n******************************************************************************")
    print("*****************| APS EDUCACIONAL - GABRIEL VOLCOV |*************************\n")
    machines = int(input("\tDigite o numero de maquinas em paralelo: "))  # leitura do número de máquinas
    jobs = int(input("\tDigite o numero de tarefas a serem ordenadas: "))  # leitura do número de jobs
    print("\n\tNumero de maquinas:", machines)
    print("\tNumero de Tarefas:", jobs)
    for i in range(jobs):  # Leitura da linha com as informações das durações
        TO[i] = i
        TD[i] = float(input(f"\n\tDigite a duracao da tarefa {i + 1}: "))


# ******************************************************************************
def Fluxo_Maximo(maq):
    F_maximo = 0
    os.system('cls')
    print("\n******************************************************************************")
    print("*****************| APS EDUCACIONAL - GABRIEL VOLCOV |*************************\n")
    # Mostra o resultado da ordenação na tela
    print("\n\tResultado da ordenacao por LPT:\n")
    print("\tTafera:\t")
    for i in range(jobs):
        print("\t", SO[i] + 1)
    print("\n")
    print("\tDuracao:")
    for i in range(jobs):
        print("\t", SD[i])
    print("\n")
    for i in range(maq):
        Ocupacao[i] = 0
        Duracao_Total[i] = 0
    Maquina_Menor = 0
    for j in range(jobs):
        for i in range(maq):
            if (Duracao_Total[i] < Duracao_Total[Maquina_Menor]):
                Maquina_Menor = i
        F[Maquina_Menor][Ocupacao[Maquina_Menor]] = F[Maquina_Menor][Ocupacao[Maquina_Menor] - 1] + SD[j]
        Duracao_Total[Maquina_Menor] = F[Maquina_Menor][Ocupacao[Maquina_Menor]]
        Ocupacao[Maquina_Menor] = Ocupacao[Maquina_Menor] + 1
    # Mostra o resultado nas máquinas:
    print("\n\tOs tempos de conclusao esperados no sistema sao:\n")
    for j in range(maq):
        print(f"\tMaquina {j + 1}: ")
        for i in range(Ocupacao[j]):
            print(f"\t´{F[j][i]}({SO[i * maq + j] + 1})")
        print("\n")
    for j in range(maq):
        for i in range(Ocupacao[j]):
            if (F_maximo < F[j][i]):
                F_maximo = F[j][i]
    return (F_maximo)


# ******************************************************************************
def LPT(self):  # Função do Menor Tempo de Processamento
    # Ordenar as tarefas para gerar a sequencia SPT.
    for j in range(self):
        Aux = Solucao[j]
        i = j - 1
        for i in i >= 0 and SD[i] < AD:
            Solucao[i + 1] = Solucao[i]
            Solucao[i] = Aux
            i = i - 1


# ****************************************************************************** 4 - 01 OK
def Leitura_J():
    os.system('cls')
    print("\n******************************************************************************")
    print("*****************| APS EDUCACIONAL - GABRIEL VOLCOV |*************************\n")
    machines = 2
    jobs = int(input("\tDigite o numero de tarefas a serem ordenadas: "))  # leitura do número de jobs
    print("\n\tNumero de maquinas:", machines)
    print("\tNumero de Tarefas:", jobs)
    for i in range(machines):
        for j in range(jobs):
            M[i][j] = float(input(f"\tDigite o tempo de processamento da tarefa {j + 1} na maquina {i + 1}: "))
    print("\n")
    print("\n\tMatriz dos tempos de processamento das tarefas:\n")
    print("\tTarefa: ", end="")
    for j in range(jobs):
        print("\t", j + 1,"\t", end="")
    print("\n")
    for i in range(machines):
        print(f"\tMaquina {i + 1}: ", end="")
        for j in range(jobs):
            print("\t", M[i][j], end="")
        print("\n")
    os.system("pause")


# ****************************************************************************** 4 - 03
def SPT_J():  # Função do Menor Tempo de Processamento
    # Ordenar as tarefas para gerar a sequencia SPT.
    for i in range(machines):
        for j in range(jobs):
            Seq_Inicial_Tarefa[i * (jobs) + j] = j
            Seq_Inicial_Maquina[i * (jobs) + j] = i
            Seq_Inicial_Duracao[i * (jobs) + j] = M[i][j]
    for j in range(machines * jobs):
        Aux = Seq_Inicial[j]
        i = j - 1
        for i in i >= 0 and Seq_Inicial_Duracao[i] > AD:
            Seq_Inicial[i + 1] = Seq_Inicial[i]
            Seq_Inicial[i] = Aux
            i = i - 1


# ****************************************************************************** 4 - 02
def Johnson():
    SPT_J()
    for j in range(jobs):
        Atribuicao[j] = False
    posicao_inicio = 0
    posicao_final = jobs - 1
    for i in range(machines * jobs):
        if (Atribuicao[Seq_Inicial_Tarefa[i]] == False):
            if (Seq_Inicial_Maquina[i] == 0):
                Sol[posicao_inicio] = Seq_Inicial[i]
                Atribuicao[Seq_Inicial_Tarefa[i]] = True
                posicao_inicio = posicao_inicio + 1
            else:
                Sol[posicao_final] = Seq_Inicial[i]
                Atribuicao[Seq_Inicial_Tarefa[i]] = True
                posicao_final = posicao_final - 1
    os.system('cls')
    print("\n******************************************************************************")
    print("*****************| APS EDUCACIONAL - GABRIEL VOLCOV |*************************\n")
    print("\n\tSolucao encontrada pelo metodo de Johnson:")
    print("\n\tTarefa:\t")
    for j in range(jobs):
        print("\t", Sol_Tarefa[j] + 1)
    print("\n")
    Calculo_Makespan_J()


# ******************************************************************************
def Calculo_Makespan_J():
    # Inicializar a matriz de tempos de processamento
    for i in range(machines):
        for j in range(jobs):
            CJ[i][j] = 0
    # Primeira maquina e primeira tarefa
    CJ[0][0] = M[0][Sol_Tarefa[0]]
    # Primeira máquina todas as tarefas
    for j in range(jobs):
        CJ[0][j] = CJ[0][j - 1] + M[0][Sol_Tarefa[j]]
    # Primeira tarefa todas as máquinas
    for i in range(machines):
        CJ[i][0] = CJ[i - 1][0] + M[i][Sol_Tarefa[0]]
    # Demais tarefas
    maximo = 0
    for i in range(machines):
        for j in range(jobs):
            if (CJ[i - 1][j] > CJ[i][j - 1]):
                maximo = CJ[i - 1][j]
            else:
                maximo = CJ[i][j - 1]
        CJ[i][j] = maximo + M[i][Sol_Tarefa[j]]
    print("\n\tOs tempos esperados de conclusao no sistema sao:\n")
    print("\tTarefa:\t")
    for j in range(jobs):
        print("\t%d", Sol_Tarefa[j] + 1)
    print("\n")
    for i in range(machines):
        print(f"\tMaquina {i + 1}: ")
        for j in range(jobs):
            print("\t", CJ[i][j])
        print("\n")
    print("\tA duracao total da programacao e:", CJ[machines - 1][jobs - 1])
    os.system("pause")


# **********************************************************
def Leitura_N():
    os.system('cls')
    print("\n******************************************************************************")
    print("*****************| APS EDUCACIONAL - GABRIEL VOLCOV |*************************\n")
    machines = int(input("\n\tDigite o numero de maquinas: "))  # leitura do número de máquinas
    jobs = int(input("n\tDigite o numero de tarefas: "))  # leitura do número de jobs
    print("\n\tNumero de maquinas:", machines)
    print("\tNumero de Tarefas:", jobs)
    print("\n\tMatriz dos tempos de processamento:\n")
    for i in range(machines):
        for j in range(jobs):
            M[i][j] = float(input(f"\tDigite tempo de processamento da tarefa {j + 1} na maquina {i + 1}: "))
        print("\n")
    os.system('cls')
    print("\n******************************************************************************")
    print("*****************| APS EDUCACIONAL - GABRIEL VOLCOV |*************************\n")
    print("\n\tMatriz dos tempos de processamento:\n")
    print("\tTarefa:\t")
    for j in range(jobs):
        print("\t", j + 1)
        for i in range(machines):
            print(f"\tMaquina {i + 1}: ")
            for j in range(jobs):
                print("\t", M[i][j])
        print("\n")


# ******************************************************************************
def LPT_N(self):  # Função do Menor Tempo de Processamento
    # Ordenar as tarefas para gerar a sequencia SPT.
    for j in range(jobs):
        aux = 0
        for i in range(machines):
            aux += M[i][j]
        Seq_Ini_Carga[j] = aux
        Seq_Ini_Tarefa[j] = j
    for j in range(self):
        Aux = Seq_Ini[j]
        i = j - 1
        for i in i >= 0 and Seq_Ini_Carga[i] < Aux.Carga:
            Seq_Ini[i + 1] = Seq_Ini[i]
            Seq_Ini[i] = Aux
            i = i - 1
    print("\n\tSequencia Inicial Segundo a Carga Total:\n")
    print("\tTarefa:\t")
    for j in range(self):
        print("\t", Seq_Ini_Tarefa[j] + 1)
    print("\n")
    print("\tCarga Total:")
    for j in range(self):
        print("\t", Seq_Ini_Carga[j])
    os.system("pause")


# ******************************************************************************
def NEH():
    contador = 2  # Contador para o número total de tarefas na sequencia parcial.
    # verificar a melhor sequencia entre as 2
    Seq_Aux[0] = Seq_Ini_Tarefa[0]
    Seq_Aux[1] = Seq_Ini_Tarefa[1]

    Calculo_Makespan_N(contador)

    Resultado_N[0] = Seq_Ini_Tarefa[0]
    Resultado_N[1] = Seq_Ini_Tarefa[1]
    Makespan_Resultado = CN[machines - 1][contador - 1]

    # Calculando a outra possibilidade para 2 tarefas
    Seq_Aux[0] = Seq_Ini_Tarefa[1]
    Seq_Aux[1] = Seq_Ini_Tarefa[0]

    Calculo_Makespan_N(contador)

    if (CN[machines - 1][contador - 1] < Makespan_Resultado):
        Resultado_N[0] = Seq_Ini_Tarefa[0]
        Resultado_N[1] = Seq_Ini_Tarefa[1]
        Makespan_Resultado = CN[machines - 1][contador - 1]

    while (contador < jobs):
        aux3 = Seq_Ini_Tarefa[contador]  # aux3 = recebe a tarefa que será inserida na sequencia
        Makespan_Parcial = 200000000  # Valor elevado para não atrapalhar o resultado.
        h = 0
        # Contador para a posicao de inserção da próxima tarefa.
        while (h <= contador):
            # Seq_Aux recebe a solucao parcial.
            for i in range(contador):
                Seq_Aux[i] = Resultado_N[i]

            # Inserir a proxima tarefa na posicao h
            j = contador
            for j in range(h):
                Seq_Aux[j] = Seq_Aux[j - 1]
                j = j - 1

            Seq_Aux[h] = aux3

            Calculo_Makespan_N(contador + 1)

            if (CN[machines - 1][contador] < Makespan_Parcial):
                for i in range(contador):
                    Resultado_Parcial[i] = Seq_Aux[i]
                    Makespan_Parcial = CN[machines - 1][contador]
            h = h + 1
            for i in range(contador):
                Resultado_N[i] = Resultado_Parcial[i]
    Makespan_Resultado = Makespan_Parcial
    contador = contador + 1
    # fim do NEH
    for i in range(jobs):
        Seq_Aux[i] = Resultado_N[i]

    Calculo_Makespan_N(jobs)
    Makespan_NEH = CN[machines - 1][jobs - 1]


# ******************************************************************************
def Calculo_Makespan_N(self):
    # Inicializar a matriz de tempos de processamento
    for i in range(machines):
        for j in range(self):
            CN[i][j] = 0
    # Primeira maquina e primeira tarefa
    CN[0][0] = M[0][Seq_Aux[0]]
    # Primeira máquina todas as tarefas
    for j in range(self):
        CN[0][j] = CN[0][j - 1] + M[0][Seq_Aux[j]]
    # Primeira tarefa todas as máquinas
    i = 1
    for i in range(machines):
        CN[i][0] = CN[i - 1][0] + M[i][Seq_Aux[0]]
    # Demais tarefas
    maximo = 0
    i = 1
    for i in range(machines):
        for j in range(self):
            if (CN[i - 1][j] > CN[i][j - 1]):
                maximo = CN[i - 1][j]
            else:
                maximo = CN[i][j - 1]
            CN[i][j] = maximo + M[i][Seq_Aux[j]]


#******************************************************************************
#Escolha do tipo de problema
while problema != 6:
    os.system('cls')
    print("\n******************************************************************************")
    print("*****************| APS EDUCACIONAL - GABRIEL VOLCOV |*************************\n")
    print("Escolha o tipo de problema:\n")
    print("\t Maquina unica:\n")
    print("\t\t 1 - Maquina unica (Fluxo medio e Atraso Medio):\n")
    print("\t Maquinas paralelas identicas:\n")
    print("\t\t 2 - Menor tempo medio de fluxo\n")
    print("\t\t 3 - Menor tempo total da programacao\n")
    print("\t Multiplas maquinas distintas:\n")
    print("\t\t 4 - Flowshop - Algoritmo de Johnson\n")
    print("\t\t 5 - Flowshop para ambientes com mais de 2 maquinas\n")
    print("\t\t 6 - SAIR\n")
    problema = int(input("Digite o numero do problema a ser resolvido: "))


    if problema == 1: # Maquinas unicas
        Leitura_Regras()
        Regras(jobs)
        #break

    elif problema == 2: #Maquinas paralelas identicas
        Leitura_ID()
        for i in range(jobs):
            Solucao[i] = Tarefas[i]
            Resultado = Fluxo_Medio_ID(machines)
        print("\n\tO Fluxo Medio encontrado foi ", Resultado)
        os.system("pause")
        #break

    elif problema == 3:
        Leitura_IDMAX()
        for i in range(jobs):
            Solucao[i] = Tarefas[i]
        Resultado = Fluxo_Maximo(machines)
        print("\n\tO Fluxo Maximo encontrado foi ", Resultado)
        os.system("pause")
        #break

    elif problema == 4:
        Leitura_J()
        Johnson()
        #break

    elif problema == 5:
        Leitura_N()
        NEH()
        os.system('cls')
        print("\n******************************************************************************")
        print("*****************| APS EDUCACIONAL - GABRIEL VOLCOV |*************************\n")
        print("\tA solucao encontrada pelo NEH:\n")
        print("\tTarefa:\t")
        for j in range(jobs):
            print(Resultado_N[j]+1)
            print("\n")
            print("\tMatriz dos Tempos de Conclusao:\n")
            print("\tTafera:\t")
        for j in range(jobs):
            print(Resultado_N[j]+1)
            print("\n")
        for i in range(machines):
                print("\tMaquina", i+1)
        for j in range(jobs):
            print("\t",CN[i][j])
            print("\n")
            print("\tA duracao todal da programacao (Makespan) e:", Makespan_NEH)
            print("\n")
        os.system("pause")
        #break

    elif problema == 6:
        break

