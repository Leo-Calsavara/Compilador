def get_type(nome):
    if nome in ['int', 'float', 'bool']:
        return nome
    if nome in ['_true', '_false']:
        return 'bool'
    for entry in tabela_de_tipos:
        if entry["nome"] == nome:
            return entry["tipo"]

from collections import Counter

def verify_types(ops):
    counts = Counter(ops)
    
    float_count = counts.get("float", 0)
    int_count = counts.get("int", 0)
    bool_count = counts.get("bool", 0)

    non_zero_counts = sum(1 for count in [float_count, int_count, bool_count] if count > 0)

    if non_zero_counts > 1:
        print("tipos conflitantes")
    else:
        print("sem conflitos")

caminho_do_arquivo = 'tokens_saida_semantico.txt'

linhas_arquivo = []

with open(caminho_do_arquivo, 'r') as arquivo:
    linhas_arquivo = [linha.strip() for linha in arquivo]

tabela_de_tipos = []
this = False
tipos = ["int", "float", "bool"]
aux = ["None", "variavel", "palavra_reservada"]
variaveis = []

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
                print('A variável', palavra3, 'não foi declarada')
        this = False

        if palavra2 in tipos or palavra2 == 'variavel': #se for int,float bool ou uma variavel
            proxima_palavra = linhas_arquivo[i + 1].split() 

            if proxima_palavra[2] == '=':
                if palavra2 == 'variavel' or palavra2 == 'None' or palavra2== 'palavra_reservada': 
                    variaveis.append(get_type(palavra3))
                else: variaveis.append(palavra2)
            
                proxima_palavra = linhas_arquivo[i + 2].split() 

            else: continue

            if proxima_palavra[1] == 'variavel' or proxima_palavra[1] == 'None' or proxima_palavra[1]== 'palavra_reservada':   
                variaveis.append(get_type(proxima_palavra[2]))
            else: variaveis.append(proxima_palavra[1])
                        
            proxima_palavra = linhas_arquivo[i + 3].split() 
            cont = 4

            while proxima_palavra[1] in ['Op_aritmetico', 'Op_relacional']:
                proxima_palavra = linhas_arquivo[i + cont].split() 

                if proxima_palavra[1] in tipos or proxima_palavra[1] == 'variavel' or proxima_palavra[1] == 'None' or proxima_palavra[1] == 'palavra_reservada': #se for int,float bool ou uma variavel
                    if proxima_palavra[1] == 'variavel' or proxima_palavra[1] == 'None' or proxima_palavra[1]== 'palavra_reservada': 
                        variaveis.append(get_type(proxima_palavra[2]))
                    else: variaveis.append(proxima_palavra[1])
                cont +=1
                proxima_palavra = linhas_arquivo[i + cont].split()
                cont +=1

        if variaveis.__len__() == 0:
            continue
        # verify_types(variaveis)
        print(variaveis)
        variaveis = []



print('=================================================================================')
print('TABELA:')
print("Tabela de nomes e tipos:")
for entrada in tabela_de_tipos:
    print(f"Nome: {entrada['nome']}, Tipo: {entrada['tipo']}, Usada: {entrada['used']}")