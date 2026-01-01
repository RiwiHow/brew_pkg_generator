import typer

from cask_generator import generator_from_file, generator_from_url

app = typer.Typer(no_args_is_help=True)


@app.command()
def url():
    generator_from_url()


@app.command()
def file():
    generator_from_file()


if __name__ == "__main__":
    app()
