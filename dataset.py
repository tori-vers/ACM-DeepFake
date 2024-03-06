import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import sys

import tensorflow_datasets as tfds

# Increase the recursion limit
sys.setrecursionlimit(10**6)

# Print the updated recursion limit
print(sys.getrecursionlimit())

# Load the 'celeb_a' dataset
ds = tfds.load('celeb_a', split='train', shuffle_files=True)
print(ds)
