def build_prefix_sum(grid):
    """
    Builds a 2D prefix sum array from a grid.
    
    Args:
        grid: A 2D array/list of numbers
        
    Returns:
        A 2D prefix sum array
    """
    # Get dimensions
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Initialize prefix sum array with an extra row and column
    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    # Fill the prefix sum array
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix_sum[i][j] = (
                prefix_sum[i-1][j] +      # Sum above
                prefix_sum[i][j-1] -      # Sum to the left
                prefix_sum[i-1][j-1] +    # Remove double counting
                grid[i-1][j-1]            # Add current cell
            )
    
    return prefix_sum

def get_submatrix_sum(prefix_sum, r1, c1, r2, c2):
    """
    Gets the sum of the rectangle from (r1,c1) to (r2,c2) inclusive.
    Note: r1, c1, r2, c2 are 0-indexed coordinates in the original grid.
    
    Args:
        prefix_sum: The precomputed 2D prefix sum array
        r1, c1: Top-left coordinates (0-indexed)
        r2, c2: Bottom-right coordinates (0-indexed)
        
    Returns:
        Sum of values in the rectangle
    """
    # Convert to 1-indexed for prefix sum array
    r1, c1, r2, c2 = r1+1, c1+1, r2+1, c2+1
    
    # Calculate sum using the prefix sum formula
    return (
        prefix_sum[r2][c2] -
        prefix_sum[r1-1][c2] -
        prefix_sum[r2][c1-1] +
        prefix_sum[r1-1][c1-1]
    )