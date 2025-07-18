from items.item import Item
import uuid

class Key(Item):
    def __init__(self, name, secret_id = None):
        super().__init__(name)
        self.secret_id = secret_id or uuid.uuid4()

    def __str__(self):
        return f"{self.name}"

    def get_secret(self):
        return self.secret_id
