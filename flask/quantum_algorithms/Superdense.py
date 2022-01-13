from .Algorithm import Protocol

class Superdense_Protocol(Protocol):
    def create_circuit(self):
        self.qc.r(3.1415,0, 0)
        self.qc.h(1)

