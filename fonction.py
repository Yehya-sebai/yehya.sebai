def graph_y_equals_abs_x():
    width = 20
    height = 10
    midpoint = width // 2  
    for y in range(height, -1, -1):
        for x in range(width + 1):
            x_adjusted = x - midpoint  

            if x == midpoint and y == 0:
                print('+', end=' ')  
            elif x == midpoint:
                print('|', end=' ')
            elif y == 0:
                print('-', end=' ') 
            elif y == abs(x_adjusted):
                print(' *', end=' ')  
            else:
                print('   ', end=' ')  
        print()

graph_y_equals_abs_x()
