import sys
import numpy as np

def convert_to_mtx(output_filename):
    # Load the data from .npy files
    rows = np.load('row.npy')
    cols = np.load('col.npy')
    data = np.load('data.npy')
    shape = np.load('shape.npy')

    # Check if every value in data.npy is equal to 1
    all_ones = np.all(data == 1)

    if all_ones:
        print("All values in data.npy are equal to 1.")
    else:
        print("Not all values in data.npy are equal to 1.")

    # Print the shape of the matrix
    num_rows, num_cols = shape
    print(f"Shape of the matrix: {shape}")

    # Increment row and column indices by 1 to start from 1 instead of 0
    rows += 1
    cols += 1

    # Extract and count the number of non-zero entries
    num_edges = len(rows)

    # Write to Matrix Market (.mtx) format file
    with open(output_filename, 'w') as f:
        # Write header: number of rows, number of columns, number of non-zeros
        f.write(f"%%MatrixMarket matrix coordinate pattern general\n")
        f.write(f"{num_rows} {num_cols} {num_edges}\n")

        # Write edge list in the format: row column
        if all_ones:
            for i in range(num_edges):
                f.write(f"{rows[i]} {cols[i]}\n")
        else:
            for i in range(num_edges):
                f.write(f"{rows[i]} {cols[i]} {data[i]}\n")

    print(f"Matrix Market format file '{output_filename}' has been created.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py output_filename.mtx")
        sys.exit(1)
    
    output_filename = sys.argv[1]
    convert_to_mtx(output_filename)
