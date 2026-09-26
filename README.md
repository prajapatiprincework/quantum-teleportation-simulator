# quantum-teleportation-simulator
An educational Qiskit simulation of quantum teleportation using entanglement, Bell-basis measurement, classical feed-forward, and conditional quantum corrections.
# ⚛️ Quantum Teleportation Simulator

A Qiskit-based simulation of the **quantum teleportation protocol**.

This project was built to understand how a quantum state can be transferred
from one qubit to another using:

- Quantum entanglement
- Bell-basis measurement
- Classical communication
- Conditional quantum gates
- Quantum measurement

The project is implemented using **Python, Qiskit, and Qiskit Aer**.

---

## 📌 Project Overview

Quantum teleportation is a protocol that transfers an unknown quantum state
from Alice's qubit to Bob's qubit without physically sending the original
qubit from Alice to Bob.

The protocol uses three essential resources:

1. An unknown quantum state
2. A shared entangled Bell pair
3. Two classical bits of information

The original state is destroyed during Alice's measurement and reconstructed
on Bob's qubit after the appropriate quantum corrections.

> **Important:** Quantum teleportation does not allow faster-than-light
> communication. The two classical measurement results must still be
> communicated to Bob.

---

# 🧠 How Quantum Teleportation Works

Suppose Alice has an unknown qubit:

\[
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
\]

where

\[
|\alpha|^2 + |\beta|^2 = 1.
\]

Alice and Bob first share an entangled Bell state:

\[
|\Phi^+\rangle =
\frac{|00\rangle + |11\rangle}{\sqrt{2}}.
\]

Alice now has two qubits:

- Her unknown qubit
- Her half of the entangled pair

Bob has the other half of the entangled pair.

---

# 🔬 Step 1 — Create the Bell Pair

Starting with two qubits in:

\[
|00\rangle
\]

apply a Hadamard gate to the first qubit:

\[
|00\rangle
\xrightarrow{H}
\frac{|00\rangle+|10\rangle}{\sqrt2}.
\]

Then apply a CNOT:

\[
\frac{|00\rangle+|10\rangle}{\sqrt2}
\xrightarrow{CNOT}
\frac{|00\rangle+|11\rangle}{\sqrt2}.
\]

Therefore:

\[
\boxed{
|\Phi^+\rangle =
\frac{|00\rangle+|11\rangle}{\sqrt2}
}
\]

This creates entanglement between Alice's and Bob's qubits.

In Qiskit:

```python
qc.h(1)
qc.cx(1, 2)
