from .Algorithm import Protocol

class Teleportation_Protocol(Protocol):
    def create_circuit(self):
        self.qc.h(self.qc.qubits)
        self.qc.y(0)
        self.qc.z(1)
        self.qc.x(self.q_num-1)
