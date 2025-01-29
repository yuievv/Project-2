from fpdf import FPDF
import json

# Laad de JSON gegevens (dit zou je normaal uit een bestand lezen)
factuur_data = {
    "factuurnummer": "12345",
    "datum": "2025-01-29",
    "klant": {
        "naam": "John Doe",
        "adres": "Straatnaam 123",
        "stad": "Amsterdam"
    },
    "producten": [
        {"omschrijving": "Product 1", "prijs": 10.00, "aantal": 2},
        {"omschrijving": "Product 2", "prijs": 20.00, "aantal": 1}
    ],
    "totaal": 40.00
}

# Maak een nieuwe PDF aan
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Stel lettertype en grootte in
pdf.set_font("Arial", size=12)

# Voeg de factuurnummer en datum toe
pdf.cell(200, 10, txt=f"Factuurnummer: {factuur_data['factuurnummer']}", ln=True)
pdf.cell(200, 10, txt=f"Datum: {factuur_data['datum']}", ln=True)
pdf.ln(10)  # Voeg een lege regel toe

# Voeg klantgegevens toe
pdf.cell(200, 10, txt=f"Klant: {factuur_data['klant']['naam']}", ln=True)
pdf.cell(200, 10, txt=f"Adres: {factuur_data['klant']['adres']}", ln=True)
pdf.cell(200, 10, txt=f"Stad: {factuur_data['klant']['stad']}", ln=True)
pdf.ln(10)

# Voeg de producten toe
pdf.cell(200, 10, txt="Producten:", ln=True)
pdf.cell(50, 10, txt="Omschrijving", border=1)
pdf.cell(30, 10, txt="Aantal", border=1)
pdf.cell(30, 10, txt="Prijs", border=1)
pdf.cell(30, 10, txt="Totaal", border=1)
pdf.ln(10)

for product in factuur_data['producten']:
    totaal_product = product['prijs'] * product['aantal']
    pdf.cell(50, 10, txt=product['omschrijving'], border=1)
    pdf.cell(30, 10, txt=str(product['aantal']), border=1)
    pdf.cell(30, 10, txt=f"{product['prijs']} EUR", border=1)
    pdf.cell(30, 10, txt=f"{totaal_product} EUR", border=1)
    pdf.ln(10)

# Voeg het totaal toe
pdf.cell(200, 10, txt=f"Totaal te betalen: {factuur_data['totaal']} EUR", ln=True)

# Opslaan van de PDF
pdf.output("factuur.pdf")

print("Factuur is succesvol gegenereerd!")

