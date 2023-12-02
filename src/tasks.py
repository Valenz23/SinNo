from invoke import task

@task
def ayuda(c):
    print("Menú de ayuda:")
    print(" * inv ayuda: muestra este menú")
    print(" * inv test: realiza todos los test")

@task
def test(c):
    c.run("python -m unittest -v")
    