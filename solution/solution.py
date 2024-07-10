from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        status = list()  # Initialize an empty list to simulate the folder stack
        
        for operation in logs:
            if operation == "../":  # Handle going back to the parent folder
                if status:  # Check if there are folders in the stack
                    status.pop()  # Pop the last folder to move back
            elif operation == "./":  # Ignore the current folder operation
                continue
            else:  # Handle moving into a child folder
                status.append(operation[:-1])  # Add the folder name to the stack
        
        return len(status)  # Return the number of folders left in the stack, representing the minimum operations
