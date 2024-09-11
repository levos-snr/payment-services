import click

@click.group()
def cli():
    """Admin commands"""
    pass

@cli.command()
def create_admin():
    """Create an admin user"""
    click.echo("Admin user created!")
