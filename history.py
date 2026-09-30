class History:
    def __init__(self):
        self.records = []

    def add(self, expression, result):
        self.records.append((expression, result))

    def show(self):
        print("\n=== CALCULATION HISTORY ===")

        if not self.records:
            print("No calculations yet.")
            return

        for number, (expression, result) in enumerate(self.records, start=1):
            print(f"{number}. {expression} = {result}")

    def clear(self):
        self.records.clear()
