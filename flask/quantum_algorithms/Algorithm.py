from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector, plot_histogram, plot_state_qsphere
from qiskit.quantum_info import Statevector
import os

class Protocol:
    def __init__(self, save_folder, num_qubits=1):
        self.folder = save_folder
        self.qc = QuantumCircuit(num_qubits)
        
        self.initialize_circuit()
        self.create_circuit()
        self.save()
    
    def initialize_circuit(self):
        # To be implemented in each protocol
        return NotImplemented

    def create_circuit(self):
        # To be implemented in each protocol
        return NotImplemented

    def save(self, circ=True, qsphere=True, qubits=True, hist=True):
        self.statevector = Statevector(self.qc)
        self.probabilities = self.statevector.probabilities_dict()

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        if circ:
            self.qc.draw('mpl', filename= self.folder+"circ.jpg")
        if qsphere:
            plot_state_qsphere(self.statevector).savefig(self.folder+"qsphere.jpg")
        if qubits:
            plot_bloch_multivector(self.statevector).savefig(self.folder+"qubits.jpg")
        if hist:
            plot_histogram(self.probabilities, title="Measurement").savefig(self.folder+"hist.jpg")
