import Wavelengths
import Customer

default_cwdm_frequencies = [1471,1491,1511,1551,1531,1571,1591,1611]
default_12ch_dwdm_channels = [50,51,52,53,54,55,56,57,58,59,60,61]
default_16ch_dwdm_channels = [25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40] 
#default_mux_types = enumerate(["cwdm", "12ch_dwdm", "16ch_dwdm"])

class Mux:
    name = ""
    type = ""
    wavelengths = []

    #initilization
    def __init__(self, name, type):
        self.name = name
        self.type = type
        match type:
            case "cwdm":
                for w in default_cwdm_frequencies:
                    self.wavelengths.append(Wavelengths.Wavelengths(w))
            case "12ch_dwdm":
                for w in default_12ch_dwdm_channels:
                    self.wavelengths.append(Wavelengths.Wavelengths(w))
            case "16ch_dwdm":
                for w in default_16ch_dwdm_channels:
                    self.wavelengths.append(Wavelengths.Wavelengths(w))
    
    def search_wavelength(self, wavelength):
        i = 0
        for w in self.wavelengths:
            if w.wavelength == wavelength:
                return i
            i += 1
        return -1

    #region CUSTOMER

    def add_customer(self, fwd, rtn, jobNumber, name, address, date, notes):
        if self.wavelengths[self.search_wavelength(fwd)].customer != None:
            print("---ERROR: Existing Customer---")
            print("---CONFLICTING TRAFFIC---")
            self.display_traffic(fwd)
            print("---ACTION CANCELLED---")
            return
        if self.wavelengths[self.search_wavelength(rtn)].customer != None:
            print("---ERROR: Existing Customer---")
            print("---CONFLICTING TRAFFIC---")
            self.display_traffic(rtn)
            print("---ACTION CANCELLED---")
            return
        customer = Customer.Customer(jobNumber, name, address, date, notes)
        self.wavelengths[self.search_wavelength(fwd)].customer = customer
        self.wavelengths[self.search_wavelength(rtn)].customer = customer
    
    def delete_customer(self, wavelength):
        if self.search_wavelength(wavelength) != -1:
            del self.wavelengths[self.search_wavelength(wavelength)].customer
            self.wavelengths[self.search_wavelength(wavelength)].customer = None

    def get_customer(self, wavelength):
        if self.search_wavelength(wavelength) != -1:
            return self.wavelengths[self.search_wavelength(wavelength)].customer
        return None

    #endregion

    #region DISPLAY METHODS

    def display(self):
        print("MUX Type:", self.type.upper())
        print("Identification number:", self.name)

    def display_all_traffic(self):
        print("---",self.name,"---")
        for w in self.wavelengths:
            if w.customer != None:
                print("---", w.wavelength, "---")
                w.customer.display()
            else:
                print(w.wavelength,": None")

    def display_traffic(self, wavelength):
        self.wavelengths[self.search_wavelength(wavelength)].display()

    #endregion
