import unittest
from src.services.payment_factory import PaymentFactory

class TestPayments(unittest.TestCase):

    def test_mpesa_service(self):
        service = PaymentFactory.get_service('mpesa')
        # Add test cases for Mpesa service
        self.assertTrue(service is not None)

    def test_paypal_service(self):
        service = PaymentFactory.get_service('paypal')
        # Add test cases for Paypal service
        self.assertTrue(service is not None)

    def test_stripe_service(self):
        service = PaymentFactory.get_service('stripe')
        # Add test cases for Stripe service
        self.assertTrue(service is not None)

if __name__ == '__main__':
    unittest.main()
