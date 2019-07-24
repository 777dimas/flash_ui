#from numpy import exp, array, random, dot
#training_set_inputs = array([[1, 1, 1], [1, 0, 1], [1, 0, 1], [0, 1, 1]])
#training_set_outputs = array([[0, 1, 1, 0]]).T
#random.seed(1)
#synaptic_weights = 2 * random.random((3, 1)) - 1
#for iteration in range(10000):
#    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
#    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
#print (1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights)))))


import binascii
#from urllib.request import urlopen
#response = urlopen('https://www.halls.my-support.club/api/getfilecard.php?FileCardId=131843_31')
#data = response.read()
#data1 = data.decode("utf8")
#response.close()
#print(data1)
#binary_string = binascii.unhexlify(data1)
#print(binary_string)
import urllib.request

url = 'https://www.halls.my-support.club/api/getfilecard.php?FileCardId=131843_31'

out = urllib.request.urlopen(url).read()
print(out)