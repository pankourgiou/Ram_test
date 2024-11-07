import psutil
import time
import random
import string

# Function to track memory usage
def get_memory_usage():
    """Get current memory usage in MB."""
    process = psutil.Process()  # Current process
    memory_info = process.memory_info()
    return memory_info.rss / (1024 * 1024)  # Convert bytes to MB

# Function to simulate memory allocation
def stress_test_memory(size_in_mb):
    """Simulate memory usage by allocating a large list."""
    print(f"Starting memory stress test to allocate {size_in_mb} MB.")
    
    # Track initial memory usage
    initial_memory = get_memory_usage()
    print(f"Initial memory usage: {initial_memory:.2f} MB")

    # Allocate a large list of random strings to simulate memory usage
    data = []
    for _ in range(size_in_mb):
        random_str = ''.join(random.choices(string.ascii_letters, k=1024))  # 1 KB string
        data.append(random_str)

    # Track memory usage after allocation
    final_memory = get_memory_usage()
    print(f"Final memory usage: {final_memory:.2f} MB")

    # Print the memory difference
    memory_used = final_memory - initial_memory
    print(f"Memory used: {memory_used:.2f} MB")
    
    # Wait for the user to press Enter to release memory
    input("Press Enter to release memory...")

    # After the test, release memory by clearing the list and monitoring the drop in memory usage
    data.clear()

    # Final memory after clearing data
    final_memory_cleared = get_memory_usage()
    print(f"Memory usage after releasing data: {final_memory_cleared:.2f} MB")

# Running the memory test
if __name__ == "__main__":
    try:
        size_in_mb = int(input("Enter the memory size to allocate (in MB): "))
        stress_test_memory(size_in_mb)
    except ValueError:
        print("Please enter a valid integer for memory size.")
