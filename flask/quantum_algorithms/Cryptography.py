from qiskit.circuit import Gate
from .Algorithm import Protocol

class Cryptography_Protocol(Protocol):
    # def __init__(self, save_folder, q_num):
    #     super().__init__(save_folder, 1)
    
    def create_circuit(self):
        self.qc.h(self.qc.qubits)
        self.qc.cx(0, self.q_num-1)

        # self.qc.append(Gate("Alice",1,[]), self.qc.qregs)

        # self.qc.h(0) # if i==0 else qc.i(0)
        # self.qc.barrier() # Loooooong distance
        # self.qc.barrier() # Loooooong distance
        # self.qc.h(0) # if j==0 else qc.i(0)
        
        # self.qc.append(Gate("Bob",1,[]), self.qc.qregs)


