#Problem
There is a program which encode two float inputs. Write a program that decode the
output of the program given in problem and print the main initial input. 
#Tasks
##The encoding program
The program of the problem is coded like below:
```
dx = float(input('Enter original x in float format: '))
dy = float(input('Enter original y in float format: '))
dxi = int(dx)
dyi = int(dy)
dxj = str(dx-dxi)
dyj = str(dy-dyi)
enx = str(dxi**2-7)
eny = str(dyi**3-6)
print('Encrypted x is: '+' '+enx+'.'+dxj)
print('Encrypted y is: '+' '+eny+'.'+dyj)
```
##An example
The answer to this problem should be able to return the correct x as 10.2
where the coded x is 93.0.1999999996.
