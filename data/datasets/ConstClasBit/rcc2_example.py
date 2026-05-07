from qiskit import QuantumCircuit


def build_measurement_subcircuit():
    meas = QuantumCircuit(1, 1, name="meas_sub")
    meas.measure(0, 0)
    return meas


def build_full_circuit():
    full = QuantumCircuit(1, 1, name="full")
    full.h(0)  # 상위 회로에서 qubit 0을 먼저 변형
    full.compose(build_measurement_subcircuit(), inplace=True)
    return full


qc = build_full_circuit()
print(qc)