import time
class Difficulty:
    def __init__(self):
        super().__init__()
# Settings of the difficulty level
    def set_difficulty(self, user_level):
        if user_level == "easy":
            time.sleep(0.1)
        elif user_level == "medium":
            time.sleep(0.08)
        elif user_level == "hard":
            time.sleep(0.05)
        elif user_level == "wtf":
            time.sleep(0.03)
