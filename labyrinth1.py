string = input().split(" ")
w  = int(string[0])
h = int(string[1])
Matrix_input = [[' ' for x in range(h)] for y in range(w)] 
for x in range(w):
    string = input()
    for y in range(h):
        Matrix_input[x][y] = string[y]
        if Matrix_input[x][y] == '*':
            x_start = x
            y_start = y

Matrix_result = [[-1 for x in range(h)] for y in range(w)] 
Matrix_result[x_start][y_start] = 0
for step in range(1,2*w+2*h+2):
    for x in range(w): 
        for y in range(h):
            if Matrix_result[x][y] == step-1:
                    if (x + 1 < w):
                        if (Matrix_result[x+1][y] == -1) & (Matrix_input[x+1][y] != '#') :
                            Matrix_result[x+1][y] = step

                    if  (y + 1 < h):
                         if (Matrix_result[x][y+1] == -1) & (Matrix_input[x][y+1] != '#')  :
                            Matrix_result[x][y+1] = step

                    if (x - 1 >= 0):
                        if (Matrix_result[x-1][y] == -1) & (Matrix_input[x-1][y] != '#') :
                            Matrix_result[x-1][y] = step

                    if (y - 1 >= 0) :
                        if (Matrix_result[x][y-1] == -1) & (Matrix_input[x][y-1] != '#') :
                            Matrix_result[x][y-1] = step
                



for x in range(w):
    for y in range(h):
        print(Matrix_result[x][y], end = " ")
    print("")



