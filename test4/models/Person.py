from Model import Model

class Person(Model):
    def __init__(self, values):
        super().__init__('Persona', 'keyStr', values)
    def __str__(self):
        return f"""Persona {super().__str__()}"""