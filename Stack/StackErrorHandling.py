class StackIsEmpty(Exception):
    def __init__(self):
        self.error_message = 'Stack is empty'
        super().__init__(self.error_message)
    
    def __str__(self):
        return f'CustomException: {self.error_message}'
    