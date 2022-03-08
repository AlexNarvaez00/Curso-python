# Lanzaremos una exception 
def setPort(numberPort) : 
    if numberPort > 0 : 
        return True
    else:
        # raise -> Lanza la excepcion 
        raise ValueError('Valor de puerto no perimitido')


print(setPort(-20))