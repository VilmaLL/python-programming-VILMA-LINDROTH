class Village:

    def __init__(self, crop, clay, lumber, iron):
        self.crop = crop
        self.clay = clay
        self.lumber = lumber
        self.iron = iron

    def deposit(self, crop, clay, lumber, iron):
        Stock_max_cap = 800
     
        try:   
            if crop < 0 or clay < 0 or lumber < 0 or iron < 0:
                raise ValueError(f"you can't deposit a negative amount")

            self.crop += crop
            self.clay += clay
            self.lumber += lumber
            self.iron += iron

            if self.crop > Stock_max_cap:
                self.crop = Stock_max_cap
            elif self.clay > Stock_max_cap:
                self.clay = Stock_max_cap
            elif self.lumber > Stock_max_cap:
                self.lumber = Stock_max_cap
            elif self.iron > Stock_max_cap:
                self.iron = Stock_max_cap
            
        except ValueError as err:
            print(err)

    def withdraw(self, crop, clay, lumber, iron):
        try:
            if crop < 0 or clay < 0 or lumber < 0 or iron < 0:
                raise ValueError(f"you can't withdraw a negative amount")
            if crop > self.crop or clay > self.clay or lumber > self.lumber or iron > self.iron:
                raise ValueError(f"You can't withdraw more than you have in your stock")
            
            self.crop -= crop
            self.clay -= clay
            self.lumber -= lumber
            self.iron -= iron
        except ValueError as err:
            print(err)

    def check_stock(self):
        return {
            "crop" : self.crop,
            "clay" : self.clay,
            "lumber" : self.lumber,
            "iron" : self.iron
        }

    def __repr__(self):
        return f"Stock: Crop: {self.crop}/800 Clay: {self.clay}/800 Lumber: {self.lumber}/800 Iron: {self.iron}/800"
    


vill = Village(200, 200, 200, 200)
vill.deposit(700, 0, 200, 0)
vill.withdraw(0, 25, 0, 0)
print(vill)
