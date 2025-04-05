from database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Time, Boolean
from datetime import time

class Refeicao(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    descricao: Mapped[str] = mapped_column(String(80), nullable=False)
    horario: Mapped[time] = mapped_column(Time, nullable=False)
    dentro_dieta: Mapped[bool] = mapped_column(Boolean, nullable=False)
