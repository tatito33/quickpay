from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Establecimiento(Base):
    __tablename__ = "establecimientos"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    direccion = Column(String(200))
    telefono = Column(String(20))
    
    mesas = relationship("Mesa", back_populates="establecimiento")

class Mesa(Base):
    __tablename__ = "mesas"
    
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(Integer)
    codigo_qr = Column(String(200))
    establecimiento_id = Column(Integer, ForeignKey("establecimientos.id"))
    
    establecimiento = relationship("Establecimiento", back_populates="mesas")
    cuentas = relationship("Cuenta", back_populates="mesa")

class Cuenta(Base):
    __tablename__ = "cuentas"
    
    id = Column(Integer, primary_key=True, index=True)
    mesa_id = Column(Integer, ForeignKey("mesas.id"))
    total = Column(Float)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    estado = Column(String(20), default="abierta")
    
    mesa = relationship("Mesa", back_populates="cuentas")
    consumiciones = relationship("Consumicion", back_populates="cuenta")

class Consumicion(Base):
    __tablename__ = "consumiciones"
    
    id = Column(Integer, primary_key=True, index=True)
    cuenta_id = Column(Integer, ForeignKey("cuentas.id"))
    producto = Column(String(100))
    precio = Column(Float)
    cantidad = Column(Integer)
    
    cuenta = relationship("Cuenta", back_populates="consumiciones")