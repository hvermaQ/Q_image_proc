# Q_image_proc in Qiskit Hackathon 2022
Aim: Reproduce an image pixel by pixel using a noisy quantum circuit. 

Theory: Noise restricts the available amplitude range in measurement basis, and hence, restricts an exact reproduction of image.

Steps (completed): 

      Take an image, break it into RGB components. Take one component (=number : n).
      
      Make a noisy quantum circuit with a fixed single qubit rotation, but variable noise parameter (= probability: p).
      
      Cost function: absolute square error in (255 * normalized amplitude of |0> state - n ) with variable p, and input color from pixel n.
      
      Minimize the cost function, find best p such that the image can be reproduced to the best extent possible i.e. color matching.
      
      Do it for all the std quantum channels: Ampl damping, dephasing and depolarizing.
      
      Incorporate into a multicore routine.
      
Drawback: selecting a fixed rotation and then applying a variable noise porbability only offers a range of measurement amplitudes, which can be made into an index, 
thus, not requiring an optimization at each pixel.

Reason for the drawback: 2 day timeframe. Actual plan was to take a random circuit for each pixel, then minimize over noise parameter (p).
