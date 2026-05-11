from qiskit import QuantumCircuit

# 데이터 qubit 3개 + ancilla 1개
qc = QuantumCircuit(4, 1)

# 데이터 영역
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)

# ancilla(3번)로 syndrome 추출
qc.cx(0, 3)
qc.cx(1, 3)
qc.cx(2, 3)

# ancilla만 측정
qc.measure(3, 0)