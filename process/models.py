from sqlalchemy import Boolean, Column,\
    Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()


class Users(Base):
    __tablename__ = "usuariotabla"

    id = Column(Integer, primary_key=True, index=True)
    name = Column("nombre", String)
    username = Column("usuario", String, unique=True)
    password = Column(String)
    access = Column("permisos", Boolean, default=False)


class Client():
    __tablename__ = "revisiones"

    id = Column(Integer, primary_key=True, index=True)
    empresa = Column(String, index=True)
    placa_empresa = Column("placaEmpresa", String, index=True)
    placa = Column(String, index=True)
    bimensual = Column(Date)
    soat = Column(Date)
    tecnomecanica = Column(Date)
    poliza = Column(Date)
    bimensual = Column(Date)
    archivo = Column(Date)
    archivo2 = Column(Date)
    fecha_registro = Column(DateTime)
    aprobado = Column(Boolean, default=False)


engine = create_engine("sqlite:///tecnocars.db", echo=True)
Base.metadata.create_all(engine)
