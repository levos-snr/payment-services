from src.services.mpesa_service import MpesaService
from src.services.paypal_service import PaypalService
from src.services.stripe_service import StripeService

class PaymentFactory:
    @staticmethod
    def get_service(provider_name: str):
        if provider_name == 'mpesa':
            return MpesaService()
        elif provider_name == 'paypal':
            return PaypalService()
        elif provider_name == 'stripe':
            return StripeService()
        else:
            raise ValueError(f"Unknown payment provider: {provider_name}")
