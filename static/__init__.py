class User:
    def __init__(self, name):
        self.name = name
        self.is_authenticated = False
        self.is_active = False
        self.is_anonymous = False

    def get_id(self):
        return self.name

