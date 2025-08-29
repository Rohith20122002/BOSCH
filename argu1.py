import sys
args = sys.argv[1:]
numeric_args = [arg for arg in args ]
biggest = max(numeric_args)
smallest = min(numeric_args)
print("Biggest value:" ,biggest)
print("Smallest value: ",smallest)