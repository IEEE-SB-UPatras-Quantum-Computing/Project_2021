from .Algorithm import Protocol
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from qiskit.circuit import Gate
from math import pi, cos, sin, sqrt
from random import randrange
# Necessary Imports for the notebook
from qiskit import QuantumCircuit, execute, assemble, Aer
from qiskit.visualization import plot_bloch_multivector, plot_histogram, plot_state_qsphere


from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from qiskit.circuit import Gate
from math import pi, cos, sin, sqrt
from random import randrange
# Necessary Imports for the notebook
from qiskit import QuantumCircuit, execute, assemble, Aer
from qiskit.visualization import plot_bloch_multivector, plot_histogram, plot_state_qsphere

        
class Teleportation_Protocol(Protocol):
    def __init__(self):
        q_num = 3
        super().__init__("folder1", q_num)
        
        
    def create_circuit(self):
        print("io")
        alice =  QuantumRegister(2,"a")
        self.a0 = alice[0]
        self.a1 = alice[1]
        bob =  QuantumRegister(1,"b")
        self.b0 = bob[0]
        c = ClassicalRegister(3,"c")
        self.qc = QuantumCircuit(alice,bob, c)
        self.s=0
        self.alice_init()
        self.initialize()
        self.initialize_exp()

    def alice_init(self):
        theta = 2*pi* randrange(100)/100 # random angle in radians
        self.qc.ry(2*theta, self.a0) # random state for Alice
        self.qc.h(self.a1)
        self.qc.cx(self.a1, self.b0)
        
    def initialize(self):
        self.simulator()
        self.read_statevector()
        self.classical_register()
       # self.circuit_draw()

    def initialize_exp(self):
        self.exp_circuit()
        self.exp_initialize()
        self.calculate()
        self.classical_out()
        self.new_quantum_state()
        
    def read_statevector(self):
        self.s = 0
        self.simulator()                                        # One for initial state          # One after Alice's measurement
        state=self.job.result().get_statevector(self.qc)

    def classical_register(self):
        self.s = 1
        self.simulator()
        alice_bits = list(self.job.result().get_counts(self.qc))[0][1:3]                  # measurement of Alice's qubits
        print("Bits measured by Alice:", alice_bits, self.job.result().get_counts(self.qc))
        print(alice_bits)
        
    def simulator(self, sim = 'statevector_simulator',shots=1 ):
        if (self.s) == 1:
            sim = 'qasm_simulator'
        simulator = Aer.get_backend(sim)
        self.job = execute(self.qc, simulator,shots = shots)

    def circuit_draw(self):
        display(self.qc.draw(output='mpl'))
        
    def exp_circuit(self):
        self.q =  QuantumRegister(3,"q") 
        self.c = ClassicalRegister(3,"c") 
        self.qc = QuantumCircuit(self.q,self.c)
        
    def exp_initialize(self):
        r = randrange(100)
        theta = 2*pi*(r/100) # radians
        print("the picked angle is",r*3.6,"degrees and",theta,"radians")
        self.a = cos(theta)
        self.b = sin(theta)
        print("a=",round(self.a,3),"b=",round(self.b,3))
        print("a*a=",round(self.a**2,3),"b*b=",round(self.b**2,3))
        self.qc.ry(2*theta,self.q[2])
        
    def calculate(self):
        self.qc.h(self.q[1])
        self.qc.cx(self.q[1],self.q[0]) 
        self.qc.cx(self.q[2],self.q[1])
        self.qc.h(self.q[2])
        self.qc.measure(self.q[1:3], self.c[1:3])

        #self.circuit_draw()
        
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
