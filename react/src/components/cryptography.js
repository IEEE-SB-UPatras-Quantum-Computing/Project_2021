import './components.css';
import QuantumAlg from './quantum-algorithm';

const properties = ["qubits", "gates", "other"];

function QCryptography(props) {
    return (
        <section>
            <QuantumAlg name="Quantum Cryptography" algorithm="cryptography" properties={properties} />
        </section>
    );
}

export default QCryptography;
