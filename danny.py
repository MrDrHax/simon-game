#función 1:

def regresar_valor(valor, lista, x):
    # regresa el valor de True si preciono el correcto, False si no 
    if (not x<len(lista)):
        return True
    if valor==lista[x]:
        return False
    else:
        return True

#función 2:
    
def estop(x, lista):
    # regresa el valor True si es necesario parar
    if x+1==len(lista):
        return True
    else:
        return False