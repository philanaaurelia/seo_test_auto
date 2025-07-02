
class InternManager:
    def __init__(self):
        self.interns = []

    def add_intern(self, name):
        if name not in self.interns:
            self.interns.append(name)
            return True
        return False

    def remove_intern(self, name ):
        if name in self.interns:
            self.interns.remove(name)
            return True
        return False

    def get_intern_list(self):
        return self.interns

    def clear_interns(self):
        self.interns.clear()
        return True

    def find_intern(self, name):
        return name in self.interns
