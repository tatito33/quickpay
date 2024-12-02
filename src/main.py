from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import qrcode
import stripe

from . import models, schemas, crud
from .database import engine, get_db

# Configurar Stripe
stripe.api_key = "tu_clave_stripe"

app = FastAPI()

@app.post("/generar_qr/")
def generar_qr(
    establecimiento_id: int, 
    mesa_numero: int, 
    db: Session = Depends(get_db)
):
    # Lógica generación QR
    mesa = crud.crear_mesa(
        db, 
        establecimiento_id, 
        mesa_numero
    )
    
    # Generar QR
    qr = qrcode.QRCode()
    qr.add_data(f"/cuenta/{mesa.id}")
    qr.make()
    
    return {"qr": qr.make_image()}

@app.get("/cuenta/{mesa_id}")
def obtener_cuenta(
    mesa_id: int, 
    db: Session = Depends(get_db)
):
    cuenta = crud.obtener_cuenta_mesa(db, mesa_id)
    return cuenta