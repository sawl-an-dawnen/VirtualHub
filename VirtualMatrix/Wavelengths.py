class Wavelengths:
    wavelength = -1
    customer = None

    #initilization
    def __init__(self, wavelength):
        self.wavelength = wavelength

    #def __init__(self, wavelength, customer):
        #self.wavelength = wavelength
        #self.customer = Customer.Customer(customer)

    def display(self):
        print("Wavelength:", self.wavelength)
        self.customer.display()
        return