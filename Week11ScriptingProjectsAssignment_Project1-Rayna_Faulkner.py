from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Tax Calculator")
        self.addLabel(text = "Gross Income", row = 0, column = 0)
        self.income = self.addFloatField(value = 0.00, row = 0, column = 1, columnspan = 2, precision = 2)
        self.addLabel(text = "Dependents", row = 1, column = 0)
        self.dependents = self.addIntegerField (value = 0, row = 1, column = 1)
        self.addButton("Compute", row = 2, column = 1, command = self.compute)
        self.addLabel (text = "Total Tax", row = 3, column = 0)
        self.totalTax = self.addFloatField(value = 0.0, row = 3, column = 1, precision = 2)
    def compute(self):
        rate = 0.20
        standard_deduction = 10000.0
        dependent_deduction = 3000.0
        try:
            numOfDependents = self.dependents.getNumber()
            grossIncome = self.income.getNumber()
        except ValueError:
            self.messageBox("Error Message", "Invalid Input")
            return
        taxableIncome = grossIncome - standard_deduction - (dependent_deduction * numOfDependents)
        incomeTax = taxableIncome * rate
        self.totalTax.setNumber(incomeTax)

def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()
