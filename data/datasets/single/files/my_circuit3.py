from qiskit import QuantumCircuit

qc = QuantumCircuit(3, 3)  # classical bit 3개로 변경
qc.x(0)
qc.cx(0, 2)
qc.cx(2, 1)

qc.measure([0, 1], [0, 1]) 

print(qc) 