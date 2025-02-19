import React from 'react';
import QuantumAlg from './quantum-algorithm.tsx';

const properties = ["qubits", "gates", "other"];

function Superdense(props: any) {
    return (
        <section>
            <QuantumAlg name="Superdense" algorithm="superdense" properties={properties} />
        </section>
    );
}

export default Superdense;
