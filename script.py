import numpy as np
import sys

# Check if filename argument is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <output_filename>")
    sys.exit(1)

output_filename = sys.argv[1]  # Get the output filename from command line argument

# Load source and destination arrays
src_li = np.load('src_li.npy')
dst_li = np.load('dst_li.npy')

# Number of nodes (assuming it's a scalar value)
num_nodes = np.load('num_nodes.npy').item()

# Number of non-zero entries (number of edges)
num_non_zeros = len(src_li)

# Create list of tuples for rows and columns, and adjust indices
data_tuples = [(src + 1, dst + 1) for src, dst in zip(src_li, dst_li)]

# Write to .mtx format
with open(output_filename, 'w') as f:
    f.write("%%MatrixMarket matrix coordinate pattern general\n")
    f.write(f"{num_nodes} {num_nodes} {num_non_zeros}\n")  # Write num_rows, num_cols, and num_non_zeros
    for row, col in data_tuples:
        f.write(f'{row} {col}\n')

print(f"Matrix written to {output_filename}")

