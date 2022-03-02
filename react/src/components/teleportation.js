import './components.css';
import QuantumAlg from './quantum-algorithm';

const properties = ["qubits", "gates", "other"];

function Teleport(props) {
    return (
        <section>
            <QuantumAlg name="Teleportation" algorithm="teleportation" properties={properties} />
        </section>
    );
}

export default Teleport;
