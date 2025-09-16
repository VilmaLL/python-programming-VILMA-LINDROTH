
Row1 = [letter + '1' for letter in 'ABCDEFGH']
print(Row1)

chessboard = [[col + str(row) for col in 'ABCDEFGH'] for row in range(1, 9)]
for row in chessboard:
    print(row)


'''
for i in range(len(Rows)):
    print('\n')
    for j in range(len(Column)):
        print(f"{Column[j]}{Rows[i]}" , end= ' ')
        '''