def func_table(exp, x, y):
    res = [[eval(exp.replace('x', str(i)).replace('y', str(j))) for j in range(y + 1)] for i in range(x + 1)]
    [print(*i, sep='\t') for i in res]


