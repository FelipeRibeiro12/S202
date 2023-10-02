from typing import List
from corrida import *

class Motorista:

    def __init__(self, nota: int, corrida: List[Corrida]):
        self.nota = nota
        self.corrida = corrida
