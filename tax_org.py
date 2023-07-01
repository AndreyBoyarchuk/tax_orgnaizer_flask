from fpdf import FPDF
from home_office_table import HomeOfficeTable
from auto_expense_table import AutoExpenseTable
from datetime import datetime
import inspect
class TaxOrganizer(FPDF):
    def __init__(self, selected_categories, include_cogs, company_name, add_home_office, add_auto_expense,standalone=False):
        super().__init__()
        self.selected_categories = selected_categories
        self.include_cogs = include_cogs
        self.company_name = company_name
        self.add_home_office = add_home_office  # Store add_home_office as instance variable
        self.add_auto_expense = add_auto_expense
        self.current_section = "Tax Organizer"

        self.add_home_office_table = HomeOfficeTable.add_home_office_table.__get__(self)
        self.add_auto_expense_table = AutoExpenseTable.add_auto_expense_table.__get__(self)
        self.standalone = standalone

        # Define an alias for total number of pages
        self.alias_nb_pages(alias='{nb}')

    def header(self):
        # Now, it uses the current section as the title
        self.set_font("Arial", "B", size=16)
        self.set_fill_color(192, 150, 192)
        self.cell(w=0, h=10, txt=self.current_section, border=1, align="C", ln=1, fill=True)
        self.cell(w=0, h=10, txt=" ", border=0, ln=1)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Add company name to the left
        self.cell(0, 10, 'Company: %s' % self.company_name, 0, 0, 'L')
        # Page number
        self.set_x(100)
        self.cell(0, 10, 'Page %s of {nb}' % self.page_no(), 0, 0, 'C')

        # Add date and time to the right
        self.set_x(-50)
        self.cell(0, 10, 'Generated: %s' % datetime.now().strftime("%m/%d/%Y %I:%M %p"), 0, 0, 'R')

    def generate_report(self):
        self.add_page()
        # title = "Tax Organizer"
        # self.set_font("Arial", "B", size=16)
        # self.set_fill_color(192, 150, 192)
        # self.cell(w=0, h=10, txt=title, border=1, align="C", ln=1, fill=True)
        # self.cell(w=0, h=10, txt=" ", border=0, ln=1)

        # Add company name or sole proprietor name
        self.set_font("Arial", "b", size=12, )
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
            self.current_section = "Auto Expense Worksheet"
            self.add_auto_expense_table()

        if self.add_home_office:  # Only call the method if add_home_office is True
            self.current_section = "Home Office Worksheet"
            self.add_home_office_table()
        self.output("TaxOrganizerReport.pdf")

    def add_cost_of_goods_sold_section(self):
        self.set_font("Arial", size=10, style="B")
        self.cell(0, 10, "Cost of Goods Sold", ln=True)
        self.set_font("Arial", size=10)
        cogs_items = ["Beginning inventory", "Purchases", "Ending inventory"]
        for item in cogs_items:
            self.cell(0, 10, f"{item}: $________", ln=True)
        self.set_font("Arial", size=10, style="B")
        self.cell(0, 10, "Total Cost of Goods Sold: $__________", ln=True)
