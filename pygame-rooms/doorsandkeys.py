import time
import uuid

class Key:
    def __init__(self, id: uuid.UUID, key_name: str):
        self.id = id
        self.key_name = key_name
        
    def __str__(self):
        return self.key_name
    
class Lock:
    def __init__(self):
        self.id = uuid.uuid4()
        
    def issue_key(self, key_name):
        return Key(self.id, key_name)
    
lock = Lock()
key = lock.issue_key("hall key")
print(key)