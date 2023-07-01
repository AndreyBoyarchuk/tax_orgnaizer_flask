from flask import Flask, render_template, request, send_file,session,redirect,url_for
import json
import os
from tax_org import TaxOrganizer
from home_office_table import HomeOfficeTable
from auto_expense_table import AutoExpenseTable
from revenue_report import RevenueReport

app = Flask(__name__)
app.secret_key = 'fdfdfdff'
# Load categories from the JSON file
@app.route("/choose_json", methods=["POST"])
def choose_json():
    json_file = request.form.get("json_choice", "categories1.json")
    with open(json_file, "r") as f:
        categories = json.load(f)
    session['categories'] = categories
    return render_template("index.html", categories=categories, current_json=json_file)

@app.route("/")
def index():
    categories = session.get('categories')  # Get the categories from session
    if not categories:  # If no categories in session
        with open("categories1.json", "r") as f:  # Open default JSON file
            categories = json.load(f)
    return render_template("index.html", categories=categories)

@app.route("/", methods=["POST"])
def handle_action():
    company_name = request.form["company_name"]
    selected_categories = request.form.getlist("categories")
    include_cogs = "include_cogs" in request.form
    include_home_office = "include_home_office" in request.form
    include_auto_expenses = "include_auto_expenses" in request.form
    action = request.form["action"]
    current_header = "Tax Organizer"
    if action == "Generate Tax Organizer":
        tax_organizer = TaxOrganizer(selected_categories, include_cogs, company_name,  include_home_office, include_auto_expenses)
        tax_organizer.generate_report()

        if os.path.exists("TaxOrganizerReport.pdf"):
            return send_file("TaxOrganizerReport.pdf", as_attachment=True, download_name="TaxOrganizerReport.pdf")
        else:
            return "Error: Could not generate report."
    elif action == "Generate Revenue Report":
        revenue_report = RevenueReport(company_name)  # Initialize your revenue report class
        revenue_report.generate_report()  # Call the method to generate the revenue report

        if os.path.exists("RevenueReport.pdf"):
            return send_file("RevenueReport.pdf", as_attachment=True, download_name="RevenueReport.pdf")
        else:
            return "Error: Could not generate revenue report."
    elif action == "Generate Home Office Table":
        home_office_table = HomeOfficeTable(company_name, standalone=True)
        home_office_table.add_home_office_table()
        home_office_table.output('HomeOfficeTable.pdf', 'F')

        if os.path.exists("HomeOfficeTable.pdf"):
            return send_file("HomeOfficeTable.pdf", as_attachment=True, download_name="HomeOfficeTable.pdf")
        else:
            return "Error: Could not generate home office table."

    elif action == "Generate Auto Expense Table":
        table = AutoExpenseTable(company_name, standalone=True)
        table.add_auto_expense_table()
        table.output("AutoExpenseTable.pdf")

        if os.path.exists("AutoExpenseTable.pdf"):
            return send_file("AutoExpenseTable.pdf", as_attachment=True, download_name="AutoExpenseTable.pdf")
        else:
            return "Error: Could not generate auto expense table."

    else:
        return "Invalid action."

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    files = os.listdir('.')  # Adjust this to wherever your .json files are located
    json_files = [file for file in files if file.endswith('.json')]
    file = request.args.get('file')

    if request.method == 'POST':
        data = {}
        categories = request.form.getlist('category')
        for category in categories:
            subcategories = request.form.getlist(category)
            deletions = request.form.getlist('delete_' + category)
            data[category] = [sub for sub in subcategories if sub not in deletions]
        with open(file, 'w') as f:
            json.dump(data, f)
        return redirect(url_for('edit', file=file))
    else:
        data = None
        if file:
            with open(file, 'r') as f:
                data = json.load(f)
        return render_template('edit.html', files=json_files, data=data, file=file)


if __name__ == "__main__":
    app.run(debug=True)
