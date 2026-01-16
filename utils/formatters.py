from datetime import date


def format_currency(amount: float) -> str:
    return f"{amount:,.0f} F CFA".replace(",", " ")


def format_number(amount: float) -> str:
    return f"{amount:,.0f}".replace(",", " ")


def format_date(dt: date) -> str:
    return dt.strftime("%d/%m/%Y")
