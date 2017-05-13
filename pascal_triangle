def print_pascal(n):
    """
    Prints not centered pascal triangle.
    """
    def pascal_triangle(n):
        if n == 2:
            return [[1, 1], [1]]
        else:
            line = [1]
            x = pascal_triangle(n-1)[0]
            for j in range(0, len(x) - 1):
                line.append(x[j]+x[j+1])
            line.append(1)
            return [line] + pascal_triangle(n - 1)
    pascal_tr = pascal_triangle(10)[::-1]
    for i in pascal_tr:
        for j in i:
            print (j, end = ' ')
        print(' ')
print_pascal(7)



    
def print_pascal2(n):
    """
    Prints centered pascal triangle.
    """
    def pascal_triangle(n):
        if n == 2:
            return [[1, 1], [1]]
        else:
            line = [1]
            x = pascal_triangle(n-1)[0]
            for j in range(0, len(x) - 1):
                line.append(x[j]+x[j+1])
            line.append(1)
            return [line] + pascal_triangle(n - 1)
    pascal_tr = pascal_triangle(10)[::-1]
    for i in pascal_tr:
        s = ''
        for j in i:
            s += str(j)
            s += ' '
        print('{:^80s}'.format(s))
print_pascal2(7)
