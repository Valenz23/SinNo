
# cualquier usuario podrá buscar una canción
def buscarCancion(algo):

    #buscar cancion usando "algo"

    # buscar la cancion en una lista


    cancion = algo

    return cancion

# usuario ya logueado
class usuario:

    ID = '' 
    tipo = ''
    nick = ''
    password = ''

    def __init__(self,nick,password) -> None:
        self.ID = 12345
        self.tipo = 1
        self.nick = nick
        self.password = password