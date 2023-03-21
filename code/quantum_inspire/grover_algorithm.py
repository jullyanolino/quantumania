version 1.0
#developer: Jullyano Lino
#date: March 13, 2022
#platform: Quantum Inspire by QuTech (https://www.quantum-inspire.com)
#backend: QX-34-L

#Grover algorithm to search databases
qubits 3

.init
H q[0:2]
.grover(2)

#quantum oracle
{X q[0] | H q[2]}
Toffoli q[0], q[1], q[2]
{H q[2] | X q[0]}

#Diffusion
{H q[0] | H q[1] | H q[2]}
{H q[1] | X q[0] | X q[2]}
H q[2]
Toffoli q[0], q[1], q[2]
H q[2]
{X q[1] | X q[0] | X q[2]}
{H q[0] | H q[1] | H q[2]}
