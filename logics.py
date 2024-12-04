import random

def start():
    mat=[[0]*4 for i in range(4)]
    return mat

def add_new_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while(mat[r][c]!=0):
        r=random.randint(0,3)
        c=random.randint(0,3) 
    mat[r][c]=2

def reverse(mat):
    new_mat=[[0]*4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[i][j]=mat[i][3-j]
    return new_mat

def transpose(mat):
    new_mat=[[0]*4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[i][j]=mat[j][i]
    return new_mat

def merge(mat):
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1]:
                mat[i][j]=2*mat[i][j]
                mat[i][j+1]=0

def compress(mat):
    new_mat=[[0]*4 for i in range(4)]
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                pos+=1
    for i in range(4):
        for j in range(4):
            mat[i][j]=new_mat[i][j]

def left(mat):
    compress(mat)
    merge(mat)
    compress(mat) 
    return mat

def right(mat):
    a=reverse(mat)
    compress(a)
    merge(a)
    compress(a)
    b=reverse(a)
    return b

def up(mat):
    a=transpose(mat)
    compress(a)
    merge(a)
    compress(a)
    b=transpose(a)
    return b

def down(mat):
    a=transpose(mat)
    b=reverse(a)
    compress(b)
    merge(b)
    compress(b)
    c=reverse(b)
    d=transpose(c)
    return d

def get_current_state(mat):
    #checking anywhere 2048 is present.
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return "WON" 
    #checking anywhere 0 is present.     
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return "GAME NOT OVER"
    #checking if adjacent numbers are same in every row and column except last row and column.
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i][j+1]:
                return "GAME NOT OVER"    
    #checking if adjacent numbers are same in last row.
    for i in range(3):
        if mat[3][i]==mat[3][i+1]:
            return "GAME NOT OVER"  
    #checking if adjacent numbers are same in last column.    
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return "GAME NOT OVER"
    #if none of the above conditions are possible.    
    return "LOST"