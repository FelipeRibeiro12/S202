from corrida import *
from motorista import *
from passageiro import *
from motoristaDAO import MotoristaDAO
from motoristaCLI import MotoristaCLI

dao = MotoristaDAO()

motoristaCLI = MotoristaCLI(dao)
motoristaCLI.run()
