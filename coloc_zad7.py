class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __add__(self, other):
        result_coeffs = []
        max_degree = max(len(self.coeffs), len(other.coeffs))
        for i in range(max_degree):
            coeff1 = self.coeffs[i] if i < len(self.coeffs) else 0
            coeff2 = other.coeffs[i] if i < len(other.coeffs) else 0
            result_coeffs.append(coeff1 + coeff2)
        return Polynomial(result_coeffs)

    def __sub__(self, other):
        result_coeffs = []
        max_degree = max(len(self.coeffs), len(other.coeffs))
        for i in range(max_degree):
            coeff1 = self.coeffs[i] if i < len(self.coeffs) else 0
            coeff2 = other.coeffs[i] if i < len(other.coeffs) else 0
            result_coeffs.append(coeff1 - coeff2)
        return Polynomial(result_coeffs)

    def __str__(self):
        terms = []
        for i, coeff in enumerate(self.coeffs):
            degree = len(self.coeffs) - i - 1
            if coeff == 0:
                continue
            elif degree == 0:
                terms.append(f"({coeff})")
            elif degree == 1:
                terms.append(f"({coeff}x)")
            else:
                terms.append(f"({coeff}x)^{degree}")
        return " + ".join(terms)

    def __len__(self):
        return len(self.coeffs)

    def __getitem__(self, i):
        if i > len(self.coeffs) - 1:
            return 0
        else:
            if i == len(self.coeffs) - 1:
                return str(self.coeffs[i])
            elif i == len(self.coeffs) - 2:
                return f"{self.coeffs[i]}x + "
            else:
                return f"{self.coeffs[i]}x^{len(self.coeffs) - i - 1} + "


p1 = Polynomial([2, 0, -1, 3])  # 2x^3 - x^2 + 3x - 2
p2 = Polynomial([1, -1, 1])  # x^2 - x + 1
print(p1)
print(p2)

p3 = p1 + p2  # 2x^3 + x^2 + 2x - 1
print(p3)

p4 = p1 - p2  # 2x^3 - 2x^2 + 4x - 3
print(p4)

p = Polynomial([1, 2, 3])
print(p[1])
