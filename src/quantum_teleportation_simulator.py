import qiskit 
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Constructing Entanglement-Bell State 
qcE=QuantumCircuit(3, 3)
qcE.h(1)
qcE.cx(1, 2)
qcE.barrier()

#Constructing Sender's Operations
qcE.h(0)
qcE.cx(0, 1)
qcE.h(0)
qcE.barrier()
qcE.measure(0, 0)
qcE.measure(1, 1)

# Construction of Receiver's Operations
with qcE.if_test((qcE.clbits[1], 1)):
    qcE.x(2)

with qcE.if_test((qcE.clbits[0], 1)):
    qcE.z(2)


qcE.barrier() 

qcE.measure(2, 2)

simulator = AerSimulator()

result = simulator.run(
    qcE,
    shots=1000
).result()
counts = result.get_counts()

print(counts)
print(" \n  \n")
print(qcE.draw())
print(" \n  \n")