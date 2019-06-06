from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister


def flubulator():

    q = QuantumRegister(2)
    qc = QuantumCircuit(q, name='Flubulator')

    qc.h(q)
    qc.cx(q[1], q[0])

    return qc.to_instruction()
