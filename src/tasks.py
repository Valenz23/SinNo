from invoke import task

@task
def ayuda(c):
    print("Menú de ayuda:")
    print(" * inv ayuda: muestra este menú")
    print(" * inv test: realiza todos los test")
    print(" * inv apitest: realiza todos los test de la api")

@task
def test(c):
    c.run("python -m unittest -v")

@task
def apitest(c):
    # c.run("cd api && python -m unittest -v")
    c.run("python -m unittest api/test_sonder_api.py -v")
    