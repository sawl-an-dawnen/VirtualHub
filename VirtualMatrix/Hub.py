import Fiber

color_standards = ["Blue", "Orange", "Green", "Brown", "Red", "Black", "Grey", "White", "Yellow", "Violet", "Pink", "Aqua"]

class Hub:
    name = "" 
    shorthand = ""
    fibers = [] #an array of fiber objects, each

    #initilization

    def __init__(self, name, shorthand, size):
        self.name = name
        self.shorthand = shorthand
        self.fibers = []
        self.initilize_fibers(size)

    #region SET METHODS

    def set_name(self, name):
        self.name = name

    def set_shorthand(self, shorthand):
        self.shorthand = shorthand

    def initilize_fibers(self, count):
        i = 0
        for j in range(12):
            for k in range(12):
                if i >= count:
                    break
                self.fibers.append(Fiber.Fiber(i+1, color_standards[j], color_standards[k], "DARK", None))
                i += 1
    
    #endregion

    #region EQUIPMENT
                
    def add_equipment(self, sequence, name, type, status):
        fiber = self.fibers[sequence-1]
        if fiber.equipment == None:
            fiber.add_equipment(name, type, status)
            print("---EQUIPMENT ADDED---")
            self.display_sequence(sequence)
        else:
            print("---ERROR: Existing Equipment---")
            print("---ACTION CANCELLED---")
            self.display_sequence(sequence)

    def delete_equipment(self, sequence):
        self.fibers[sequence-1].delete_equipment()
        print("---EQUIPMENT REMOVED---")
        self.display_sequence(sequence)

    def get_equipment(self, sequence):
        return self.fibers[sequence-1]
    
    #endregion
    
    #region CUSTOMER

    def add_customer(self, sequence, fwd, rtn, jobNumber, name, address, date, notes):
        self.fibers[sequence-1].equipment.add_customer(fwd,rtn,jobNumber, name, address, date, notes)

    def delete_customer(self):
        pass

    def get_customer(self):
        pass
    
    #endregion

    #region DISPLAY METHODS

    def display(self):
        print("HUB Name:", self.name)
        print("Shorthand:", self.shorthand)
        print("Number of Fibers:", len(self.fibers))
        print()

    def display_sequence(self, sequence): 
        self.fibers[sequence-1].display()
        print()
    
    def display_all_traffic(self, sequence):
        self.fibers[sequence-1].equipment.display_all_traffic()
    
    #endregion
        
    def search_customer_name(self):
        pass
    def search_customer_job(self):
        pass
