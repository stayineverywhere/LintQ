from qiskit import QuantumCircuit

qc = QuantumCircuit(3, 2)  # classical bit 2개로 변경
qc.x(0)
qc.cx(0, 2)
qc.cx(2, 1)

qc.measure([0, 1], [0, 1])  # q0 → c0, q1 → c1

print(qc) 