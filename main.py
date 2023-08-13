import docker
import subprocess

import typer

app = typer.Typer()

client = docker.from_env()

@app.command()
def create(distro : str, name : str):
    image = client.images.pull(distro)
    client.containers.run(image, detach=True, name=name, remove=True, tty=True, stdin_open=True)

@app.command()
def run(name : str):
    subprocess.call(["docker", "exec", "-it", name, "sh"])

@app.command()
def stop(name : str):
    for container in client.containers.list():
        if name == container.attrs['Name'][1:]: # remove the '/'
            container.stop()



if __name__ == "__main__":
    app()

