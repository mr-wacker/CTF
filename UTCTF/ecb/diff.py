a = open('a','r')
b = open('b','r')

a_line = a.readline()
b_line = b.readline()

print(a_line)
print(b_line)

for i in range(len(a_line)):
    if a_line[i] != b_line[i]:
        print(a_line[i],end='')
    else:
        print("*",end='')


'''
b08a5a4f4dac225666fb7966352ccb04 =a
3a0c61082d0f75e029f59629193eeb59 =b
f3d44b68ea8da5bd7dd0902c9b4acc3d =c
'''