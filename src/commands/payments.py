import click
from src.services.payment_factory import PaymentFactory

@click.group()
def cli():
    """Payment commands"""
    pass

@cli.command()
@click.argument('provider')
def process_payment(provider):
    """Process payment using the specified provider"""
    service = PaymentFactory.get_service(provider)
    service.process_payment()
    click.echo(f"Payment processed with {provider}!")
