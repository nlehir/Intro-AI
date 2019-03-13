
class Character():
    def __init__(self):
        self.status = 'suspect'
        self.color = None
        self.position = 0

    def update(self, report: str) -> None:
        __, self.position, status = report.split('-')
        if self.status != status:
            self.status = status
            print(self.color + " a été innocenté")

    def __str__(self):
        return f"{self.color}-{self.position}-{self.status}"


class Red(Character):
    def __init__(self):
        super().__init__()
        self.color = 'rouge'


class Blue(Character):
    def __init__(self):
        super().__init__()
        self.color = 'bleu'


class Grey(Character):
    def __init__(self):
        super().__init__()
        self.color = 'gris'


class Black(Character):
    def __init__(self):
        super().__init__()
        self.color = 'noir'


class Violet(Character):
    def __init__(self):
        super().__init__()
        self.color = 'violet'


class Pink(Character):
    def __init__(self):
        super().__init__()
        self.color = 'rose'


class White(Character):
    def __init__(self):
        super().__init__()
        self.color = 'blanc'


class Brown(Character):
    def __init__(self):
        super().__init__()
        self.color = 'marron'
