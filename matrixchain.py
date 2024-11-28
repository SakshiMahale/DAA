def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    # Create a table to store the minimum number of scalar multiplications
    m = [[0] * n for _ in range(n)]  # Initialize table m with zero
    s = [[0] * n for _ in range(n)]  # Table to store the index of the split

    # Loop over chain lengths (subproblem sizes)
    for chain_length in range(2, n + 1):  # Chain length goes from 2 to n
        for i in range(n - chain_length + 1):  # Loop over starting index
            j = i + chain_length - 1  # End index of subchain
            m[i][j] = float('inf')  # Start with a large number (infinity)
            # Try all possible positions to split the chain
            for k in range(i, j):  # Split between i and j at position k
                # q is the cost of multiplying matrices Ai...Ak and Ak+1...Aj
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q  # Update the minimum cost
                    s[i][j] = k  # Store the index of the split

    return m, s  # Return both tables


def print_parenthesization(s, i, j):
    """This function prints the parenthesization of matrices using the split points."""
    if i == j:
        return f"A{i + 1}"
    else:
        k = s[i][j]
        left = print_parenthesization(s, i, k)
        right = print_parenthesization(s, k + 1, j)
        return f"({left} x {right})"


def main():
    # Example meteorological data: 3 cities with data for 7 days
    # City A: 7 days, 5 attributes
    # City B: 7 days, 6 attributes
    # City C: 7 days, 4 attributes
    # The dimensions of the matrices for cities A, B, and C will be [7x5],
    # [7x6], [7x4]
    p = [7, 5, 6, 4]  # The dimensions of the matrices: [7x5], [7x6], [7x4]
    m, s = matrix_chain_order(p)  # Call the function to find the minimum multiplications

    print(f"Minimum number of scalar multiplications: {m[0][len(p) - 2]}")  # Minimum cost to multiply all matrices A1 to An
    print(f"Optimal parenthesization: {print_parenthesization(s, 0, len(p) - 2)}")  # Parenthesization


if __name__ == "__main__":
    main()
