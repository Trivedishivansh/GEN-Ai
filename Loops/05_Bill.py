#zips in python

name = ["shiv","vandan","krish","jayverr"]
bill = [20,50,80,100]

for customer,amount in zip(name,bill):
  print(f"{customer}:{amount}")