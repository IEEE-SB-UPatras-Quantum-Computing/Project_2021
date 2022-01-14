from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from .Algorithm import Protocol

class Superdense_Protocol(Protocol):
    """Alice = Sender q[1] \n Bob = Reciever q[0]"""
    
    def create_circuit(self):
        self.q = QuantumRegister(2,"q") # quantum register with 2 qubits
        self.c = ClassicalRegister(2,"c") # classical register with 2 bits
        self.qc = QuantumCircuit(self.q, self.c) # quantum circuit with quantum and classical registers

        self.initializeBellPair(self.q[0], self.q[1])
        self.encodeQbits(self.q[1], "00")
        self.sendQbit()
        self.decodeQbits(self.q[0], self.q[1])
    
    def initializeBellPair(self, q0, q1):
        self.qc.h(q1) # apply h-gate to the Alice's qubit
        self.qc.cx(q1, q0) # apply cx-gate to Alice's qubit, controlled by Bob's qubit
    
    ### PROBLEM WITH q: slef.q or self.q[1]?
    def encodeQbits(self, q, data="00"):
        # if a is 1, then apply z-gate to Alice's qubit
        if data[0]=='1':
            self.qc.z(q)

        # if b is 1, then apply x-gate to Alice's qubit
        if data[1]=='1':
            self.qc.x(self.q)
    
    def sendQbit(self):
        self.qc.barrier() # Alice sends her qubit to Bob
    
    def decodeQbits(self, q0, q1):
        self.qc.cx(q1, q0) #  apply cx-gate to Alice's qubit, controlled by Bob's qubit
        self.qc.h(q1) # apply h-gate to the Alice's qubit

