
import time

def download_file(filepath, delay):
    print(f"downloading first file.....{filepath}")
    time.sleep(delay)
    print(f"{filepath} downloaded.")

def main():

    # Record the start time
    start_time = time.time()
    
    
    download_file("file1", 2)
    download_file("file2", 1)
    download_file("file3", 3)
    

    # Calculate elapsed time
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"\nTotal execution time: {elapsed_time:.2f} seconds")
main()
    

