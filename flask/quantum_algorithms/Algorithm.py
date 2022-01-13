# Necessary Imports for the notebook
from qiskit import QuantumCircuit, execute, assemble, Aer
from qiskit.visualization import plot_bloch_multivector, plot_histogram, plot_state_qsphere

class Protocol:
    def __init__(self, save_folder, q_num):
        self.q_num = q_num
        self.qc = QuantumCircuit(q_num)
        self.folder = save_folder
        self.create_circuit()
        self.save()
    
    def create_circuit(self):
        # To be implemented in each protocol
        pass
    
    def save(self):
        self.save_circuit()
        self.save_qshpere()
        self.save_qubits()
        self.save_histogram()

    def save_circuit(self):
        self.qc.draw('mpl', filename = self.folder+"circ.jpg")
    
    def save_qshpere(self):
        result = execute(self.qc, Aer.get_backend("statevector_simulator"), shots=1).result()
        plot_state_qsphere(result.get_statevector()).savefig(self.folder+"qsphere.jpg")

    def save_qubits(self):
        result = execute(self.qc, Aer.get_backend("statevector_simulator"), shots=1).result()
        plot_bloch_multivector(result.get_statevector()).savefig(self.folder+"qubits.jpg")
    
    def save_histogram(self):
        sim = Aer.get_backend('statevector_simulator')
        qobj = assemble(self.qc)  # Assemble circuit into a Qobj that can be run
        counts = sim.run(qobj).result().get_counts()  # Do the simulation, returning the state vector

        plot_histogram(counts).savefig(self.folder+"hist.jpg")  # Save the output on measurement of state vector