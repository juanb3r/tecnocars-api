from sqlalchemy.orm import sessionmaker
from process.models import engine

Session = sessionmaker(bind=engine)
session = Session()
