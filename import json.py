import json
import os

def order_naar_factuur(order_json):
    """
    Zet een order JSON om naar een factuur JSON met extra berekeningen.
    """
    klant = order_json.get("klant", {})
    producten = order_json.get("producten", [])

    totaal_bedrag = 0
    factuur_items = []

    for product in producten:
        prijs_per_stuk = product.get("prijs_per_stuk", 0)
        hoeveelheid = product.get("hoeveelheid", 0)
        totaal_product = prijs_per_stuk * hoeveelheid
        totaal_bedrag += totaal_product

        factuur_items.append({
            "product_id": product.get("product_id", ""),
            "naam": product.get("naam", "Onbekend product"),
            "hoeveelheid": hoeveelheid,
            "prijs_per_stuk": prijs_per_stuk,
            "totaal_product": totaal_product
        })

    btw = totaal_bedrag * 0.21
    te_betalen = totaal_bedrag + btw

    factuur = {
        "factuur_id": f"F{order_json.get('order_id', '00000')}",
        "klant": klant,
        "factuur_regels": factuur_items,
        "totaal_bedrag": round(totaal_bedrag, 2),
        "BTW": round(btw, 2),
        "te_betalen": round(te_betalen, 2)
    }

    return factuur

# Dummy order JSON
order_json = {
    "order_id": "12345",
    "klant": {
        "naam": "Jan Jansen",
        "adres": "Straatnaam 1, 1234 AB, Stad",
        "email": "jan@example.com"
    },
    "producten": [
        {"product_id": "A123", "naam": "Product A", "hoeveelheid": 2, "prijs_per_stuk": 10.00},
        {"product_id": "B456", "naam": "Product B", "hoeveelheid": 1, "prijs_per_stuk": 20.00}
    ]
}

# Factuur genereren
factuur_json = order_naar_factuur(order_json)

# Opslaan in map PDF_INVOICE
output_folder = "PDF_INVOICE"
os.makedirs(output_folder, exist_ok=True)
factuur_pad = os.path.join(output_folder, "factuur.json")

with open(factuur_pad, "w") as f:
    json.dump(factuur_json, f, indent=4)

print(f"Factuur JSON bestand is aangemaakt: {factuur_pad}")
os.makedirs(output_folder, exist_ok=True)
os.startfile(factuur_pad)
