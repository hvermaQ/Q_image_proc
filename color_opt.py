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

def color_opt(p_in,in_color):
    error_meas = pauli_error([('X',p_in), ('I', 1 - p_in)])
    cr = ClassicalRegister(1, 'c') 
    qr = QuantumRegister(1, 'q')
    qc = QuantumCircuit(qr,cr,name='circ')
    init = [1,0]
    qc.initialize(init,0)
    qc.h(0)
    qc.u(np.pi/3,0,np.pi/6,0)
    qc.measure(0,0)
    noise_bit_flip = NoiseModel()
    noise_bit_flip.add_all_qubit_quantum_error(error_meas, "u")
    sim_noise = AerSimulator(noise_model = noise_bit_flip)
    circ_n = transpile(qc,sim_noise)
    job = sim_noise.run(circ_n,shots=100)
    res = job.result()
    tes = res.get_counts()
    r_1 = tes['0']
    r_2 = tes['1']
    cost = (255*r_1/(r_2 +r_1) - in_color)**2
    return(cost)
