import click


@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def greet(count, name):
    for _ in range(count):
        click.echo(f"Hello {name}!")


@click.command()
@click.option('--name', prompt='Enter the new item')
# @click.argument('item')
def create(name=None):
    click.echo(f"Creating a new {name}!")


def run_the_counts(count, name):
    for _ in range(count):
        click.echo(f"Hello {name}")


def greeting(name):
    click.echo(f"""
               **************
               HELLO {name}!
               **************
               
               You have found a cool CLI
               """)


@click.command()
@click.option('--count', type=int, help='number of greetings')
@click.option('--name', prompt='Enter the new item')
def justatest(name=None, count=None):
    """
    
░██████╗██╗░██████╗░  ░█████╗░██╗░░░░░██╗
██╔════╝██║██╔═══██╗  ██╔══██╗██║░░░░░██║
╚█████╗░██║██║██╗██║  ██║░░╚═╝██║░░░░░██║
░╚═══██╗██║╚██████╔╝  ██║░░██╗██║░░░░░██║
██████╔╝██║░╚═██╔═╝░  ╚█████╔╝███████╗██║
╚═════╝░╚═╝░░░╚═╝░░░  ░╚════╝░╚══════╝╚═╝
    
    
    
\nSick driver code for rippin cli
    """
    if count is not None:
        run_the_counts(count, name)
    if name:
        greeting(name)


def main():
    # greet()
    # create()
    justatest()


if __name__ == '__main__':
    main()
