import React from "react";
import QuantumAlg from '../components/quantumAlgorithm.tsx';

const properties = ["qubits", "gates", "other"];

export default function QKDPage() {
  return (
    <div className='container'>
      <QuantumAlg algorithm="key-distribution" properties={properties} />
    </div>
  );
};
