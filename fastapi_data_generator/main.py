from fastapi import FastAPI
import requests
import random
import time
import threading

app = FastAPI()

def generate_data():
    while True:
        payload = {
            "id": "urn:ngsi-ld:Room:001",
            "type": "Room",
            "temperature": {"value": round(random.uniform(20, 30), 2), "type": "Number"},
            "humidity": {"value": round(random.uniform(30, 70), 2), "type": "Number"},
            "occupancy": {"value": random.randint(0, 10), "type": "Integer"}
        }

        headers = {"Content-Type": "application/json"}
        try:
            requests.post("http://orion:1026/v2/entities", json=payload, headers=headers)
        except Exception as e:
            print("Erreur d'envoi vers Orion:", e)
        time.sleep(5)

@app.on_event("startup")
def start_simulation():
    thread = threading.Thread(target=generate_data)
    thread.start()

@app.get("/")
def root():
    return {"message": "Data generator for Smart Building running"}
