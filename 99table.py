for j in range(1, 10):
    for i in range(1, j+1):
        print('{}x{}={}\t'.format(i, j, i*j), end='')
    print()
