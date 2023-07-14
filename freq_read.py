# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 20:51:22 2023

@author: Strange
"""

import wave
import numpy as np

# Open the audio file
audio_file = 'om_sound.wav'
with wave.open(audio_file, 'rb') as wav_file:
    # Get the sample rate
    sample_rate = wav_file.getframerate()

    # Calculate the frequency range in Hz
    frame_duration = 1 / sample_rate
    hop_duration = 512 / sample_rate
    frequency_range_hz = 1 / (frame_duration * hop_duration)

# Print the frequency range in Hz
print("Frequency range:", frequency_range_hz, "Hz")
