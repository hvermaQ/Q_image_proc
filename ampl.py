# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 12:18:39 2022

@author: uqhverma
"""

from qiskit import *
import numpy as np
from qiskit.visualization import plot_bloch_vector
from qiskit.providers.aer import AerSimulator
from qiskit.providers.aer.noise import amplitude_damping_error
from qiskit.providers.aer.noise import NoiseModel

def ampl(p_in,in_color):
    error_amp_damp_1 = amplitude_damping_error(p_in, 1)
    noise_amp_damp_1 = NoiseModel()
    noise_amp_damp_1.add_all_qubit_quantum_error(error_amp_damp_1, ['u'])
    sim_noise = AerSimulator(noise_model = noise_amp_damp_1)
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
    r_1 = int(tes.get('0') or 0)
    r_2 = int(tes.get('1') or 0)
    cost = (255*r_1/(r_2 +r_1) - in_color)**2
    return(cost)
