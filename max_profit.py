from prefix_sum import build_prefix_sum

def overlappingGridsCheck(range1, range2):
    """
    Check if two rectangular ranges overlap.
    Each range is represented as [row_start, row_end, col_start, col_end].
    """
    j1, j2, i1, i2 = range1  # First rectangle
    y1, y2, x1, x2 = range2  # Second rectangle
    
    if i2 < x1 or x2 < i1 or j2 < y1 or y2 < j1:
        return False
    
    # Otherwise, they overlap
    return True

def allGridsNonOverlapping(prefix_sum, avoid_ranges, grid):
    """
    Generate all possible rectangles that don't overlap with any in avoid_ranges.
    Returns list of [profit, [row_start, row_end, col_start, col_end]] pairs.
    """
    m, n = len(grid), len(grid[0])
    
    ret = []

    for j in range(m):
        for j_end in range(j, m):
            for i in range(n):
                for i_end in range(i, n):
                    rect = [j, j_end, i, i_end]
                    
                    # Check if current rectangle overlaps with any to avoid
                    overlaps = False
                    for avoid_range in avoid_ranges:
                        if overlappingGridsCheck(avoid_range, rect):
                            overlaps = True
                            break
                    
                    if not overlaps:
                        value = get_submatrix_sum(prefix_sum, j, i, j_end, i_end)
                        ret.append([value, rect])
    return ret

def maxProfit(grid, avoid_ranges=None, freq=0):
    """
    Find the maximum profit from placing 'freq' more mines.
    """
    if avoid_ranges is None:
        avoid_ranges = []
        
    if freq >= 3:
        return 0
    
    prefix_sum = build_prefix_sum(grid)
    
    ret = float("-inf")

    for value, rect in allGridsNonOverlapping(prefix_sum, avoid_ranges, grid):

        avoid_ranges.append(rect)
        ret = max(ret, value + maxProfit(grid, avoid_ranges, freq+1))
        avoid_ranges.pop()

    return ret

def get_submatrix_sum(prefix_sum, r1, c1, r2, c2):
    """
    Gets the sum of values in the rectangle from (r1,c1) to (r2,c2) inclusive.
    """
    # Convert to 1-indexed for prefix sum array
    r1, c1, r2, c2 = r1+1, c1+1, r2+1, c2+1
    
    return (
        prefix_sum[r2][c2] -
        prefix_sum[r1-1][c2] -
        prefix_sum[r2][c1-1] +
        prefix_sum[r1-1][c1-1]
    )