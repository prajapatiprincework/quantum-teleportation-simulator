# ⚛️ Quantum Teleportation Simulator

A Qiskit-based simulation of the **Quantum Teleportation Protocol** using Python, Qiskit, Qiskit Aer, and NumPy.

This is my first quantum-computing project, built to understand the complete working of quantum teleportation — from creating entanglement to measurement, classical communication, conditional quantum operations, and Bob's final state.

---

## 📌 Project Overview

Quantum teleportation is a quantum-information protocol that transfers the **quantum state** of one qubit to another qubit.

It does **not** physically send the original qubit from Alice to Bob.

Instead, the protocol uses:

- An input quantum state
- A shared entangled Bell pair
- Two classical bits
- Conditional quantum operations

If Alice initially has an unknown state

**|ψ⟩ = α|0⟩ + β|1⟩**

the goal is to reproduce the same state on Bob's qubit.

The original state is destroyed during Alice's measurement, while Bob's qubit is transformed into the original state.

> **Important:** Quantum teleportation does not allow faster-than-light communication. Alice must communicate her two classical measurement results to Bob.

---

# 🧠 1. Quantum State

A general single-qubit state can be written as:

**|ψ⟩ = α|0⟩ + β|1⟩**

where α and β are probability amplitudes.

They satisfy the normalization condition:

**|α|² + |β|² = 1**

Therefore:

- Probability of measuring `0` = **|α|²**
- Probability of measuring `1` = **|β|²**

For example:

**|ψ⟩ = √0.8|0⟩ + √0.2|1⟩**

gives:

- **P(0) = 0.8**
- **P(1) = 0.2**

---

# 🎯 2. Objective

The objective of the project is to start with a quantum state on Alice's qubit:

**|ψ⟩ = α|0⟩ + β|1⟩**

and reconstruct that state on Bob's qubit.

Conceptually:

**Alice: |ψ⟩**

↓

**Quantum Teleportation Protocol**

↓

**Bob: |ψ⟩**

The physical qubit is not transported from Alice to Bob.

The protocol uses:

**Entanglement + Classical Communication + Quantum Corrections**

---

# 🧩 3. Qubits and Classical Bits

This project uses **3 quantum bits** and **3 classical bits**.

| Qubit | Role |
|---|---|
| `q0` | Alice's input quantum state |
| `q1` | Alice's half of the entangled pair |
| `q2` | Bob's half of the entangled pair |

The classical bits are:

| Classical Bit | Role |
|---|---|
| `c0` | Alice's first measurement result |
| `c1` | Alice's second measurement result |
| `c2` | Bob's final measurement result |

---

# 🔗 4. Creating the Entangled Bell Pair

Alice and Bob first create a shared entangled state between `q1` and `q2`.

Initially:

**|00⟩**

Apply a Hadamard gate to `q1`:

```python
qc.h(1)
```

The Hadamard gate transforms:

**|0⟩ → (|0⟩ + |1⟩) / √2**

The two-qubit state becomes:

**(|00⟩ + |10⟩) / √2**

Now apply a CNOT gate:

```python
qc.cx(1, 2)
```

The resulting state is:

**|Φ⁺⟩ = (|00⟩ + |11⟩) / √2**

This is one of the four Bell states.

The two qubits are now entangled.

---

# 🔬 5. Bell State

The Bell state used in this project is:

**|Φ⁺⟩ = (|00⟩ + |11⟩) / √2**

The four standard Bell states are:

- **|Φ⁺⟩ = (|00⟩ + |11⟩) / √2**
- **|Φ⁻⟩ = (|00⟩ − |11⟩) / √2**
- **|Ψ⁺⟩ = (|01⟩ + |10⟩) / √2**
- **|Ψ⁻⟩ = (|01⟩ − |10⟩) / √2**

This project uses **|Φ⁺⟩** as the shared entanglement resource.

---

# 👤 6. Alice's Input State

The circuit initially starts in:

**|000⟩**

Therefore every qubit starts in the `|0⟩` state.

In the current implementation:

```python
qc.h(0)
```

This prepares Alice's qubit in:

**|+⟩ = (|0⟩ + |1⟩) / √2**

So the current version of the project demonstrates teleportation of the **|+⟩ state**.

The circuit can later be extended to arbitrary single-qubit states.

---

# 📐 7. Alice's Bell-Basis Operation

Alice has:

- `q0` → input state
- `q1` → her half of the Bell pair

Bob has:

- `q2` → his half of the Bell pair

Alice applies:

```python
qc.cx(0, 1)
qc.h(0)
```

These operations transform Alice's two qubits into the Bell-measurement basis.

Alice then measures both qubits:

```python
qc.measure(0, 0)
qc.measure(1, 1)
```

The measurements produce two classical bits:

**c0** and **c1**

There are four possible combinations:

| `c1 c0` | Bob's correction |
|---|---|
| `00` | None |
| `01` | Z |
| `10` | X |
| `11` | X + Z |

---

# 📡 8. Classical Communication

After Alice measures her two qubits, she obtains two classical bits.

These bits are sent to Bob.

The important distinction is:

**Quantum information:** the state `|ψ⟩`

**Classical information:** the measurement results `c0` and `c1`

Alice does **not** send the original qubit to Bob.

She sends only the two classical measurement results.

Bob already possesses the other half of the entangled pair.

---

# ⚙️ 9. Bob's Conditional Corrections

Depending on Alice's measurement results, Bob's qubit may require an X and/or Z correction.

In this implementation:

```python
with qc.if_test((qc.clbits[1], 1)):
    qc.x(2)

with qc.if_test((qc.clbits[0], 1)):
    qc.z(2)
```

This means:

- If `c1 = 1` → apply **X** to Bob's qubit.
- If `c0 = 1` → apply **Z** to Bob's qubit.

Therefore:

| `c1` | `c0` | Operation on Bob |
|---:|---:|---|
| 0 | 0 | None |
| 0 | 1 | Z |
| 1 | 0 | X |
| 1 | 1 | X + Z |

After the correction, Bob's qubit contains the teleported state.

---

# 🔢 10. Understanding Qiskit's Bit Ordering

One important detail in Qiskit is that classical bits are displayed in reverse numerical order.

For example, if the output is:

```text
101
```

Qiskit displays this as:

**c2 c1 c0**

Therefore:

- `c2 = 1`
- `c1 = 0`
- `c0 = 1`

In this project:

- `c0` → Alice's first measurement
- `c1` → Alice's second measurement
- `c2` → Bob's final measurement

So `101` means:

**Bob's final measurement = 1**

and Alice's measurement result is:

**c1 c0 = 01**

which corresponds to the **Z correction** in this circuit convention.

---

# 🧮 11. Mathematical Picture of Teleportation

Suppose Alice starts with:

**|ψ⟩ = α|0⟩ + β|1⟩**

and Alice and Bob share:

**|Φ⁺⟩ = (|00⟩ + |11⟩) / √2**

The complete three-qubit state is:

**|ψ⟩ ⊗ |Φ⁺⟩**

After Alice performs the Bell-basis operations and measurement, Bob's qubit becomes one of four related states.

The four possibilities are:

| Alice's result | Bob's state |
|---|---|
| `00` | `|ψ⟩` |
| `01` | `Z|ψ⟩` |
| `10` | `X|ψ⟩` |
| `11` | `XZ|ψ⟩` |

Bob uses Alice's classical information to apply the appropriate correction.

The final result is:

**Bob → |ψ⟩**

Therefore the quantum state has been transferred to Bob.

---

# 🚫 12. Teleportation Is Not Cloning

Quantum teleportation does not create two copies of the original quantum state.

Before Alice's measurement:

**Alice → |ψ⟩**

**Bob → entangled qubit**

After Alice's measurement and Bob's correction:

**Alice → original state destroyed**

**Bob → |ψ⟩**

Therefore:

**Teleportation ≠ Copying**

This is consistent with the **no-cloning theorem**.

---

# 🌐 13. Why Classical Communication Is Required

Although Alice and Bob share entanglement, Bob cannot simply measure his qubit and obtain Alice's state.

Alice must communicate the two classical bits.

Therefore:

**Entanglement + 2 classical bits + Bob's conditional correction = Quantum Teleportation**

This is why quantum teleportation cannot be used for faster-than-light communication.

---

# 💻 14. Qiskit Implementation

The current implementation is:

```python
import numpy as np

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


# ============================================================
# CREATE QUANTUM CIRCUIT
# ============================================================

qc = QuantumCircuit(3, 3)


# ============================================================
# 1. PREPARE ALICE'S INPUT STATE
# ============================================================

# Hadamard creates |+>
# |+> = (|0> + |1>) / sqrt(2)

qc.h(0)


# ============================================================
# 2. CREATE BELL STATE BETWEEN q1 AND q2
# ============================================================

qc.h(1)
qc.cx(1, 2)

qc.barrier()


# ============================================================
# 3. ALICE'S BELL-BASIS OPERATIONS
# ============================================================

qc.cx(0, 1)
qc.h(0)

qc.barrier()


# ============================================================
# 4. ALICE MEASURES HER TWO QUBITS
# ============================================================

qc.measure(0, 0)
qc.measure(1, 1)


# ============================================================
# 5. BOB'S CONDITIONAL CORRECTIONS
# ============================================================

# If c1 = 1 → apply X to Bob's qubit
with qc.if_test((qc.clbits[1], 1)):
    qc.x(2)

# If c0 = 1 → apply Z to Bob's qubit
with qc.if_test((qc.clbits[0], 1)):
    qc.z(2)


qc.barrier()


# ============================================================
# 6. BOB MEASURES HIS FINAL QUBIT
# ============================================================

qc.measure(2, 2)


# ============================================================
# 7. RUN SIMULATION
# ============================================================

simulator = AerSimulator()

result = simulator.run(
    qc,
    shots=1000
).result()


# ============================================================
# 8. GET RESULTS
# ============================================================

counts = result.get_counts()

print("Measurement results:")
print(counts)

print("\nQuantum circuit:")
print(qc.draw())
```

---

# 📊 15. Simulation

The circuit is simulated using:

```python
simulator = AerSimulator()
```

The circuit is executed:

```python
shots=1000
```

This means the circuit is simulated **1000 times**.

The measurement results can look like:

```text
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
```

The exact numbers vary because quantum measurement is probabilistic.

---

# 📈 16. What Does the Output Mean?

A three-bit result such as:

```text
101
```

contains three classical measurement results:

**c2 c1 c0**

For `101`:

- `c2 = 1` → Bob's final measurement
- `c1 = 0` → Alice's second measurement
- `c0 = 1` → Alice's first measurement

Therefore Alice's measurement result is:

**c1 c0 = 01**

and Bob's final measurement is:

**c2 = 1**

The first two bits determine the correction Bob needed.

The final bit is Bob's measurement outcome.

---

# 🔬 17. Different Input States

The input state can be changed by modifying the operations on `q0`.

## State |0⟩

The circuit starts with:

```python
# q0 is already |0>
```

No gate is required.

---

## State |1⟩

Apply:

```python
qc.x(0)
```

This produces:

**|1⟩**

---

## State |+⟩

Apply:

```python
qc.h(0)
```

This produces:

**|+⟩ = (|0⟩ + |1⟩) / √2**

This is the state used in the current version.

---

## General Real-Amplitude State

The `RY` gate can prepare:

```python
theta = np.pi / 3

qc.ry(theta, 0)
```

which gives:

**|ψ⟩ = cos(θ/2)|0⟩ + sin(θ/2)|1⟩**

This allows testing states beyond `|0⟩`, `|1⟩`, and `|+⟩`.

---

# 🔍 18. Statevector Verification

Measurement counts are useful, but they do not directly compare the complete quantum states.

A future version of this project will use **statevector verification**.

The idea is:

**Prepare original state**

↓

**Teleport the state**

↓

**Obtain Bob's statevector**

↓

**Compare the original and Bob's state**

For two pure states, fidelity can be written as:

**F = |⟨ψ_original|ψ_Bob⟩|²**

For an ideal noiseless teleportation circuit:

**F = 1**

This will provide quantitative verification of the teleportation process.

---

# 🚀 19. Future Improvements

## Completed

- [x] Three-qubit teleportation circuit
- [x] Bell-state generation
- [x] Entanglement
- [x] Alice's Bell-basis operations
- [x] Alice's measurement
- [x] Classical feed-forward
- [x] Conditional X correction
- [x] Conditional Z correction
- [x] Bob's final measurement
- [x] Qiskit Aer simulation

## Planned

- [ ] Arbitrary single-qubit state preparation
- [ ] Statevector verification
- [ ] Fidelity calculation
- [ ] Bloch-sphere visualization
- [ ] Quantum-state tomography
- [ ] Noise simulation
- [ ] Decoherence analysis
- [ ] Error analysis
- [ ] Circuit-depth analysis
- [ ] Gate-count analysis
- [ ] Execution on real quantum hardware
- [ ] Comparison between ideal simulation and real hardware

---

# 🧪 20. What I Learned

Building this project helped me understand quantum teleportation from both the **physics** and **programming** perspectives.

The main concepts I explored were:

- Qubits
- Superposition
- Quantum gates
- Entanglement
- Bell states
- Bell-basis measurement
- Classical bits
- Conditional quantum operations
- Quantum measurement
- Quantum circuit simulation

The complete conceptual flow is:

**Qubit**

↓

**Superposition**

↓

**Entanglement**

↓

**Bell measurement**

↓

**Classical information**

↓

**Conditional quantum operations**

↓

**Recovered quantum state**

---

# 🛠️ 21. Technologies Used

- **Python**
- **Qiskit**
- **Qiskit Aer**
- **NumPy**

---

# 📁 22. Project Structure

```text
quantum-teleportation-simulator/
│
├── README.md
├── requirements.txt
│
├── src/
│   └── quantum_teleportation_simulator.py
│
├── images/
│   ├── teleportation_circuit.png
│   ├── teleportation_code.png
│   ├── teleportation_principle.png
│
└── results/
    └── example_output.txt
```

---

# ▶️ 23. How to Run

## Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/quantum-teleportation-simulator.git
```

## Enter the project directory

```bash
cd quantum-teleportation-simulator
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the simulator

```bash
python src/quantum_teleportation.py
```

---

# 📦 24. Requirements

Create a file named `requirements.txt` with:

```text
qiskit
qiskit-aer
numpy
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

---

# 🖼️ 25. Project Images

## Quantum Teleportation Circuit

![Quantum Teleportation Circuit](images/teleportation_circuit.png)

## Qiskit Implementation

![Qiskit Implementation](images/teleportation_code.png)

## Quantum Teleportation Principle

![Quantum Teleportation Principle](images/teleportation_principle.png)

---

# 👨‍💻 Author

## Prince Prajapati

Integrated MSc Physics Student

### Interests

- Quantum Computing
- Quantum Information
- Quantum Mechanics
- Quantum Algorithms
- Python
- Qiskit

---

# 📌 26. Project Status

**🟢 Basic Quantum Teleportation Simulation Completed**

The current version implements the ideal quantum teleportation protocol using a Qiskit simulator.

The current implementation demonstrates teleportation of the **|+⟩ state**.

The next development stage will focus on:

**Arbitrary-state preparation → Statevector verification → Fidelity → Visualization → Noise analysis → Real quantum hardware**

---

## ⭐ Explore and Experiment

This project is primarily an educational implementation.

The goal is to understand the underlying physics and how the theoretical quantum teleportation protocol maps onto an executable Qiskit circuit.
