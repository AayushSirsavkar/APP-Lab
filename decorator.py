# Define a decorator for formatting
def bold_text(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper


# Define the Report class
class Report:

    # Class variable for storing templates
    templates = {}

    # Constructor to initialize the report with title and content
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class method to add a template
    @classmethod
    def add_template(cls, name, template):
        cls.templates[name] = template

    # Class method to retrieve a template
    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    # Magic method to call a report instance with a template name
    def __call__(self, template_name):
        template = self.get_template(template_name)

        if template:
            return template(self)
        else:
            return "Template not found"

    # String representation of the report
    def __str__(self):
        return f"Report: {self.title}\nContent: {self.content}"


# Define a simple template function
def simple_template(report):
    return f"{report.title}\n{report.content}"


# Define a fancy template function with bold formatting
@bold_text
def fancy_template(report):
    return f"{report.title}\n{report.content}"


# Main function to generate and display reports
def main():

    # Add templates to the Report class
    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    # Create a report instance
    report = Report(
        "Monthly Sales Report",
        "Sales increased by 20% this month."
    )

    # Generate reports with different templates
    simple_report = report("simple")
    fancy_report = report("fancy")

    # Display the reports
    print("Simple Report:")
    print(simple_report)

    print("\nFancy Report:")
    print(fancy_report)

    print("\nUsing __str__ method:")
    print(report)


# Run the main function
if __name__ == "__main__":
    main()
