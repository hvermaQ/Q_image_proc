from qiskit import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from color_opt import color_opt
from qiskit.visualization import plot_bloch_vector
from qiskit.providers.aer import AerSimulator
from qiskit.providers.aer.noise import pauli_error
from qiskit.providers.aer.noise import NoiseModel
from PIL import Image
import itertools
from multiprocessing import Pool
import time

im = Image.open("img_100.png")
rgb_im = im.convert('RGB')

#cord should be coordinate tuple

def mini(cord):
    imp = rgb_im.getpixel(cord)
    in_red = imp[0]
    res3 = minimize_scalar(color_opt, args = in_red,method='bounded', bounds=(0, 1))
    arg = res3.x
    error_meas = pauli_error([('X',arg), ('I', 1 - arg)])
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
    out_c= 255*r_1/(r_2 +r_1)
    return((out_c,0,0))
