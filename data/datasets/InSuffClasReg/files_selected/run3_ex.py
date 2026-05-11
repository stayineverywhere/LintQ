from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# 측정 대신 상태벡터를 직접 확인
sv = Statevector.from_instruction(qc)
print(sv)