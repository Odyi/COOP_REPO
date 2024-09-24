# back_end.py

def evaluate_expression(expression):
    """Evaluerer et matematisk uttrykk og returnerer resultatet."""
    try:
        # Evaluerer uttrykket
        resultat = eval(expression)
        return resultat
    except (SyntaxError, NameError, ZeroDivisionError) as e:
        # Returnerer feilmeldingen hvis det er en feil i uttrykket
        return f"*** Ugyldig uttrykk: {e} ***"
