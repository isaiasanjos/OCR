from sqlalchemy import Column, Integer, String, Date
from database.config import Base, engine
from datetime import date

class Presenca(Base):
    __tablename__ = 'presencas'
    
    id = Column(Integer, primary_key=True, index=True)
    nome_aluno = Column(String, index=True)
    presenca = Column(String)
    
    def __init__(self, nome_aluno, presenca):
        self.nome_aluno = nome_aluno
        self.presenca = presenca
        
Base.metadata.create_all(engine)