import click

@click.group()
def cli():
    """Tenant commands"""
    pass

@cli.command()
def add_tenant():
    """Add a new tenant"""
    click.echo("New tenant added!")
