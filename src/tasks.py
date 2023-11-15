from invoke import task

@task
def help(c):
    print("Menú de ayuda:")
    print(" * inv help: muestra este menú")
    print(" * inv test -n songs: realiza el test de canciones")
    print(" * inv test -n users: realiza el test de usuarios")
    print(" * inv test -n liked: realiza el test de listas")
    print(" * inv test -n batchs: realiza el test de lotes")
    print(" * inv test -n all: realiza todos los tests")

@task
def test(c, name=""):

    if name == "songs": 
        c.run("python ./tests/test_songs.py -v")

    elif name == "users": 
        c.run("python ./tests/test_users.py -v")

    elif name == "liked": 
        c.run("python ./tests/test_liked_list.py -v")

    elif name == "batchs":
        c.run("python ./tests/test_bacths.py -v")
   
    elif name == "all":
        c.run("python ./tests/test_songs.py -v")
        c.run("python ./tests/test_users.py -v")
        c.run("python ./tests/test_liked_list.py -v")
        c.run("python ./tests/test_batchs.py -v")
    else:
        print("Error: pruebe a decir 'inv help'")
    
