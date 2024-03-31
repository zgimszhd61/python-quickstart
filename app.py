# people.py

from memory import Memory
import time

def main():
    # Initialize memory object
    memory = Memory()
    
    # Data to be saved
    data_to_save = "This is a piece of data to remember."
    
    # Save data to memory
    memory.save(data_to_save)
    
    # Sleep for 1 seconds
    time.sleep(1)
    
    # Retrieve data from memory
    retrieved_data = memory.retrieve()
    print(retrieved_data)

if __name__ == "__main__":
    main()
