# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 20:51:22 2023

@author: Strange
"""

import numpy as np
from scipy.io import wavfile

# Set the desired sample rate and duration
sample_rate = 44100  # 44.1kHz
duration = 5  # 5 seconds

# Generate a numpy array of samples for the "om" sound
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Define the frequencies and durations for each part of the "om" sound
frequencies = [136.1, 108.1, 86.1]  # Adjust these frequencies as needed
durations = [1, 2, 2]  # Adjust these durations as needed

# Generate the "om" sound by concatenating sine waves for each part
sound = np.concatenate([np.sin(2 * np.pi * f * t[:int(d * sample_rate)]) for f, d in zip(frequencies, durations)])

# Scale the sound to 16-bit integers (between -32768 and 32767)
scaled_sound = np.int16(sound * 32767)

# Save the sound as a WAV file
wavfile.write("om_sound.wav", sample_rate, scaled_sound)
