from qiskit import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from p_flip import p_flip
from qiskit.visualization import plot_bloch_vector
from qiskit.providers.aer import AerSimulator
from qiskit.providers.aer.noise import pauli_error
from qiskit.providers.aer.noise import NoiseModel
from PIL import Image

im = Image.open("img_100.png")
rgb_im = im.convert('RGB')

#cord should be coordinate tuple

def mini_1(cord):
    imp = rgb_im.getpixel(cord)
    in_red = imp[0]
    res3 = minimize_scalar(p_flip, args = in_red,method='bounded', bounds=(0, 1))
    arg = res3.x
    error_phaseflip_1 = pauli_error([('Z',arg), ('I', 1 - arg)])
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
    out_c = 255*r_1/(r_2 +r_1)
    return((out_c,0,0))
