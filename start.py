import os
from PIL import Image
import pytesseract
import pandas as pd

# Pfad zu Tesseract auf deinem System (falls nötig, anpassen)
# Beispiel für Windows: pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Funktion, um Text aus einem Bild zu extrahieren
def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Fehler beim Extrahieren des Textes aus {image_path}: {e}")
        return ""

# Funktion, um Text aus allen Bildern in einem Ordner zu extrahieren
def extract_text_from_folder(folder_path):
    extracted_texts = []
    for filename in os.listdir(folder_path):
        if filename.endswith((".png", ".jpg", ".jpeg")):  # Dateitypen anpassen, falls nötig
            image_path = os.path.join(folder_path, filename)
            text = extract_text_from_image(image_path)
            extracted_texts.append([filename, text])
            print(f"Text aus {filename} extrahiert.")
    return extracted_texts

# Beispiel für die Verwendung
if __name__ == "__main__":
    folder_path = "./images"  # Pfad zum Ordner mit den Bildern
    texts = extract_text_from_folder(folder_path)
    
    # Speichere die extrahierten Texte in eine Excel-Datei mit zwei Spalten
    df = pd.DataFrame(texts, columns=["Dateiname", "Extrahierter Text"])
    df.to_excel("extracted_texts.xlsx", index=False)
    
    print("Textextraktion abgeschlossen und in Excel gespeichert!")
