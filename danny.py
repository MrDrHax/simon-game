#función 1:

def regresar_valor(valor, lista, x):
    if (not x<len(lista)):
        return True
    if valor==lista[x]:
        return False
    else:
        return True

#función 2:
    
def estop(x, lista):
    if x+1==len(lista):
        return True
    else:
        return False