def parse_matrix_file(file_path):
    """
    Parse a text file containing a matrix into a 2D array
    
    Args:
        file_path (str): Path to the text file
        
    Returns:
        list: 2D array representing the matrix
    """
    try:
        # Read the file
        with open(file_path, 'r') as file:
            lines = file.read().strip().split('\n')
        
        # Parse the first line to get dimensions
        dimensions = lines[0].strip().split()
        if len(dimensions) != 2:
            raise ValueError("First line must contain exactly two numbers for dimensions")
        
        n, m = map(int, dimensions)
        
        # Validate dimensions
        if n <= 0 or m <= 0:
            raise ValueError(f"Invalid matrix dimensions: {n}x{m}")
        
        # Parse the matrix data
        matrix = []
        for i in range(1, n+1):
            if i >= len(lines):
                raise ValueError(f"Expected {n} rows but only found {len(lines) - 1}")
            
            # Split the line by whitespace and convert to integers
            row = list(map(int, lines[i].strip().split()))
            
            if len(row) != m:
                raise ValueError(f"Row {i} has {len(row)} elements but expected {m}")
            
            matrix.append(row)
        
        # Validate matrix size
        if len(matrix) != n:
            raise ValueError(f"Expected {n} rows but parsed {len(matrix)}")
        
        return matrix
    
    except Exception as e:
        print(f"Error parsing matrix file: {e}")
        raise

# Example usage
def process_matrix(file_path):
    """
    Process a matrix file and display the parsed matrix
    
    Args:
        file_path (str): Path to the matrix file
        
    Returns:
        list: 2D array representing the matrix
    """
    try:
        matrix = parse_matrix_file(file_path)
        print(f"Matrix dimensions: {len(matrix)} x {len(matrix[0])}")
        print("Parsed matrix:")
        for row in matrix:
            print(row)
        return matrix
    except Exception as e:
        print(f"Failed to process matrix: {e}")
        return None

# Example call
# if __name__ == "__main__":
#     process_matrix("matrix.txt")