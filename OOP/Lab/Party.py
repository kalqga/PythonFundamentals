class Party:
    def __init__(self):
        self.people = []

    def going(self):
        return f"Going: {', '.join(self.people)}"

    def total(self):
        return f'Total: {len(self.people)}'


party = Party()

while True:
    command = input()

    if command == 'End':
        break

    party.people.append(command)

print(party.going())
print(party.total())
