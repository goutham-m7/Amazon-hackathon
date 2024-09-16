import ast

def read_file_as_lists(filename):
    lists = []
    
    with open(filename, 'r') as file:
        for line in file:
            # Strip any extraneous whitespace and newlines
            line = line.strip()
            if line:
                try:
                    # Convert the line to a list using ast.literal_eval
                    list_from_line = ast.literal_eval(line)
                    if isinstance(list_from_line, list):
                        lists.append(list_from_line)
                    else:
                        print(f"Warning: The line does not evaluate to a list: {line}")
                except (ValueError, SyntaxError) as e:
                    print(f"Error parsing line: {line}\n{e}")
    
    return lists

# Usage
filename = 'new.txt'  # Replace with your actual file path
list_of_lists = read_file_as_lists(filename)

# For demonstration purposes, print the result
for lst in list_of_lists:
    print(lst)
