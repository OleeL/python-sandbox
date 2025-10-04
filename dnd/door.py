class Door():
    def __init__(self, key, description = "Door", is_locked=True):
        self.lock_id = key.get_secret()
        self.description = description
        self.is_locked = is_locked

    def use_key(self, key):
        # If the key matches and the door is locked, unlock it
        if self.is_locked and key.secret_id == self.lock_id:
            self.is_locked = False
            return True
        return False

    def __str__(self):
        return f"{self.is_locked and "A locked" or "An unlocked"} {self.description}"
