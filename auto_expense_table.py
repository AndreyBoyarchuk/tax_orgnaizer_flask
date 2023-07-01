from fpdf import FPDF

class AutoExpenseTable(FPDF):
    def __init__(self, company_name, standalone=False):
        super().__init__()
        self.company_name = company_name
        self.standalone = standalone




    def add_auto_expense_table(self):
        self.add_page()
        if self.standalone:
            self.set_title()
        # title = 'Auto Expense Report'
        # self.set_font("Arial", "B", size=16)
        # self.set_fill_color(192, 192, 192)
        # self.cell(w=0, h=10, txt=title, border=1, align="C", ln=1, fill=True)
        # self.cell(w=0, h=10, txt=" ", border=0, ln=1)

        self.set_font("Arial", "b", size=12, )
        self.cell(0, 10, f" Name: {self.company_name}", ln=True, align="C")
        self.set_font("Arial", size=8, style="B")

        self.set_font("Arial", size=10)
        expenses = [
            "Description of vehicle:",
            "Date placed in service:",
            "Describe business activity for multiple 1099:",
            "Odometer starting:",
            "Odometer ending:",
            "Business miles before July 1:",
            "Business miles after June 30:",
            "Other miles:"
        ]

        for expense in expenses:
            self.cell(0, 8, f"{expense} __________________", ln=True)

        self.cell(0, 8, "Full price of the car: $________", ln=True)

        self.cell(0, 8, "Will it be standard mileage or actual expenses? ___________________", ln=True)

        self.cell(w=0, h=7, txt="", border=0, ln=1)
        self.set_fill_color(192, 192, 192)
        self.cell(w=0, h=5, txt="Actual Expenses ", border=1, align="C", ln=1, fill=True)
        self.cell(w=0, h=5, txt=" ", border=0, ln=1)
        expense_categories = [
            "Gasoline:",
            "Oil:",
            "Repairs:",
            "Tires:",
            "Insurance:",
            "License, registration, and taxes:",
            "Other (specify):"
        ]

        self.set_font("Arial", size=8)
        for category in expense_categories:
            self.cell(0, 8, f"{category} $____________________", ln=True)
        self.set_font("Arial", size=10)
        self.cell(w=0, h=7, txt="", border=0, ln=1)
        self.set_fill_color(192, 192, 192)
        self.cell(w=0, h=5, txt="Pleae Verify this  ", border=1, align="C", ln=1, fill=True)
        self.cell(w=0, h=5, txt=" ", border=0, ln=1)
        self.set_font("Arial", size=10, style="B")
        self.cell(0, 10, "Was the vehicle used for personal off-duty hours? __________", ln=True)
        self.cell(0, 10, "Do you use another vehicle? __________", ln=True)
        self.cell(0, 10, "Do you have evidence to support this deduction (mileage log, app, etc.)? ____________________________", ln=True)
        self.cell(0, 14, "", ln=True)
        self.set_font("Arial", "B", size=12)
        self.cell(0, 10, "Signature: ________________________", ln=True)
        self.cell(0, 10, "Date: __________", ln=True)
        self.ln()
    def set_title(self):
        self.set_font("Arial", "B", size=16)
        self.set_fill_color(192, 192, 192)
        self.cell(w=0, h=10, txt="Auto Expense Report", border=1, align="C", ln=1, fill=True)
        self.cell(w=0, h=10, txt=" ", border=0, ln=1)


table = AutoExpenseTable("ABC Company")
table.add_auto_expense_table()
table.output("AutoExpenseTable.pdf")
