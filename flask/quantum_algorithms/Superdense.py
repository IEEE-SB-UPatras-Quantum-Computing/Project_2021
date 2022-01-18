from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from .Algorithm import Protocol

class Superdense_Protocol(Protocol):
    """Alice = Sender q[1] \n Bob = Reciever q[0]"""
    def __init__(self, save_folder):
        self.data = "00"
        super().__init__(save_folder)
    
    def initialize_circuit(self):
        self.q = QuantumRegister(2,"q") # quantum register with 2 qubits
        self.c = ClassicalRegister(2,"c") # classical register with 2 bits
        self.qc = QuantumCircuit(self.q, self.c) # quantum circuit with quantum and classical registers
    
    def create_circuit(self):
        self.createBellPair(self.q[0], self.q[1])
        self.encodeQbits(self.q[1])
        self.sendQbit()
        self.decodeQbits(self.q[0], self.q[1])
    
    def createBellPair(self, q0, q1):
        self.qc.h(q1) # apply h-gate to the Alice's qubit
        self.qc.cx(q1, q0) # apply cx-gate to Alice's qubit, controlled by Bob's qubit
    
    def encodeQbits(self, qubit):
        # if a is 1, then apply z-gate to Alice's qubit
        if self.data[0]=='1':
            self.qc.z(qubit)
        
        # if b is 1, then apply x-gate to Alice's qubit
        if self.data[1]=='1':
            self.qc.x(qubit)
    
    def sendQbit(self):
        self.qc.barrier() # Alice sends her qubit to Bob
    
    def decodeQbits(self, q0, q1):
        self.qc.cx(q1, q0) #  apply cx-gate to Alice's qubit, controlled by Bob's qubit
        self.qc.h(q1) # apply h-gate to the Alice's qubit

