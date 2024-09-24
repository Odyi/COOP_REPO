# back_end.py
from currency_converter import CurrencyConverter
from datetime import datetime


def evaluate_expression(expression):
    """Evaluerer et matematisk uttrykk og returnerer resultatet."""
    try:
        # Basically regner ut alt for deg
        resultat = eval(expression)
        return resultat
    except (SyntaxError, NameError, ZeroDivisionError) as e:
        # Returnerer feilmeldingen hvis det er en feil i uttrykket
        return f"*** Ugyldig uttrykk: {e} ***"


def convert_currency():
    # Initialize the converter
    c = CurrencyConverter()
    
    try:
        # Get user inputs
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the source currency code (e.g., USD, EUR): ").upper()
        to_currency = input("Enter the target currency code (e.g., USD, EUR): ").upper()
        converted_amount = c.convert(amount, from_currency, to_currency)
        
        print(f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}")

    except ValueError:
        print("Invalid input. Please enter valid numbers and date format.")
    except Exception as e:
        print(f"Error: {e}")
