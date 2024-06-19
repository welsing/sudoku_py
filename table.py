## CRIAR MATRIZ 6X6
# M = []
from random import randint
from time import sleep
## GERAR TABULEIRO VAZIO 
def empty_table():
    table = []            
    for i in range(9):   # cria listas de 9 zeros 9 vezes
        line = [0]*9
        table.append(line)   # adiciona a linha ao tabuleiro
    return table


## Visualiza Tabuleiro
def view_table(tab):
    line_labels = "ABCDEFGHI"
    print("="*26)
    for n, line in enumerate(tab):  # Faz um laço pelo que passa linha por linha do tabuleiro

        if n % 3 == 0 and n != 0:   # Condição para criar separador a cada 3 linhas
            
            print("-"*26)

        print(line_labels[n] + "  ", end='')   # Atribui uma letra para cada linha

        for j, col in enumerate(line):  # Passa por cada elemento (coluna) da linha selecionada

            if j % 3 == 0 and j != 0:  # Condição que cria o separador vertical
                print("| ", end="")

            if col == 0:            # Printa o elemento (col) da linha (line)
                print(".", end=' ')
            else:
                print(col, end=' ')
        print('|', end='')
        print()



    print('-- ', end='')  
    col_labels = "JKLMNOPQR"    
    for i in range(len(col_labels)):          # Da nome as colunas
        print(col_labels[i], end=' ')
        if i == 2 or i == 5 and i != 0:
            print('  ', end='')
    print("|", end='')
    print()        
    print("="*26)
        


# Função auxiliar da random_game()
def is_safe(table, line, col, num):
    if num in table[line]:
        return False
    

    if num in [table[r][col] for r in range(9)]:
        return False
    
    return True


def random_game(table):


    for i, linha in enumerate(table):

        for j, coluna in enumerate(linha):

            while True:
                n = randint(1, 9)
                # if n not in table[i]:
                #     table[i][j] = n
                
                if is_safe(table, i, j, n):
                    table[i][j] = n
                    break




tabuleiro = empty_table()


view_table(tabuleiro)
random_game(tabuleiro)
view_table(tabuleiro)


