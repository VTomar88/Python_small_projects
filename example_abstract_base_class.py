"""
Abstract Base Classes (ABC) 
ABC are relevant when we want to enforce a consistent interface
or behaviour acrosss multiple classes.
This is example for a payement system where all payment gateways must implement certain
methods like 'authenticate' and 'process_payment'.
"""

from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    """
    Abstract Base Class for payment gateways.

    Defines the blueprint for payment gateway subclasses, requiring them to implement:
    - authenticate: Method to authenticate a user.
    - process_payment: Method to process a payment.
    """

    @abstractmethod
    def authenticate(self):
        """
        Authenticate the user for the payment gateway.
        Must be implemented by all subclasses.
        """
        pass

    @abstractmethod
    def process_payment(self):
        """
        Process a payment with the specified amount.
        Must be implemented by all subclasses.

        Args:
            amount (float): The amount to be processed.
        """
        pass


class PayPal(PaymentGateway):
    """
    Concrete implementation of the PaymentGateway class for PayPal.
    """

    def authenticate(self):
        """
        Authenticate a PayPal user.
        """
        print("AUthenticating PayPal user.")

    def process_payment(self, amount):
        """
        Process a payment through PayPal.

        Args:
            amount (float): The amount to be processed.
        """
        print(f"Processing payment of ${amount} via PayPal.")


class Stripe(PaymentGateway):
    """
    Implementation of the PaymentGateway class for Stripe.
    """

    def authenticate(self):
        """
        Authenticate a Stripe user.
        """
        print("AUthenticating Stripe user.")

    def process_payment(self, amount):
        """
        Process a payment through Stripe.

        Args:
            amount (float): The amount to be processed.
        """
        print(f"Processing payment of ${amount} via Stripe.")


def process_all_payments(gateways, amount):
    """
    Process payments for all provided gateways.

    Iterates over a list of payment gateways, authenticates each, and processes
    the specified payment amount.

    Args:
        gateways (list[PaymentGateway]): A list of payment gateway instances.
        amount (float): The amount to be processed through each gateway.
    """
    for gateway in gateways:
        # Authenticate the user for the gateway
        gateway.authenticate()
        # Process the payment with the specified amount
        gateway.process_payment(amount)


# Usage
gateways = [PayPal(), Stripe()]
process_all_payments(gateways, 100)
