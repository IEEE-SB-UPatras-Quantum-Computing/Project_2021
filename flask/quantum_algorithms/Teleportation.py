from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from math import pi, cos, sin
from random import randrange
from .Algorithm import Protocol

class Teleportation_Protocol(Protocol):
    
    def create_circuit(self):
        self.alice =  QuantumRegister(2,"a")
        self.a0 = self.alice[0]
        self.a1 = self.alice[1]
        self.bob =  QuantumRegister(1,"b")
        self.b0 = self.bob[0]
        self.c = ClassicalRegister(3,"c")
        self.qc = QuantumCircuit(self.alice,self.bob, self.c)

        self.alice_init()
        self.initialize()
        self.initialize_exp()

    def alice_init(self):
        theta = 2*pi* randrange(100)/100 # random angle in radians
        self.qc.ry(2*theta, self.a0) # random state for Alice
        self.qc.h(self.a1)
        self.qc.cx(self.a1, self.b0)
    

    ##-------------------------------- INITIALIZE
    def initialize(self):
        self.simulator()
        # self.initial_state = self.job.result().get_statevector(self.qc)

        self.alice_measure()
        # self.read_statevector()
        # self.quantum_state = self.job.result().get_statevector(self.qc)

        # self.classical_register()
        self.bob_measure()
        # self.read_statevector()
        # self.final_state = self.job.result().get_statevector(self.qc)
    
    def simulator(self, sim='statevector_simulator', shots=1):
        self.job = execute(self.qc, Aer.get_backend(sim), shots=shots)
    
    def alice_measure(self):
        self.qc.cx(self.a0, self.a1)
        self.qc.h(self.a0)
        self.qc.measure(self.alice[0:2], self.c[0:2])

    def bob_measure(self):
        self.qc.cx(self.a1, self.b0)
        self.qc.cz(self.a0, self.b0)
    

    ##-------------------------------- INITIALIZE_EXP
    def initialize_exp(self):
        self.exp_circuit()
        self.exp_initialize()
        self.calculate()
        # self.classical_out()
        # self.new_quantum_state()
    
    def exp_circuit(self):
        self.q =  QuantumRegister(3,"q") 
        self.c = ClassicalRegister(3,"c") 
        self.qc = QuantumCircuit(self.q,self.c)
        
    def exp_initialize(self):
        theta = 2*pi* randrange(100)/100 # radians
        self.a = cos(theta)
        self.b = sin(theta)
        self.qc.ry(2*theta,self.q[2])
        # print("the picked angle is", theta* 360/2/pi,"degrees and",theta,"radians")
        # print("a=",round(self.a,3),"b=",round(self.b,3))
        # print("a*a=",round(self.a**2,3),"b*b=",round(self.b**2,3))
        
    def calculate(self):
        self.qc.h(self.q[1])
        self.qc.cx(self.q[1],self.q[0]) 
        self.qc.cx(self.q[2],self.q[1])
        self.qc.h(self.q[2])
        self.qc.measure(self.q[1:3], self.c[1:3])
    
    ############################################################ NOT USED ############################################################
    
    def read_statevector(self):
        self.simulator()
        state = self.job.result().get_statevector(self.qc)

    def classical_register(self):
        self.simulator(sim='qasm_simulator')
        alice_bits = list(self.job.result().get_counts(self.qc))[0][1:3]                  # measurement of Alice's qubits
        # print("Bits measured by Alice:", alice_bits, self.job.result().get_counts(self.qc))
        # print(alice_bits)

    def classical_out(self):
        job = execute(self.qc,Aer.get_backend('statevector_simulator'),optimization_level=0,shots=1)
        self.current_quantum_state=job.result().get_statevector(self.qc)
        for i in range(len(self.current_quantum_state)):
            print(self.current_quantum_state[i].real)
        print()

        classical_outcomes = ['00','01','10','11']

        for i in range(4):
            if (self.current_quantum_state[2*i].real != 0) or (self.current_quantum_state[2*i+1].real != 0):
                print("the classical outcome is",classical_outcomes[i])
                self.classical_outcome = classical_outcomes[i]
                self.balvis_state = [ self.current_quantum_state[2*i].real,self.current_quantum_state[2*i+1].real ]
        print()
        self.all_states = ['000','001','010','011','100','101','110','111']
        self.balvis_state_str = "|"+self.classical_outcome+">("

    def new_quantum_state(self):
        for i in range(len(self.current_quantum_state)):
            if abs(self.current_quantum_state[i].real-self.a)<0.000001: 
                self.balvis_state_str += "+a|"+ self.all_states[i][2]+">"
            elif abs(self.current_quantum_state[i].real+self.a)<0.000001:
                self.balvis_state_str += "-a|"+ self.all_states[i][2]+">"
            elif abs(self.current_quantum_state[i].real-self.b)<0.000001: 
                self.balvis_state_str += "+b|"+ self.all_states[i][2]+">"
            elif abs(self.current_quantum_state[i].real+self.b)<0.000001: 
                self.balvis_state_str += "-b|"+ self.all_states[i][2]+">"
        self.balvis_state_str += ")"        
        print("the new quantum state is",self.balvis_state_str)
