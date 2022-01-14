from qiskit.circuit import Gate
from .Algorithm import Protocol

class Cryptography_Protocol(Protocol):
    
    def create_circuit(self):
        # self.qc.append(Gate("Alice",1,[]), self.qc.qregs)

        for i in range(2):
            for j in range(2):
                self.qc.h(0) if i==0 else self.qc.i(0)
                self.qc.barrier() # Loooooong distance
                self.qc.barrier() # Loooooong distance
                self.qc.h(0) if j==0 else self.qc.i(0)
                self.qc.barrier()
        
        # self.qc.append(Gate("Bob",1,[]), self.qc.qregs)


