#add implementation
from distutils.log import error


def add(x,y):
    return (x+y)
#subtract implementation
def substract(x,y):
    return x-y #on master branch
#multiply implementation
def multiply(x,y):
    return x*y 
#divide implementation
def divide(x,y):
    if y==0:
        return error
    else :
        return x/y  #on master branch
        
