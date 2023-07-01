from fpdf import FPDF

class TaxOrganizer(FPDF):
    def __init__(self, selected_categories, include_cogs, company_name, add_home_office, add_auto_expense):
        super().__init__()
        self.selected_categories = selected_categories
        self.include_cogs = include_cogs
        self.company_name = company_name
        self.add_home_office = add_home_office  # Store add_home_office as instance variable
        self.add_auto_expense = add_auto_expense


    def generate_report(self):
        self.add_page()
        self.set_font("Arial", "B", size=16)
        self.cell(0, 10, "Tax Organizer Report", ln=True, align="C")

        # Add company name or sole proprietor name
        self.set_font( "Arial", "b",size=12,)
        self.cell(0, 10, f" Name: {self.company_name}", ln=True, align="C")

        self.set_font("Arial", "b", size=12)
        self.cell(0, 10, "Total Income: S _________", ln=True)

        if self.include_cogs:
            self.add_cost_of_goods_sold_section()

        self.set_font("Arial", size=10)
        for category in self.selected_categories:
            self.cell(0, 10, f"{category}: $________", ln=True)

##Singnauture Block
        self.cell(0, 14, "", ln=True)
        self.set_font("Arial", "B", size=12)
        self.cell(0, 10, "Signature: ________________________", ln=True)
        self.cell(0, 10, "Date: __________", ln=True)
##End Singnauture Block
        if self.add_auto_expense:
            self.add_auto_expense_table()

        if self.add_home_office:  # Only call the method if add_home_office is True
            self.add_home_office_table()

        self.output("TaxOrganizerReport.pdf")



    # ... (rest of the code)


    def add_cost_of_goods_sold_section(self):
        self.set_font("Arial", size=10, style="B")
        self.cell(0, 10, "Cost of Goods Sold", ln=True)

        self.set_font("Arial", size=10)
        cogs_items = ["Beginning inventory", "Purchases", "Ending inventory"]
        for item in cogs_items:
            self.cell(0, 10, f"{item}: $________", ln=True)
        self.set_font("Arial", size=10, style="B")
        self.cell(0, 10, "Total Cost of Goods Sold: $__________", ln=True)

    def add_home_office_table(self):
        self.add_page()
        self.set_font("Arial", size=16 , style="B")
        title = "Home Office Expenses - Form 8829"
        self.cell(0, 10, title, ln=True, align="C")
        self.set_font("Arial", "b", size=12, )
        self.cell(0, 10, f" Name: {self.company_name}", ln=True, align="C")
        self.set_font("Arial", size=8, style="B")
        self.cell(0, 10, "This is simlified form and doesnt copmletelly resembles form 8829 ", ln=True)

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

    def add_auto_expense_table(self):
        self.add_page()
        self.set_font("Arial", "B", size=16)
        self.set_fill_color(192, 192, 192)
        self.cell(w=0, h=10, txt="Auto Expense Report  ", border=1, align="C", ln=1, fill=True)
        self.cell(w=0, h=10, txt=" ", border=0, ln=1)

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
        self.cell(0, 10,
                      "Do you have evidence to support this deduction (mileage log, app, etc.)? ____________________________",
                      ln=True)
        self.cell(0, 14, "", ln=True)
        self.set_font("Arial", "B", size=12)
        self.cell(0, 10, "Signature: ________________________", ln=True)
        self.cell(0, 10, "Date: __________", ln=True)
        self.ln()


