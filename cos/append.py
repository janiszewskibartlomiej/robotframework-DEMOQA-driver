import os
import sys

# print(sys.path)
# # sys.path.append(os.path.dirname('.'))
# gwc = os.getcwd()
# print(gwc)
#
# # pw = os.path.abspath(__file__)
# # print(pw)
# # sys.path.append(os.path.dirname(gwc))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print(sys.path)

# z = ["name", "alfred", "email", "hongo@bongo.pl", "last name", "janisz"]
z = ["name", "alfred", "email", "hongo@bongo.pl", "last name"]
parameters = z[::2]
print(parameters)
value = z[1::2]
print(value)
xx = zip(parameters, value)
print(list(xx))