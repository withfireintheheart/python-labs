from math import sqrt, pi, exp

def calculate(a:float, b:float, c: float):
	return (1.0 * (c * sqrt(2.0*pi))) * exp(-(pow(a-b, 2.0) / 2.0 * pow(c,2.0)))

	if __name__ == '__main__':
		a = float(input("a = "))
		b = float(input("b = "))
		c = float(input("c = "))

		result = calculate(a,b,c)
		print("Calculated number = ",result)