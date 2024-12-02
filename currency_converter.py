"""
Currency Converter

This script allows users to convert an amount between USD, EUR, and CAD
using predefined exchange rates. The user inputs the amount, selects the 
source and target currencies, and the script calculates and displays the 
converted amount.

Features:
    - Input validation for amounts and currency codes.
    - Conversion based on a predefined exchange rate dictionary.
"""

# Exchange rate dictionary
EXCHANGE_RATES = {
    'USD': {'EUR': 0.9502, 'CAD': 1.4036},
    'EUR': {'USD': 1.0526, 'CAD': 1.4772},
    'CAD': {'USD': 0.7125, 'EUR': 0.677}
}


def get_amount():
    """
    Prompt the user to enter a valid amount.

    Returns:
        float: The amount to convert, which must be positive.
    """
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0.0:
                raise ValueError()
            return amount
        except ValueError:
            print("Invalid amount! Please enter a positive non-zero amount.")


def get_currency_choice():
    """
    Prompt the user to select source and target currencies.

    Returns:
        tuple: A tuple containing the source currency and target currency codes.
    """
    valid_currencies = tuple(EXCHANGE_RATES.keys())
    print(f"Available currencies: {', '.join(valid_currencies)}")

    while True:
        source_currency = input("Source currency (USD/EUR/CAD): ").upper()
        target_currency = input("Target currency (USD/EUR/CAD): ").upper()

        if source_currency in valid_currencies and target_currency in valid_currencies:
            if source_currency != target_currency:
                return source_currency, target_currency
            else:
                print("Source and target currencies must be different.")
        else:
            print("Invalid currency code! Please select from the available options.")


def convert_currency(source, target, amount):
    """
    Convert the amount from the source currency to the target currency.

    Args:
        source (str): The source currency code.
        target (str): The target currency code.
        amount (float): The amount in the source currency.

    Returns:
        float: The converted amount in the target currency.
    """
    return amount * EXCHANGE_RATES[source][target]


def main():
    """
    Main function to run the currency converter.

    - Prompts the user for an amount.
    - Prompts for source and target currencies.
    - Calculates and displays the converted amount.
    """
    print("Welcome to the Currency Converter!")
    user_amount = get_amount()  # Get the amount from the user
    # Get source and target currencies
    source_currency, target_currency = get_currency_choice()
    converted_amount = convert_currency(
        source_currency, target_currency, user_amount)  # Perform conversion

    print(f"{user_amount:.2f} {source_currency} is equal to {converted_amount:.2f} {target_currency}.")


if __name__ == '__main__':
    main()
