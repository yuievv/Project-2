import os
import json
import shutil


JSON_ORDER = 'path/to/JSON_ORDER'  
JSON_INVOICE = 'path/to/JSON_INVOICE'  
JSON_PROCESSED = 'path/to/JSON_PROCESSED'  


os.makedirs(JSON_INVOICE, exist_ok=True)
os.makedirs(JSON_PROCESSED, exist_ok=True)


def generate_invoice_json(order_data):
    
    factuur_data = {
        "factuurnummer": order_data["order_id"],
        "datum": order_data["datum"],  
        "klant": {
            "naam": order_data["klant"]["naam"],
            "adres": order_data["klant"]["adres"],
            "stad": order_data["klant"]["stad"]
        },
        "producten": order_data["producten"],  
        "totaal": sum([p['prijs'] * p['aantal'] for p in order_data['producten']])  
    }
    
    return factuur_data


order_bestanden = os.listdir(JSON_ORDER)


for bestand in order_bestanden:
    order_pad = os.path.join(JSON_ORDER, bestand)
    

    if os.path.isfile(order_pad) and bestand.endswith('.json'):
        with open(order_pad, 'r', encoding='utf-8') as f:
            order_data = json.load(f)
        
       
        factuur_data = generate_invoice_json(order_data)
        
        
        factuur_bestand = os.path.join(JSON_INVOICE, f"factuur_{order_data['order_id']}.json")
        with open(factuur_bestand, 'w', encoding='utf-8') as f:
            json.dump(factuur_data, f, ensure_ascii=False, indent=4)
        
        
        processed_pad = os.path.join(JSON_PROCESSED, bestand)
        shutil.move(order_pad, processed_pad)

        print(f"Factuur voor order {order_data['order_id']} gegenereerd en opgeslagen.")
        print(f"Orderbestand verplaatst naar JSON_PROCESSED.")
