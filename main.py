from process_file import parse_matrix_file
from max_profit import maxProfit

files = ["test_files_input/example.0.in.txt", "test_files_input/example.1.in.txt", "test_files_input/example.2.in.txt", "test_files_input/example.3.in.txt","test_files_input/example.4.in.txt", "test_files_input/example.5.in.txt"]
correct = [7,14,62,-3,28,671]


for i, file in enumerate(files):
    matrix = parse_matrix_file(file)
    
    res = maxProfit(matrix, [], 0)

    if res == correct[i]:
        print(f"Test {i}: TRUE")
    else:
        print(f"Test {i}: FALSE")
    
    

    # Display the matrix
    # print("\nParsed matrix:")
    # for row in matrix:
    #     print(row)