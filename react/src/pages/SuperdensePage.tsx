import React from "react";
import QuantumAlg from '../components/quantumAlgorithm.tsx';

const properties = ["qubits", "gates", "other"];

export default function SuperdensePage() {
  return (
    <div className='container'>
      <QuantumAlg algorithm="superdense" properties={properties} />
    </div>
  );
};
