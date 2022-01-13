#import numpy as np
#from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer, IBMQ
#from qiskit.circuit import Gate
from .Algorithms import Protocol

class SuperdenseCode:
    # Alice = Sender q[1]
    # Bob = Reciever q[0]
    def __init__(self):
        super().__init__()
        self.q = 0
        self.c = 0
        self.qc = 0
        self.create_circuit()
    def run(self, data):
        
        self.initializeBellPair(self.q[0], self.q[1], self.qc)
 
        self.encodeQbits(data, self.q[1], self.qc)
        
        self.sendQbit(self.qc)
        
        self.decodeQbits(self.q[0], self.q[1], self.qc)

#        self.drawCircuit(self.qc)
#        
#        self.measureQbits(self.q, self.c, self.qc)
#        
#        self.measureResults(self.qc, data)
        
    def create_circuit(self):
        self.q = QuantumRegister(2,"q") # quantum register with 2 qubits
        self.c = ClassicalRegister(2,"c") # classical register with 2 bits
        self.qc = QuantumCircuit(self.q, self.c) # quantum circuit with quantum and classical registers
        
        data = "00"
        self.run(data)
        
    def initializeBellPair(self, q0, q1, qc):
        # apply h-gate to the Alice's qubit
        qc.h(q1)

        # apply cx-gate to Alice's qubit, controlled by Bob's qubit
        qc.cx(q1, q0)
        
    def encodeQbits(self, data, q, qc):
        # if a is 1, then apply z-gate to Alice's qubit
        if data[0]=='1':
            qc.z(q)
    
        # if b is 1, then apply x-gate to Alice's qubit
        if data[1]=='1':
            self.qc.x(self.q)
    
    def sendQbit(self, qc):
        # Alice sends her qubit to Bob
        qc.barrier()
    
    def decodeQbits(self, q0, q1, qc):
        #  apply cx-gate to Alice's qubit, controlled by Bob's qubit
        qc.cx(q1, q0)
    
        # apply h-gate to the Alice's qubit
        qc.h(q1)
  
        
    def drawCircuit(self, qc):
        # draw the circuit in Qiskit's reading order
        display(qc.draw(output='mpl',reverse_bits=True))
        
    def measureQbits(self, q, c, qc):
        # measure both qubits
        self.qc.measure(self.q,self.c)
       
    def measureResults(self, qc, data):
        # compare the results with pair (a,b)
        job = execute(qc,Aer.get_backend('qasm_simulator'),shots=100)
        counts = job.result().get_counts(qc)
        print(data,"--->",counts)
