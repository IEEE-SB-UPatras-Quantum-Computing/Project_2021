import React from 'react';
import QuantumAlg from './quantum-algorithm.tsx';

const properties = ["qubits", "gates", "other"];

function QCryptography(props: any) {
    return (
        <section>
            <QuantumAlg name="Quantum Cryptography" algorithm="cryptography" properties={properties} />
        </section>
    );
}

export default QCryptography;
