class APIException(Exception):
    def __init__(self, message="Invalid credentials or API error"):
        self.message = message
        super().__init__(self.message)
