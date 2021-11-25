from sqlalchemy import Boolean, Column,\
    Integer, String, Date
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


class Client(Base):
    __tablename__ = "revisiones"

    id = Column(Integer, primary_key=True, index=True)
    empresa = Column(String, unique=True, index=True)
    placa_empresa = Column("placaEmpresa", String, index=True)
    placa = Column(String, index=True)
    bimensual = Column(Date)
    soat = Column(Date)
    tecnomecanica = Column(Date)
    poliza = Column(Date)
    archivo = Column(String)
    archivo_2 = Column("archivo2", String)
    fecha_registro = Column(Date)
    aprobado = Column(Boolean, default=False)


engine = create_engine("sqlite:///tecnocars.db")
Base.metadata.create_all(engine)
