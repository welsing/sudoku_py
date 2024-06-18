## CRIAR MATRIZ 6X6
# M = []


## GERAR TABULEIRO VAZIO 
def empty_table():
    table = []
    for i in range(9):
        line = [0]*9
        table.append(line)
    return table


## RANDOMIZA INICIO DE JOGO 
def random_start():
    print("ENGINE...")


def view_table(tab):
    for n, line in enumerate(tab):
        for n, col in enumerate(line):
            if n == 3:
                print("| ", end="")
            if col == 0:
                print(".", end=' ')
            else:
                print(col, end=' ')
        print()



view_table(empty_table())

# for i, g in enumerate(empty_table()):
#     print(i+1, g)