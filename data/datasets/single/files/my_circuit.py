from qiskit import QuantumCircuit

qc = QuantumCircuit(3, 1)
qc.cx(0, 2)
qc.cx(2, 1)
qc.measure(1, 0)

print(qc)