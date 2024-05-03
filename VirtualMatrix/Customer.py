class Customer:
    jobNumber = ""
    name = ""
    address = ""
    date = ""
    notes = ""

    #initilization
    def __init__(self, jobNumber, name, address, date, notes):
        self.jobNumber = jobNumber
        self.name = name
        self.address = address
        self.date = date
        self.notes = notes

    #region DISPLAY METHODS

    def display(self):
        print(self.jobNumber, "-", self.name, "-", self.date)

    def display_details(self):
        print("Customer Info:")
        print("Job Number:", self.jobNumber)
        print("Customer Name", self.name)
        print("Address:", self.address)
        print("Modified Date:", self.date)
        print("Notes:", self.notes)

    #endregion