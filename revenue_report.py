from fpdf import FPDF

class RevenueReport(FPDF):
    def __init__(self, company_name):
        super().__init__()
        self.company_name = company_name

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f'Revenue Report for {self.company_name}', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_revenue_section(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

    def generate_report(self):
        self.add_revenue_section("Q1 2023", "In Q1 2023, our revenue was...")
        self.add_revenue_section("Q2 2023", "In Q2 2023, our revenue increased by...")

        # Save the PDF to a file
        self.output("RevenueReport.pdf")
