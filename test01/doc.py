# Forma de documentar en python

def calcPadding(width,pixeles):
    """Este es un comentario dentro de la funcion que describe lo que
        debe de hacer o como hacerlo, es utili recordar comentar las cosas."""
    return width - (pixeles*4)


# Imprimimos la documentacion de la funcion
print(calcPadding.__doc__)
help(calcPadding)
