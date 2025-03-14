from collections import Counter

#################################################### VARIAVEIS GLOBAIS ###################################################################

caminho_do_arquivo = 'tokens_saida_semantico.txt'
aux = ["None", "variavel", "palavra_reservada"]
tipos = ["int", "float", "bool"]
tabela_de_tipos = []
linhas_arquivo = []
variaveis = []
this = False

######################################################### FUNÇÕES ###############################################################

def verify_var(palavra):
    if palavra[1] == 'variavel' or palavra[1] == 'None' or palavra[1]== 'palavra_reservada':   
        var = get_type(palavra[2])
        if var != '_pot':
            variaveis.append(var)
            return False
        else: return var
    else: 
        variaveis.append(palavra[1])
        return False

def get_type(nome):
    if nome in ['int', 'float', 'bool', '_pot']:
        return nome
    if nome in ['_true', '_false']:
        return 'bool'
    for entry in tabela_de_tipos:
        if entry["nome"] == nome:
            return entry["tipo"]

def verify_types(linha, ops):
    valid_types = {"float", "int", "bool"}

    # Verifica se todos os elementos pertencem ao conjunto válido
    if any(op not in valid_types for op in ops):
        print(f"Erro: tipo inválido encontrado na linha {linha}")
        return

    counts = Counter(ops)

    float_count = counts.get("float", 0)
    int_count = counts.get("int", 0)
    bool_count = counts.get("bool", 0)

    non_zero_counts = sum(1 for count in [float_count, int_count, bool_count] if count > 0)

    if non_zero_counts > 1:
        primeiro_operando = ops[0] 

        if primeiro_operando == "int" and float_count > 0:
            print(f"Conflito de tipo encontrado na linha {linha}, {ops}: requer widening (diminuir float para int)")
        elif primeiro_operando == "float" and int_count > 0:
            print(f"Conflito de tipo encontrado na linha {linha}, {ops}: requer expansão (aumentar int para float)")
        elif primeiro_operando == "bool" and (int_count > 0 or float_count > 0):
             raise ValueError(f"Erro na linha {linha}: bool não pode ser misturado com int ou float")
        elif (primeiro_operando == "int" or primeiro_operando == "float") and bool_count > 0:
            raise ValueError(f"Erro na linha {linha}: {primeiro_operando} não pode ser misturado com bool")
        else:
            print(f"Conflito de tipo encontrado na linha {linha}, {ops}: requer conversão")

######################################################### MAIN ###################################################################

with open(caminho_do_arquivo, 'r') as arquivo:
    linhas_arquivo = [linha.strip() for linha in arquivo]

for i in range(len(linhas_arquivo)):
    palavras = linhas_arquivo[i].split()

    if len(palavras) == 3:
        palavra1, palavra2, palavra3 = palavras

        #cria tabela de símbolos
        if palavra2 in tipos and palavra3 != "None":
            if not any(entry["nome"] == palavra3 for entry in tabela_de_tipos): #caso variavel não esteja na tabela, é incluida
                tabela_de_tipos.append({"nome": palavra3, "tipo": palavra2, "used": False}) #inclui como nunca usada

        if palavra2 == "variavel":
            for entry in tabela_de_tipos:
                if entry["nome"] == palavra3:
                    entry["used"] = True
                    this = True
            if this == False:
                raise ValueError('A variável', palavra3, 'não foi declarada')
        this = False
        cont = 1

        if palavra2 in tipos or palavra2 == 'variavel': #se for int,float bool ou uma variavel
            proxima_palavra = linhas_arquivo[i + cont].split() 
            cont += 1

            if proxima_palavra[2] == '=':
                verify_var(palavras)
                proxima_palavra = linhas_arquivo[i + cont].split() 
                cont += 1
            else: continue

            if verify_var(proxima_palavra):
                cont += 1
                proxima_palavra = linhas_arquivo[i + cont].split() 
                verify_var(proxima_palavra)           
                cont += 2  
                proxima_palavra = linhas_arquivo[i + cont].split() 
                verify_var(proxima_palavra)      

            proxima_palavra = linhas_arquivo[i + cont].split() 
            cont += 1


            while proxima_palavra[1] in ['Op_aritmetico', 'Op_relacional', 'Op_logico']:

                if variaveis[0] == 'bool' and proxima_palavra[1] == 'Op_aritmetico':
                    raise ValueError(f'ERRO DE OPERADOR: BOOL e {proxima_palavra[1]} não podem ser usados juntos')

                if (variaveis[0] == 'int' or variaveis[0] == 'float') and (proxima_palavra[1] == 'Op_relacional' or proxima_palavra[1] == 'Op_logico'):
                    raise ValueError(f'ERRO DE OPERADOR: {variaveis[0]} e {proxima_palavra[1]} não podem ser usados juntos')

                proxima_palavra = linhas_arquivo[i + cont].split() 
                cont += 1

                if verify_var(proxima_palavra):
                    cont += 1
                    proxima_palavra = linhas_arquivo[i + cont].split() 
                    verify_var(proxima_palavra)           
                    cont += 2  
                    proxima_palavra = linhas_arquivo[i + cont].split() 
                    verify_var(proxima_palavra)      
               

                proxima_palavra = linhas_arquivo[i + cont].split()
                cont += 1

        if variaveis.__len__() == 0:
            continue
        verify_types(proxima_palavra[0], variaveis)
        variaveis = []


# print('=================================================================================')
# print('TABELA:')
#print("Tabela de nomes e tipos:")
for entrada in tabela_de_tipos:
    #print(f"Nome: {entrada['nome']}, Tipo: {entrada['tipo']}, Usada: {entrada['used']}")
    if entrada['used'] == False:
        print(f"WARNING:\nA variavel {entrada['nome']} foi declarada, mas nunca usada")