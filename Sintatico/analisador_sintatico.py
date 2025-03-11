tabela = {
    '<prog>': {
        '_begin': ['_begin', '<decls>', '<contx>', '_end'],
        'ε': ['ε']
    },
    '<decls>': {
        '_int': ['<dec>', '<decls>'],
        '_float': ['<dec>', '<decls>'],
        '_bool': ['<dec>', '<decls>'],
        '_receba': ['ε'],
        '_end': ['ε'],
        'id': ['ε'],
        '_if': ['ε'],
        '_while': ['ε'], 
        '_for': ['ε'],
        '_seliga': ['ε'],
        '_receba': ['ε']
    },
    '<dec>': {
        '_int': ['<type>', '<dec’>'],
        '_float': ['<type>', '<dec’>'],
        '_bool': ['<type>', '<dec’>'],
        'id': ['sinc'],
        'num': ['sinc'],
        '!': ['sinc']
    },
    '<dec’>': {
        'id': ['id', '<at>'],
        '_end': ['sinc'],
        '_int': ['sinc'],
        '_float': ['sinc'],
        '_bool': ['sinc'],
        '!': ['sinc']
    },
    '<type>': {
        '_int': ['_int'],
        '_float': ['_float'],
        '_bool': ['_bool'],
        'id': ['sinc']
    },
    '<contx>': {
        '_if': ['<if>', '(', '<cond>', ')', '{', '<contx’>', '}', '<else>', '{', '<contx>', '}'],
        '_while': ['<while>', '(', '<cond>', ')', '{', '<contx’>', '}', '<contx>'],
        '_for': ['<for>', '(', '<dec>', '<cond>', ';', 'id', '<id_for>', ')', '{', '<contx’>', '}', '<contx>'],
        '_seliga': ['<seliga>', '(','“','str','”','<aux>',')',';', '<contx>'],
        '_receba': ['<receba>', '(', 'id', ')',';', '<contx>'],
        'id': ['<at>', '<contx>'],
        '}': ['sinc'],
        ')': ['sinc'],
        '_end': ['sinc']
    },
    '<aux>':{
        ',': [',', '<ids>'],
        ')': ['ε']
    },
    '<contx’>': {
        '_if': ['<if>', '(', '<cond>', ')', '{', '<contx’>', '}', '<else>', '{', '<contx>', '}'],
        '_while': ['<while>', '(', '<cond>', ')', '{', '<contx’>', '}', '<contx>'],
        '_for': ['<for>', '(', '<dec>', '<cond>', ';', 'id', '<id_for>', ')', '{', '<contx’>', '}', '<contx>'],
        '_seliga': ['<seliga>', '(','“','str','”','<aux>',')',';', '<contx>'],
        '_receba': ['<receba>', '(', 'id', ');', '<contx>'],
        'id': ['<at>', '<contx>'],
        '}': ['sinc']
    },
    '<if>': {
        '_if': ['_if'],
        '(': ['sinc']
    },
    '<else>': {
        '_else': ['_else'],
        '{': ['ε']
    },
    '<while>': {
        '_while': ['_while'],
        '(': ['sinc']
    },
    '<for>': {
        '_for': ['_for'],
        '(': ['sinc']
    },
    '<id_for>': {
        '++': ['++'],
        '--': ['--'],
        ')': ['sinc']
    },
    '<seliga>': {
        '_seliga': ['_seliga'],
        '(': ['sinc']
    },
    '<ids>': {
        'id': ['id', '<fechap>']
    },
    '<fechap>': {
        ')': ['ε']
    },
    '<receba>': {
        '_receba': ['_receba'],
        '(': ['sinc']
    },
    '<at>': {
        'id': ['id', '=', '<at’>'],
        '=': ['=', '<at’>'],
        ';': [';'],
        '_if': ['sinc'],
        '_while': ['sinc'], 
        '_for': ['sinc'],
        '_seliga': ['sinc'],
        '_receba': ['sinc']

    },
    '<at’>': {
        'id': ['<id_num>', '<expr>'],
        'num': ['<id_num>', '<expr>'],
        '_true': ['_true', ';'],
        '_false': ['_false', ';'],
        '_pot': ['<pot>', '(', '<id_num>', ',', '<id_num>', ')', '<expr>'],
        '_if': ['sinc'],
        '_while': ['sinc'], 
        '_for': ['sinc'],
        '_seliga': ['sinc'],
        '_receba': ['sinc']
    },
    '<expr>': {
        '+': ['<opr>', '<expr’>'],
        '-': ['<opr>', '<expr’>'],
        '*': ['<opr>', '<expr’>'],
        '/': ['<opr>', '<expr’>'],
        ';': [';'],
        'id': ['sinc'],
        '_if': ['sinc'],
        '_while': ['sinc'], 
        '_for': ['sinc'],
        '_seliga': ['sinc'],
        '_receba': ['sinc']
    },
    '<expr’>': {
        'num': ['<id_num>', '<expr>'],
        'id': ['<id_num>', '<expr>'],
        '_pot': ['<pot>', '(', '<id_num>', ',', '<id_num>', ')', '<expr>'],
        '_if': ['sinc'],
        '_while': ['sinc'], 
        '_for': ['sinc'],
        '_seliga': ['sinc'],
        '_receba': ['sinc']
    },
    '<opr>': {
        '+': ['+'],
        '-': ['-'],
        '/': ['/'],
        '*': ['*'],
        'id': ['sinc'],
        'num': ['sinc'],
        '_pot': ['sinc'],
        '!': ['sinc']
    },
    '<pot>': {
        '_pot': ['_pot'],
        '(' : ['sinc']
    },
    '<id_num>': {
        'id': ['id'],
        'num': ['num'],
        '::': ['sinc'],
        '<': ['sinc'],
        '>': ['sinc'], 
        '<=': ['sinc'],
        '>=': ['sinc'],
        '!=': ['sinc'],
        '+': ['sinc'],
        '-': ['sinc'],
        '*': ['sinc'], 
        '/': ['sinc'],
        ')': ['sinc'],
        '!': ['sinc'] 
    },
    '<cond>': {
        'id': ['<id_num>', '<cond’>'],
        'num': ['<id_num>', '<cond’>'],
        '!': ['!', 'id', '<cond”>'],
        ')': ['sinc']
    },
    '<cond’>': {
        '::': ['<operadores>', '<cond>'],
        '>': ['<operadores>', '<cond>'],
        '<': ['<operadores>', '<cond>'],
        '<=': ['<operadores>', '<cond>'],
        '!=': ['<operadores>', '<cond>'],
        '>=': ['<operadores>', '<cond>'],
        '&': ['<operadores>', '<cond>'],
        '|': ['<operadores>', '<cond>'],
        '+': ['<opr>', '<cond>'],
        '-': ['<opr>', '<cond>'],
        '*': ['<opr>', '<cond>'],
        '/': ['<opr>', '<cond>'],
        'ε': ['ε'],
        ')': ['ε'],
        'id': ['ε'],
        'num': ['ε'], 
        '!': ['ε']
    },
    '<cond”>': {
        '&': ['<logicos>', '<cond>'],
        '|': ['<logicos>', '<cond>'],
        ')': ['ε'],
        'id': ['ε'],
        'num': ['ε'], 
        '!': ['ε']
    },
    '<operadores>': {
        '&': ['<logicos>'],
        '|': ['<logicos>'],

        '::': ['<relacional>'],
        '>': ['<relacional>'],
        '<': ['<relacional>'],
        '<=': ['<relacional>'],
        '>=': ['<relacional>'],
        '!=': ['<relacional>'],
        'id': ['sinc'],
        'num': ['sinc'], 
        '!': ['sinc']
    },
    '<logicos>': {
        '&': ['&'],
        '|': ['|'],
        'id': ['sinc'],
        'num': ['sinc'], 
        '!': ['sinc']
    },
    '<relacional>': {
        '::': ['::'],
        '>': ['>'],
        '<': ['<'],
        '<=': ['<='],
        '!=': ['!='],
        '>=': ['>='],
        'id': ['sinc'],
        'num': ['sinc'], 
        '!': ['sinc']
    }
}



def analisar(tokens):
    pilha = ['<prog>'] 
    i = 0  

    while pilha:
        topo = pilha.pop() 

        if i < len(tokens):
            entrada = tokens[i]
        else:
            entrada = None 


        if topo == entrada:
            print(f"Consome token: {entrada}")
            i += 1 
        
        elif topo in tabela:  
            if entrada in tabela[topo]:
                producao = tabela[topo][entrada]

                if producao != ['ε'] and producao != ['sinc']:
                    pilha.extend(reversed(producao))

                    print(f"Empilha: {producao}")
                print(f"Pilha atual: {pilha}\n")
                
            else:
                print(f"Pilha atual: {pilha}\n")
                print(f"ERRO: Produção não encontrada para {topo} com token {entrada}.")
                break
        else:
            print(f"Pilha atual: {pilha}\n")
            print(f"ERRO: Token inesperado {topo}: {entrada}")
            break

    if i == len(tokens) and not pilha:
        print("Análise concluída com sucesso.")
    else:
        print("Análise terminou com erros.")

def ler_tokens_arquivo(nome_arquivo):
    tokens = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                token = linha.strip() 
                if token: 
                    tokens.append(token)
    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
    return tokens

tokens = ler_tokens_arquivo('tokens.txt')


analisar(tokens)