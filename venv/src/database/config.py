from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco de dados (no caso, usando SQLite)
DATABASE_URL = "sqlite:///presenca.db"  

# Criar o motor (engine) de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# Criar uma classe de sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base para o mapeamento de tabelas
Base = declarative_base()
