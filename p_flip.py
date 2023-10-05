# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 18:39:48 2022

@author: uqhverma
"""

from qiskit import *
import numpy as np
from qiskit.visualization import plot_bloch_vector
from qiskit.providers.aer import AerSimulator
from qiskit.providers.aer.noise import pauli_error
from qiskit.providers.aer.noise import NoiseModel

def p_flip(p_in,in_color):
    error_phaseflip_1 = pauli_error([('Z',p_in), ('I', 1 - p_in)])
    noise_phaseflip_1 = NoiseModel()
    noise_phaseflip_1.add_all_qubit_quantum_error(error_phaseflip_1, ['u'])
    sim_noise = AerSimulator(noise_model = noise_phaseflip_1)
    n_qubits = 1
    noise_circ = QuantumCircuit(n_qubits)
    noise_circ.h(0)
    noise_circ.u(np.pi/2, 0, np.pi/6, 0)
    noise_circ.x(0)
    noise_circ.measure_all()
    circ_tnoise = transpile(noise_circ, sim_noise)
    job = sim_noise.run(circ_tnoise,shots = 100)   
    res = job.result()
    tes = res.get_counts()
    r_1 = tes['0']
    r_2 = tes['1']
    cost = (255*r_1/(r_2 +r_1) - in_color)**2
    return(cost)
