import './components.css';
import QuantumAlg from './quantum-algorithm';

const properties = ["qubits", "gates", "other"];

function Superdense(props) {
    return (
        <section>
            <QuantumAlg name="Superdense" algorithm="superdense" properties={properties} />
        </section>
    );
}

export default Superdense;
