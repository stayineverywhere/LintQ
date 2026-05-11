from qiskit import QuantumCircuit

# 예: 일부 출력만 읽는 QNN/QRAM 스타일
qc = QuantumCircuit(4, 1)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)

# 최종 판단에 필요한 한 qubit만 측정
qc.measure(3, 0)