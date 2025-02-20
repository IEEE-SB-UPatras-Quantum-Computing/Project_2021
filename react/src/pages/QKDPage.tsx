import React from "react";
import QuantumAlg from '../components/quantumAlgorithm.tsx';

const properties = ["qubits", "gates", "other"];

export default function QKDPage() {
  return (
    <div className='container'>
      <QuantumAlg name="Quantum Cryptography" algorithm="cryptography" properties={properties} />
    </div>
  );
};
