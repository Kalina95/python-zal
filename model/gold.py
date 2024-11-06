class Gold:

    def __init__(self, uid: int, date: str, price: float):
        self.uid = uid
        self.date = date
        self.price = price

    def __str__(self):
        return f"Gold: id={self.uid}; date={self.date}; price={self.price}"