from fpdf import FPDF

class HomeOfficeTable(FPDF):
    def __init__(self, company_name, standalone=False):
        super().__init__()
        self.company_name = company_name
        self.standalone = standalone

    def add_home_office_table(self):
        self.add_page()
        if self.standalone:
            self.set_title()


        # title = "Home Office Expenses - Form 8829"
        # self.set_font("Arial", "B", size=16)
        # self.set_fill_color(192, 192, 192)
        # self.cell(w=0, h=10, txt=title, border=1, align="C", ln=1, fill=True)
        # self.cell(w=0, h=10, txt=" ", border=0, ln=1)


        self.set_font("Arial", "b", size=12, )
        self.cell(0, 10, f" Name: {self.company_name}", ln=True, align="C")

        self.set_font("Arial", size=8, style="B")
        self.cell(0, 10, "This is simplified form and doesnt completely resembles form 8829 ", ln=True)

        self.set_font("Arial", size=10)

        # Add total square footage and business square footage lines
        self.cell(0, 10, "Total square footage of the home: ________", ln=True)
        self.cell(0, 10, "Square footage exclusively used for business: ________", ln=True)

        # Add table headers
        header = ["Description", "Amount"]
        col_widths = [125, 65]
        for i in range(len(header)):
            self.cell(col_widths[i], 10, header[i], 1)
        self.ln()

        # Add table rows
        expenses = [
            "Rent",
            "Mortgage interest",
            "Insurance",
            "Utilities",
            "Maintenance",
            "Property taxes",
            "Other"
        ]
        for expense in expenses:
            self.cell(col_widths[0], 10, expense, 1)
            self.cell(col_widths[1], 10, "$", 1)
            self.ln()

        # Add total, percentage, and adjusted total rows
        self.set_font("Arial", style="B")  # Set font style to bold
        self.cell(col_widths[0], 10, "Total", 1)
        self.cell(col_widths[1], 10, "$", 1)
        self.set_font("Arial", style="")  # Reset font style to normal

        self.ln()
        self.cell(col_widths[0], 10, "Business Use Percentage", 1)
        self.cell(col_widths[1], 10, "________%", 1)
        self.ln()
        self.set_font("Arial", style="B")  # Set font style to bold
        self.cell(col_widths[0], 10, "Adjusted Total", 1)
        self.cell(col_widths[1], 10, "$", 1)
        self.set_font("Arial", style="")
        self.ln()

        # Add additional information lines
        self.set_font("Arial", size=12, style="B")
        self.cell(0, 14, "Purchase Price of Home:", ln=True)

        self.set_font("Arial", size=12, style="")
        self.cell(0, 10, "House purchased date: ________", ln=True)
        self.cell(0, 10, "Place in service: ________", ln=True)
        self.cell(0, 10, "Purchase price: $________", ln=True)
        self.cell(0, 10, "Land value: $________", ln=True)
        self.cell(0, 10, "Adjusted basis: $________", ln=True)
        self.set_font("Arial", size=8, style="B")
        self.cell(0, 10,
                      "Note: Your accurate depreciation amount will be determined based on the depreciation method chosen and the business-use percentage.",
                    ln=True)
        self.set_font("Arial", size=12, style="B")
        self.cell(0, 14, "Please Sign and Date It: _______________________ and Date it: _________", ln=True)
        self.ln()
    def set_title(self):
        self.set_font("Arial", "B", size=16)
        self.set_fill_color(192, 192, 192)
        self.cell(w=0, h=10, txt="Auto Expense Report", border=1, align="C", ln=1, fill=True)
        self.cell(w=0, h=10, txt=" ", border=0, ln=1)



table = HomeOfficeTable('My Company')
table.add_home_office_table()
table.output('HomeOfficeTable.pdf', 'F')


