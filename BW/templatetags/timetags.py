import datetime
from django import template
import locale

register = template.Library()

# Ustawienie polskiego języka dla formatowania
try:
    locale.setlocale(locale.LC_TIME, 'pl_PL.UTF-8')  # lub 'pl_PL' zależnie od systemu
except locale.Error:
    print("Nie udało się ustawić lokalizacji na polski. Używany jest domyślny format.")

def print_timestamp(timestamp, format_type="YMD"):
    """
    Funkcja przetwarza znacznik czasu na format daty.
    Parametr format_type pozwala wybrać format: "YMD" dla YYYY-MM-DD lub "PL" dla polskiego formatu.
    """
    try:
        ts = float(timestamp)
        date_obj = datetime.datetime.fromtimestamp(ts)
    except (ValueError, TypeError):
        return None

    if format_type == "PL":
        return date_obj.strftime('%d.%m.%Y')  # Format polski DD.MM.YYYY
    else:
        return date_obj.strftime('%d-%m-%Y, %H:%M')  # Format YYYY-MM-DD

register.filter("print_timestamp", print_timestamp)