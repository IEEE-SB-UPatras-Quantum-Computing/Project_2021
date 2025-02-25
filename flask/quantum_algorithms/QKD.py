from qiskit import QuantumCircuit
from .Algorithm import Protocol

class QKD_Protocol(Protocol):
    def __init__(self, save_folder):
        self.conditions = "00"
        super().__init__(save_folder)
    
    def initialize_circuit(self):
        self.qc = QuantumCircuit(1)
    
    def create_circuit(self):
        # self.qc.append(Gate("Alice",1,[]), self.qc.qregs)

        self.qc.h(0) if self.conditions[0]==0 else self.qc.id(0) # Alice's conditional bit
        self.qc.barrier() # Loooooong distance
        self.qc.barrier() # Loooooong distance
        self.qc.h(0) if self.conditions[1]==0 else self.qc.id(0) # Bob's conditional bit
        
        # self.qc.append(Gate("Bob",1,[]), self.qc.qregs)
