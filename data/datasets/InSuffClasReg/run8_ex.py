from qiskit import QuantumCircuit

qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)

# 인자 없이 호출하면 classical register를 자동으로 추가
qc.measure_all()