import math

import matplotlib.pyplot as plt
import numpy as np


def annuity():
    # monthly annuity
    p = float(input("Starting Amount: "))
    r = float(input("Enter the percentage rate, converted to a decimal: "))
    t = float(input("How many year will this investment grow?: "))

    xmin = -10
    xmax = 10
    ymin = -10
    ymax = 10
    points = 10 * (xmax - xmin)
    x = np.linspace(xmin, xmax, points)

    fig, ax = plt.subplots()
    plt.axis([xmin, xmax, ymin, ymax])
    plt.plot([xmin, xmax], [0, 0], "black")
    plt.plot([0, 0], [ymin, ymax], "black")

    y1 = (p * (1 + r) ** t) / 12
    y2 = p * math.e ** (r * t)

    print("Annuity with monthly Growth is: ", round(y1, 2))
    print("Annuity with continuous Growth is: ", round(y2, 2))

    a = x**y1
    b = x**y2

    plt.plot(x, a, "red")
    plt.plot(x, b, "yellow")
    plt.show


def pmt():
    p = float(input("Amount borrowed: "))
    r = float(input("Annual percentage rate: "))
    t = float(input("Number of years: "))

    numerator = r / 12 * (1 + (r / 12)) ** (12 * t)
    denominator = (1 + (r / 12)) ** (12 * t) - 1
    pmt = p * (numerator / denominator)
    print(f"Monthly payment = ${pmt}")


def investment():
    p = float(input("Starting amount: "))
    r = float(input("Annual percentage rate: "))
    t = int(input("Number of years: "))
    monthly = float(input("Monthly contribution: "))
    annuity = p

    for _ in range(12 * t):
        annuity = annuity + monthly
        interest = annuity * r / 12
        annuity = annuity + interest
    print("Retirement Investment Balance = ", annuity)


def rate():
    p = float(input("Starting amount = "))
    r = float(input("Enter the percentage rate, converted to a decimal: "))
    t = float(input("How many years will this investment grow? "))
    a = p * (1 + r) ** t
    print("The annuity is ", a)


def log():
    base = float(input("base: "))
    result = float(input("result: "))
    exp = math.log(result, base)
    print("exponent = ", exp)


def notation():
    a = float(input("Enter a number to convert to scientific notation: "))
    x = math.floor(math.log(a, 10))
    n = round(a * 10 ** (-x), 2)
    print(f"{a} = {n} * 10^{x}")


# loop
def main():
    print("Welcome to the financial Calculator!")
    print("Select the function which you want to perform")
    print("  A) Annuity with monthly or continuous growth")
    print("  B) Monthly mortgage payment")
    print("  C) Estimate retirement investment balance")
    print("  D) Determine how long until an amount doubles, given the rate")
    print("  E) Solve logarithmic equations")
    print("  F) Convert to (and from) scientific notation")

    qst = str(input("Which Option You Choose? : "))

    match qst:
        case "A":
            annuity()
        case "B":
            pmt()
        case "C":
            investment()
        case "D":
            rate()
        case "E":
            log()
        case "F":
            notation()
        case _:
            print("Invalid Option")


if __name__ == "__main__":
    main()
