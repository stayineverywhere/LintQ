from qiskit import QuantumCircuit

# 마지막 qubit를 ancilla로 사용한다고 가정
qc = QuantumCircuit(3, 2)
qc.h(0)
qc.cx(0, 1)
qc.ccx(0, 1, 2)   # 2번 qubit는 ancilla 역할

# 데이터 qubit만 측정
qc.measure(0, 0)
qc.measure(1, 1)