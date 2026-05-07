from qiskit import QuantumCircuit

def circuit_with_unmodeled_gate():
    qc = QuantumCircuit(3, 1)
    qc.mcx([0, 1], 2)
    qc.measure(2, 0)
    return qc

qc = circuit_with_unmodeled_gate()
print(qc)