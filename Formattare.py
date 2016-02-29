# 2 metodi diversi per formattare output
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
 
print('___________')
print()  
    
for y in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(y, y*y, y*y*y))