#!/usr/bin/python3
'''Module to generate Pascal's triangle'''

def pascal_triangle(n):
    '''
    Generate Pascal's triangle
    Args:
      n (int): Number of rows in the triangle
    Returns:
      List of lists representing Pascal’s triangle
    '''
    lists = []
    if n == 0:
        return lists
    for i in range(n):
        lists.append([])
        lists[i].append(1)
        if i > 0:
            for j in range(1, i):
                lists[i].append(lists[i - 1][j - 1] + lists[i - 1][j])
            lists[i].append(1)
    return lists
