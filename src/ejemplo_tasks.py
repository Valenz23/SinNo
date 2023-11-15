from invoke import task

@task
def clean_html(c):
    print("Cleaning HTML")

@task
def clean_tgz(c):
    print("Cleaning .tar.gz files")

@task(clean_html, clean_tgz)
def clean(c):
    print("Cleaned everything")

@task
def makedirs(c):
    print("Making directories")

@task(clean, makedirs)
def build(c):
    print("Building")

@task(build)
def deploy(c):
    print("Deploying")