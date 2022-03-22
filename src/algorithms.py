import math
import torch
from tqdm import tqdm


def gsa(propagator, desired_image, distance, iterations=2000):
    
    original_amplitude = propagator.E_amplitude

    #for i in tqdm(range(iterations)):
    for i in range(iterations):
        
        #Prop to the image plane
        propagator.prop_asm(distance = distance)
   
        #Replace the amplitude with desired image
        propagator.set_amplitude(desired_image)
        
        #Prop to the diffractive plane
        propagator.prop_asm(distance = -distance)

        #Replace the amplitude with the original amplitude
        propagator.set_amplitude(original_amplitude)


    return propagator
