import sys
import time

# sys.argv is a list with the command-line arguments. sysv.arg[0] is the name of Python script
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))


T1 = time.perf_counter()


T2 = time.perf_counter()
print('Time required', T2 - T1, 'sec.')