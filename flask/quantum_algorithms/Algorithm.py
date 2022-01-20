from msilib.schema import Error
from qiskit import QuantumCircuit, execute, assemble, Aer
from qiskit.visualization import plot_bloch_multivector, plot_histogram, plot_state_qsphere

class Protocol:
    def __init__(self, save_folder):
        self.folder = save_folder
        self.initialize_circuit()
        self.create_circuit()
        self.save()
    
    def initialize_circuit(self):
        # implement and declare the QuantumCircuit self.qc
        self.qc = QuantumCircuit(1) # Default circuit
    
    def create_circuit(self):
        # To be implemented in each protocol
        pass
    
    def save(self):
        self.save_circuit()
        self.sim = Aer.get_backend("statevector_simulator")
        self.statevector = execute(self.qc, self.sim, shots=1).result().get_statevector()
        self.save_qshpere()
        self.save_qubits()
        try: self.save_histogram()
        except Exception: return

    def save_circuit(self):
        self.qc.draw('mpl', filename= self.folder+"circ.jpg")
    
    def save_qshpere(self):
        plot_state_qsphere(self.statevector).savefig(self.folder+"qsphere.jpg")
    
    def save_qubits(self):
        plot_bloch_multivector(self.statevector).savefig(self.folder+"qubits.jpg")
    
    def save_histogram(self):
        #self.qc.measure_all()
        self.sim = Aer.get_backend("qasm_simulator")
        counts = execute(self.qc, self.sim).result().get_counts()  # Do the simulation, returning the statevector
        plot_histogram(counts, title="Measurement").savefig(self.folder+"hist.jpg")  # Save the output on measurement of statevector
