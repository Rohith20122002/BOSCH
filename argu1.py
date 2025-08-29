import sys

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
args = sys.argv[1:]

    # Filter out only numeric arguments
numeric_args = [float(arg) for arg in args if is_number(arg)]
biggest = max(numeric_args)
smallest = min(numeric_args)
print(f"Biggest value: {biggest}")
print(f"Smallest value: {smallest}")