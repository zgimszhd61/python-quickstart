```python
# memory.py

class Memory:
    def __init__(self):
        self.data = None

    def save(self, data):
        self.data = data
        print("Data saved to memory.")

    def retrieve(self):
        print("Data retrieved from memory.")
        return self.data
```

```python
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
    
    # Sleep for 2 seconds
    time.sleep(2)
    
    # Retrieve data from memory
    retrieved_data = memory.retrieve()
    print(retrieved_data)

if __name__ == "__main__":
    main()
```

在`memory.py`文件中，我们定义了一个`Memory`类，它具有两个方法：`save()`用于保存数据，`retrieve()`用于检索数据。这个类有一个实例变量`data`，用于存储记忆。

在`people.py`文件中，我们定义了一个`main`函数，它首先初始化`Memory`类的一个实例。然后，它使用`save()`方法保存一条数据，等待2秒钟，最后使用`retrieve()`方法检索并打印出保存的数据。通过`if __name__ == "__main__":`检查，我们确保只有当`people.py`作为主程序运行时，`main()`函数才会被调用。
