import React from "react";
import QuantumAlg from '../components/quantumAlgorithm.tsx';

const properties = ["qubits", "gates", "other"];

export default function TeleportationPage() {
  return (
    <div className='container'>
      <QuantumAlg name="Teleportation" algorithm="teleportation" properties={properties} />
    </div>
  );
};
