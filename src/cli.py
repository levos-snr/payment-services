import click
from src.commands import admin, tenant, payments

@click.group()
def cli():
    """Payment Service CLI"""
    pass

cli.add_command(admin.cli)
cli.add_command(tenant.cli)
cli.add_command(payments.cli)

if __name__ == '__main__':
    cli()
