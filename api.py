from typing import Union
from fastapi import FastAPI
from google.cloud import firestore
import os

# Setzen Sie die Umgebungsvariable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/pfad/zu/ihrem/servicekonto-schluessel.json"

app = FastAPI()

# Erstellen Sie eine Firestore-Instanz
db = firestore.Client()

@app.get("/search/{query}")
def search(query: str):
    # Erstellen Sie eine Referenz zur Sammlung
    collection_ref = db.collection('insolvenzen')

    # Suchen Sie nach Dokumenten, die den Suchbegriff enthalten
    name_results = collection_ref.where('Schuldner Name', '==', query).stream()
    aktenzeichen_results = collection_ref.where('Aktenzeichen', '==', query).stream()

    # Konvertieren Sie die Ergebnisse in eine Liste von Dictionaries
    results = [doc.to_dict() for doc in name_results] + [doc.to_dict() for doc in aktenzeichen_results]

    return {"results": results}
