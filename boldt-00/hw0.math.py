# file: hw0.math.py
# author: Brendon Boldt
# version: 1.1
# date: Sep/11/2017
# 
# This file demonstrates using Numpy and TensorFlow for basic
# computations in linear algebra

import numpy as np
import tensorflow as tf

# Create the necessary arrays in Numpy format
a = np.array([[1,4,-3],[2,-1,3]], dtype=np.float64)
b = np.array([[-2,0,5],[0,-1,4]], dtype=np.float64)
c = np.array([[1,0],[0,2]], dtype=np.float64)

# Demonstrate the computation using Numpy
print("numpy\n")
print("a^T b =\n%s\n" % (np.matmul(np.transpose(a), b)))
print("a b^T + c^-1 =\n%s\n" % (np.matmul(a, np.transpose(b)) + np.linalg.inv(c)))

# Create the TensorFlow graph
# TF graph can be created directly from Numpy arrays
atb = tf.matmul(tf.transpose(a), b)
abt = tf.matmul(a, tf.transpose(b))
with tf.Session() as sess:
	# Demonstrate the computation using TensorFlow
	print("tensorflow\n")
	print("a^T x b =\n%s\n" % (atb.eval()))
	print("a b^T + c^-1 =\n%s\n" % ((abt+tf.matrix_inverse(c)).eval()))
