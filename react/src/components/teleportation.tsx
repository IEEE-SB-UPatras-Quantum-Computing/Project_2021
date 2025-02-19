import React from 'react';
import QuantumAlg from './quantum-algorithm.tsx';

const properties = ["qubits", "gates", "other"];

function Teleport(props: any) {
    return (
        <section>
            <QuantumAlg name="Teleportation" algorithm="teleportation" properties={properties} />
        </section>
    );
}

export default Teleport;
