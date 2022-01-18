from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from math import pi
from random import randrange
from .Algorithm import Protocol

class Teleportation_Protocol(Protocol):
    def __init__(self, save_folder, theta=2*pi* randrange(100)/100):
        self.theta = theta # initial angle in radians
        super().__init__(save_folder)

    def initialize_circuit(self):
        self.alice =  QuantumRegister(2,"a")
        self.a0 = self.alice[0]
        self.a1 = self.alice[1]
        self.bob =  QuantumRegister(1,"b")
        self.b0 = self.bob[0]
        self.clscl = ClassicalRegister(3,"c")
        self.qc = QuantumCircuit(self.alice,self.bob, self.clscl)

    def create_circuit(self):
        self.qc.h([0,1,2])
        return
        self.alice_init()
        self.distriute_qubits()
        self.alice_measure()
        self.bob_side()

    def alice_init(self):
        self.qc.ry(2*self.theta, self.a0) # initialize state for Alice
        self.qc.h(self.a1)
        self.qc.cx(self.a1, self.b0)
        self.qc.barrier()
    
    def distriute_qubits(self):
        self.qc.append(QuantumCircuit(2).to_gate(label="Alice"), self.alice)
        self.qc.append(QuantumCircuit(1).to_gate(label="Bob"), self.bob)
        self.qc.barrier()

    def alice_measure(self):
        self.qc.cx(self.a0, self.a1)
        self.qc.h(self.a0)
        self.qc.measure(self.alice[0:2], self.clscl[0:2])

    def bob_side(self):
        self.qc.barrier()
        self.qc.cx(self.a1, self.b0)
        self.qc.cz(self.a0, self.b0)

