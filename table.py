## CRIAR MATRIZ 6X6
# M = []


## GERAR TABULEIRO VAZIO 
def empty_table():
    table = []            
    for i in range(9):   # cria listas de 9 zeros 9 vezes
        line = [0]*9
        table.append(line)   # adiciona a linha ao tabuleiro
    return table


## RANDOMIZA INICIO DE JOGO 
def random_start():
    print("ENGINE...")


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
        


tabuleiro = empty_table()


view_table(tabuleiro)

