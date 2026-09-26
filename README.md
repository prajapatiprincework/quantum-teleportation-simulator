# quantum-teleportation-simulator
An educational Qiskit simulation of quantum teleportation using entanglement, Bell-basis measurement, classical feed-forward, and conditional quantum corrections.
# ⚛️ Quantum Teleportation Simulator

# ⚛️ Quantum Teleportation Simulator

A Qiskit-based simulation of the **Quantum Teleportation Protocol** using
Python, Qiskit, Qiskit Aer, and NumPy.

This project was built to understand how an unknown quantum state can be
transferred from one qubit to another using **quantum entanglement,
measurement, classical communication, and conditional quantum operations**.

---

## 📌 Project Overview

Quantum teleportation is a quantum-information protocol that transfers the
**quantum state** of one qubit to another distant qubit.

The protocol does NOT physically transport the original qubit.

Instead, it uses:

1. An unknown quantum state
2. A shared entangled pair
3. Two classical bits of information
4. Conditional quantum operations

The original quantum state is destroyed during Alice's measurement, while
Bob's qubit is transformed into the original state.

### Important

Quantum teleportation does **not** allow faster-than-light communication.

Alice must communicate her two classical measurement results to Bob before
Bob can apply the required corrections.

---

# 🧠 Basic Quantum State

A general single-qubit state can be written as:

```text
|ψ⟩ = α|0⟩ + β|1


where:
α and β are complex probability amplitudes
and they satisfy:|α|² + |β|² = 1

The probability of measuring:

0 → |α|²

1 → |β|²

For example:

|ψ⟩ = √0.8 |0⟩ + √0.2 |1⟩

means:

P(0) = 0.8
P(1) = 0.2

🎯 Objective of the Project

The objective is to start with an input quantum state on Alice's qubit
|ψ⟩ = α|0⟩ + β|1⟩
and reproduce the same quantum state on Bob's qubit:Input:

Alice
 |ψ⟩
  |
  | Quantum Teleportation
  ↓
Bob
 |ψ⟩The physical qubit itself is not sent from Alice to Bob.

Only:

Quantum entanglement
        +
2 classical bits
        +
Conditional X/Z corrections

🧩 Qubits Used in This Project

The circuit contains three qubits:

q0 → Alice's unknown/input qubit

q1 → Alice's half of the entangled Bell pair

q2 → Bob's half of the entangled Bell pair

There are also three classical bits:

c0 → Alice's first measurement result

c1 → Alice's second measurement result

c2 → Bob's final measurement result

The circuit therefore has:

3 quantum bits
3 classical bits
🔬 Quantum Teleportation Protocol

The complete protocol can be divided into four major stages:

1. Prepare Alice's quantum state

2. Create an entangled Bell pair

3. Alice performs a Bell-basis measurement

4. Bob applies X/Z corrections using Alice's classical bits

Finally, Bob measures his qubit.

1️⃣ Prepare Alice's Quantum State

The circuit initially starts in:

|000⟩

which means that all three qubits are initially in the |0⟩ state.

For example, applying:

qc.x(0)

changes Alice's qubit from:

|0⟩

to:

|1⟩

A Hadamard gate can instead create an equal superposition:

qc.h(0)

which produces:

|+⟩ = (|0⟩ + |1⟩) / √2

For a more general real-amplitude state, the Ry gate can be used:

qc.ry(theta, 0)

which produces:

|ψ⟩ = cos(theta/2)|0⟩ + sin(theta/2)|1⟩
2️⃣ Create the Entangled Bell Pair

Alice and Bob first need a shared entangled state.

The circuit uses qubits q1 and q2.

First:

qc.h(1)

The Hadamard gate creates:

|0⟩ → (|0⟩ + |1⟩) / √2

Therefore the two-qubit state becomes:

(|00⟩ + |10⟩) / √2

Then we apply:

qc.cx(1, 2)

This creates the Bell state:

|Φ⁺⟩ = (|00⟩ + |11⟩) / √2

This is an entangled state.

The important feature is that the two qubits are no longer independently
described by separate states.

They form one combined quantum state.

🔗 Bell State

The Bell state used in this project is:

|Φ⁺⟩ = (|00⟩ + |11⟩) / √2

There are four standard Bell states:

|Φ⁺⟩ = (|00⟩ + |11⟩) / √2

|Φ⁻⟩ = (|00⟩ - |11⟩) / √2

|Ψ⁺⟩ = (|01⟩ + |10⟩) / √2

|Ψ⁻⟩ = (|01⟩ - |10⟩) / √2

This project uses:

|Φ⁺⟩
3️⃣ Alice's Bell-Basis Measurement

Alice now has:

q0 → unknown state |ψ⟩

q1 → Alice's half of Bell pair

Bob has:

q2 → Bob's half of Bell pair

Alice performs:

qc.cx(0, 1)
qc.h(0)

These operations transform Alice's two qubits into a basis suitable
for Bell-state measurement.

Alice then measures:

qc.measure(0, 0)
qc.measure(1, 1)

This produces two classical bits:

c0
c1

There are four possible combinations:

00
01
10
11

These two bits contain the information Bob needs to determine which
correction must be applied.

📡 4️⃣ Classical Communication

Alice sends her two classical measurement results to Bob.

The important distinction is:

Quantum information:
|ψ⟩

Classical information:
c0, c1

The classical bits are not the quantum state.

They only tell Bob which operation he needs to perform on his qubit.

5️⃣ Bob's Conditional Corrections

Bob's qubit may have one of four related states depending on Alice's
measurement result.

The required corrections are:

Alice result     Bob correction

c1 c0 = 00       I

c1 c0 = 01       X

c1 c0 = 10       Z

c1 c0 = 11       XZ

Here:

I = Identity operation

X = Pauli-X gate

Z = Pauli-Z gate

In this implementation, the Qiskit code is:

with qc.if_test((qc.clbits[1], 1)):
    qc.x(2)

with qc.if_test((qc.clbits[0], 1)):
    qc.z(2)

This means:

If c1 = 1:
    apply X to Bob's qubit

If c0 = 1:
    apply Z to Bob's qubit

Therefore:

c1 = 0, c0 = 0
→ no correction

c1 = 0, c0 = 1
→ Z correction

c1 = 1, c0 = 0
→ X correction

c1 = 1, c0 = 1
→ X + Z correction
⚠️ Important Note About Bit Ordering

Qiskit displays classical bits in reverse numerical order.

For example:

101

is displayed as:

c2 c1 c0

Therefore:

101

means:

c2 = 1
c1 = 0
c0 = 1

In this project:

c0 → Alice's first measurement
c1 → Alice's second measurement
c2 → Bob's final measurement

This is an important detail when interpreting the output.

🧠 What Happens Mathematically?

Suppose Alice's original state is:

|ψ⟩ = α|0⟩ + β|1⟩

After Alice performs her Bell-basis operations and measurement,
Bob's qubit becomes one of four related states.

Depending on Alice's two classical bits, Bob's state is:

00 → |ψ⟩

01 → Z|ψ⟩

10 → X|ψ⟩

11 → XZ|ψ⟩

Bob then applies the corresponding correction.

Because:

X² = I

Z² = I

the unwanted transformation can be removed.

Finally:

Bob → |ψ⟩

Therefore the quantum state has been transferred from Alice's qubit
to Bob's qubit.

🚫 Teleportation Is NOT Cloning

Quantum teleportation does not make two copies of the original state.

Before Alice's measurement:

Alice → |ψ⟩
Bob   → entangled qubit

After Alice's measurement and Bob's correction:

Alice → original state destroyed

Bob   → |ψ⟩

Therefore:

Original state is not copied.

This is consistent with the no-cloning theorem.

🌐 No Faster-Than-Light Communication

Quantum entanglement produces correlations between Alice and Bob,
but Bob cannot use teleportation to receive usable information instantly.

Alice still has to send:

2 classical bits

to Bob.

Therefore the protocol respects the limitations imposed by
relativistic causality.

💻 Qiskit Implementation

The core implementation is:

import numpy as np

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


# ============================================================
# CREATE CIRCUIT
# ============================================================

qc = QuantumCircuit(3, 3)


# ============================================================
# PREPARE ALICE'S INPUT STATE
# ============================================================

# Example: prepare |1>
qc.x(0)


# ============================================================
# CREATE BELL PAIR
# ============================================================

qc.h(1)
qc.cx(1, 2)

qc.barrier()


# ============================================================
# ALICE'S BELL-BASIS MEASUREMENT
# ============================================================

qc.cx(0, 1)
qc.h(0)

qc.barrier()

qc.measure(0, 0)
qc.measure(1, 1)


# ============================================================
# BOB'S CONDITIONAL CORRECTIONS
# ============================================================

# If c1 = 1 → apply X
with qc.if_test((qc.clbits[1], 1)):
    qc.x(2)

# If c0 = 1 → apply Z
with qc.if_test((qc.clbits[0], 1)):
    qc.z(2)

qc.barrier()


# ============================================================
# BOB'S FINAL MEASUREMENT
# ============================================================

qc.measure(2, 2)


# ============================================================
# SIMULATION
# ============================================================

simulator = AerSimulator()

result = simulator.run(
    qc,
    shots=1000
).result()

counts = result.get_counts()


# ============================================================
# OUTPUT
# ============================================================

print("Measurement results:")
print(counts)

print("\nQuantum circuit:")
print(qc.draw())
📊 Simulation

The circuit is simulated using:

simulator = AerSimulator()

The number of repetitions is controlled using:

shots=1000

This means that the circuit is executed 1000 times.

For example, the output may look like:

{
    '000': 116,
    '010': 138,
    '111': 142,
    '100': 130,
    '110': 123,
    '101': 129,
    '001': 120,
    '011': 102
}

The exact numbers change between simulations because quantum measurement
is probabilistic.

📈 Understanding the Measurement Results

The three-bit output contains:

c2 c1 c0

For example:

101

means:

Bob's result     = 1

Alice's c1       = 0

Alice's c0       = 1

Therefore Alice's measurement result is:

c1 c0 = 01

and according to this circuit's correction convention, Bob applies:

Z

The important point is that the three-bit output should not be treated
as one quantum state.

Each bit has a separate role.

🖼️ Circuit

The generated Qiskit circuit can be found in:

images/teleportation_circuit.png

The circuit represents:

q0 → Alice's input qubit

q1 → Alice's entangled qubit

q2 → Bob's qubit

c0, c1 → Alice's classical measurement results

c2 → Bob's final measurement
📚 Concepts Demonstrated

This project demonstrates the following concepts:

1. Qubit initialization

A Qiskit qubit starts in:

|0⟩
2. Quantum gates

The project uses:

H  → Hadamard gate

X  → Pauli-X gate

Z  → Pauli-Z gate

CX → Controlled-X / CNOT gate
3. Superposition

The Hadamard gate creates:

|+⟩ = (|0⟩ + |1⟩) / √2
4. Entanglement

The H + CNOT sequence creates the Bell state:

|Φ⁺⟩ = (|00⟩ + |11⟩) / √2
5. Measurement

Measurement converts quantum information into classical information.

6. Classical feed-forward

Alice's measurement results control Bob's quantum operations.

7. Quantum teleportation

The quantum state is reconstructed on Bob's qubit.

🧪 Different Input States

The circuit can be modified to test different input states.

State |0⟩

No gate is required:

# q0 starts as |0>
State |1⟩

Apply:

qc.x(0)
Equal Superposition

Apply:

qc.h(0)

giving:

|+⟩ = (|0⟩ + |1⟩) / √2
Real-Amplitude Superposition

Apply:

theta = np.pi / 3

qc.ry(theta, 0)

which creates:

|ψ⟩ = cos(theta/2)|0⟩ + sin(theta/2)|1⟩
🔍 Statevector Verification

A future version of this project will compare the original quantum
state with Bob's recovered quantum state using the simulator's
statevector representation.

The goal is to verify:

Original state = Bob's recovered state

using a quantitative measure such as state fidelity.

For two pure states, fidelity can be written as:

F = |⟨ψoriginal|ψBob⟩|²

For an ideal noiseless simulation, the expected fidelity is:

F = 1

This is a planned extension of the current measurement-based
implementation.

🚀 Future Improvements

The project will be extended in several stages.

Version 1 — Completed
 Three-qubit teleportation circuit
 Bell-state generation
 Alice's Bell measurement
 Classical measurement results
 Conditional X/Z corrections
 Bob's final measurement
 Qiskit Aer simulation
Version 2 — Planned
 Arbitrary single-qubit state preparation
 Statevector verification
 Fidelity calculation
 Bloch-sphere visualization
Version 3 — Planned
 Quantum-state tomography
 Noise simulation
 Decoherence effects
 Error analysis
 Comparison between ideal and noisy teleportation
Version 4 — Planned
 Execution on real quantum hardware
 Hardware noise comparison
 Transpilation analysis
 Gate-count and circuit-depth analysis
🛠️ Technologies Used
Python
Quantum information
Quantum mechanics
Quantum Teleportation
Qiskit
Qiskit Aer
NumPy
