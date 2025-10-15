class Frac:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator
        self.simplify()

    @property
    def nominator(self):
        return self._nominator
    
    @nominator.setter
    def nominator(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Nominator must be int not {type(value)}")
        self._nominator = value
    
    @property
    def denominator(self):
        return self._denominator
    
    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Denominator must be int not {type(value)}")
        if value == 0:
            raise ValueError("Denominator cannot be zero")
        self._denominator = value

    def __add__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        new_nominator = self.nominator * other.denominator + other.nominator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Frac(new_nominator, new_denominator)
    
    def __sub__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        new_nominator = self.nominator * other.denominator - other.nominator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Frac(new_nominator, new_denominator)
    
    def __mul__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        elif not isinstance(other, Frac):
            return NotImplemented
        new_nominator = self.nominator * other.nominator
        new_denominator = self.denominator * other.denominator
        return Frac(new_nominator, new_denominator)
    
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        if other.nominator == 0:
            raise ZeroDivisionError("You can't divide by zero")
        new_nominator = self.nominator * other.denominator
        new_denominator = self.denominator * other.nominator
        return Frac(new_nominator, new_denominator)
    
    def simplify(self, value = None):
        if value is None:
            value = min(self.nominator, self.denominator)
        if self.nominator % value == 0 and self.denominator % value == 0:
            self.nominator //= value
            self.denominator //= value
        else:
            self.simplify(value - 1)
        return self
    
    def __str__(self):
        return f"{self.nominator}/{self.denominator}"
    
    def mixed(self):
        whole = self.nominator // self.denominator
        remainder = abs(self.nominator % self.denominator)
        if remainder == 0:
            return str(whole)
        return f"{whole} {remainder}/{self.denominator}"
    
    def __eq__(self, other):
        return self.nominator * other.denominator == self.denominator * other.nominator

print(Frac(1, 2) + Frac(1, 3))
print(Frac(1, 2) - Frac(1, 3))
print(Frac(7, 6).mixed())
print(3 * Frac(1, 2))
print(Frac(1, 2) * 3)
print(Frac(1, 4) + 2)
print(Frac(1, 4) / Frac(1, 2))
print(Frac(2, 4) == Frac(1, 2))
f = Frac(3, 4)
f += 2
print(f)


