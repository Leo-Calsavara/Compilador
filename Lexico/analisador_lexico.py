palavras_reservadas = [
    '_for', '_begin', '_end', '_receba', '_seliga', '_if', '_else', 
    '_int', '_float', '_bool', '_while', '_true', '_false', '_pot'
]

operadores_aritmeticos = ['+', '-', '*', '/']
operadores_logicos = ['&', '|', '!']

def getPalavraReservada(palavra):
    if palavra in palavras_reservadas:    
        return palavra
    else:
        return -1

def getFloat(num):
    if num.count('.') <= 1:
        return True
    else:
        return False

def getOpAritmetico(op):
    if len(op) > 1:
        return -1
    else: 
        if op in operadores_aritmeticos:
            return op
        else:
            return -1

def adicionar_par_sintatico(linha, tipo):
    k.append((linha, tipo))

def adiciona_par_semantico(linha, posicao, tipo):
    semantico.append((linha, tipo, posicao))

def ler_caracteres(arquivo):
    tokens = ''
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            while True:
                char = f.read(1)
                if not char:
                    break
                tokens += char
        return tokens

    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")

tokens = ler_caracteres('tokens.txt')

k = []
semantico = []
i = 0
linha = 1

while i < len(tokens):
    if tokens[i] == '_':

        j = i + 1
        aux = tokens[i]

        while j < len(tokens) and tokens[j].isalpha():
            aux += tokens[j]
            j += 1
        
        a = getPalavraReservada(aux)

        if a != -1:
            adicionar_par_sintatico(linha, a)
            adiciona_par_semantico(linha, a, 'palavra_reservada')
            i = j
        
            if tokens[i] == ' ':
                i += 1
                if tokens[i].isalpha():
                    j = i + 1
                    aux = tokens[i]

                    while j < len(tokens) and tokens[j].isalnum():
                        aux += tokens[j]
                        j += 1

                    adicionar_par_sintatico(linha, 'id')     
                    a = a[1:]
                    adiciona_par_semantico(linha, aux, a)

        else:
            print('O token', aux, 'da linha', linha, 'não faz parte da linguagem, verifique a digitação')
        i = j

    elif tokens[i].isdigit():
        j = i + 1
        aux = tokens[i]

        while j < len(tokens) and (tokens[j].isdigit() or tokens[j] == '.'):
            aux += tokens[j]
            j += 1
        
        if '.' in aux:
            if getFloat(aux):
                adicionar_par_sintatico(linha, 'num')
                adiciona_par_semantico(linha, 'float', None)

            else:
                print('O token', aux, 'da linha', linha, 'não faz parte da linguagem, verifique a digitação')
        else:
            adicionar_par_sintatico(linha, 'num')
            adiciona_par_semantico(linha, 'int', None)
        i = j

    elif tokens[i] == ' ' or tokens[i] == '\t':
        i += 1

    elif tokens[i].isalpha():
        j = i + 1
        aux = tokens[i]

        while j < len(tokens) and tokens[j].isalnum():
            aux += tokens[j]
            j += 1

        adicionar_par_sintatico(linha, 'id')     
        adiciona_par_semantico(linha, aux, 'variavel')

        i = j  

    elif tokens[i] == '\n':
        linha += 1
        i += 1

    elif tokens[i] in operadores_aritmeticos:
        pos = getOpAritmetico(tokens[i])
        if pos != -1:
            adicionar_par_sintatico(linha, pos)
            adiciona_par_semantico(linha, pos, 'Op_aritmetico')
        else:
            print('O token', tokens[i], 'da linha', linha, 'não faz parte da linguagem, verifique a digitação')
        i += 1

    elif tokens[i] == ':':
        if i + 1 < len(tokens) and tokens[i+1] == ':':
            adicionar_par_sintatico(linha, '::')
            adiciona_par_semantico(linha, '::', 'Op_relacional')
            i += 2
        else:                        
            print('O token', tokens[i], 'da linha', linha, 'não faz parte da linguagem, verifique a digitação')
            i += 1

    elif tokens[i] == '!':
        if tokens[i+1] == '=':
            adicionar_par_sintatico(linha, '!=')
            adiciona_par_semantico(linha, '!=', None)
            i+=2
        else:    
            adicionar_par_sintatico(linha, '!')
            adiciona_par_semantico(linha, '!', None)
            i += 1

    elif tokens[i] == '>':
        if i + 1 < len(tokens) and tokens[i+1] == '=':
            adicionar_par_sintatico(linha, '>=')
            adiciona_par_semantico(linha, '>=', None)
            i += 2
        else:
            adicionar_par_sintatico(linha, '>')
            adiciona_par_semantico(linha, '>', None)
            i += 1

    elif tokens[i] == '<':
        if i + 1 < len(tokens) and tokens[i+1] == '=':
            adicionar_par_sintatico(linha, '<=')
            adiciona_par_semantico(linha, '<=', None)
            i += 2
        else:
            adicionar_par_sintatico(linha, '<')
            adiciona_par_semantico(linha, '<', None)
            i += 1

    elif tokens[i] == '=':
        adicionar_par_sintatico(linha, '=')
        adiciona_par_semantico(linha, '=', None)
        i += 1
    
    elif tokens[i] == '(':
        adicionar_par_sintatico(linha, '(')
        adiciona_par_semantico(linha, '(', None)
        i += 1

    elif tokens[i] == ')':
        adicionar_par_sintatico(linha, ')')
        adiciona_par_semantico(linha, ')', None)
        i += 1

    elif tokens[i] == '{':
        adicionar_par_sintatico(linha, '{')
        adiciona_par_semantico(linha, '{', None)
        i += 1

    elif tokens[i] == '}':
        adicionar_par_sintatico(linha, '}')
        adiciona_par_semantico(linha, '}', None)
        i += 1

    elif tokens[i] == ';':
        adicionar_par_sintatico(linha, ';')
        adiciona_par_semantico(linha, ';', None)
        i += 1

    elif tokens[i] == ',':
        adicionar_par_sintatico(linha, ',')
        adiciona_par_semantico(linha, ',', None)
        i += 1

    elif tokens[i] == '“':
        adicionar_par_sintatico(linha, '“')
        adiciona_par_semantico(linha, '“', None)
        j = i + 1

        while j < len(tokens) and tokens[j] != '”':
        
            j += 1
        adicionar_par_sintatico(linha, 'str')
        adiciona_par_semantico(linha, 'str', None)

        if j < len(tokens):
            adicionar_par_sintatico(linha, '”')
            adiciona_par_semantico(linha, '”', None)
            i = j + 1
        else:
            print("Erro léxico, necessita de um fecha aspas na linha", linha, "Antes de continuar ajuste o erro...")
            break

    elif tokens[i] in operadores_logicos:
        adicionar_par_sintatico(linha, tokens[i])
        adiciona_par_semantico(linha, tokens[i], None)
        i += 1
                       
    else:
        print('O token', tokens[i], 'da linha', linha, 'não faz parte da linguagem, verifique a digitação')
        i += 1

with open('tokens_saida.txt', 'w') as saida:
    for t in k:
        linha, pos = t
        saida.write(f"{pos}\n")

with open('../Semantico/tokens_saida_semantico.txt', 'w') as saida:
    for linha, tipo, posicao in semantico:
        saida.write(f"{linha} {tipo} {posicao}\n")