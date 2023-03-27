class Question:
    """Models a Question that can be used in a quiz"""
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer