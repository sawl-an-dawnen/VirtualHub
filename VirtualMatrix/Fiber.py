import Mux

class Fiber:
    sequence = -1
    buffer = ""
    color = ""
    status = ""
    equipment = None
    
    #initilization
    
    def __init__(self, fiber_sequence, buffer_color, fiber_color, fiber_status, assigned_equipment):
        self.sequence = fiber_sequence
        self.buffer = buffer_color
        self.color = fiber_color
        self.status = fiber_status
        self.equipment = assigned_equipment

    #region EQUIPMENT

    def add_equipment(self, name, type, status):
        self.status = status
        self.equipment = Mux.Mux(name, type)

    def delete_equipment(self):
        self.status = "DARK"
        del self.equipment
        self.equipment = None
    
    def get_equipment(self):
        return self.equipment
    
    #endregion

    #region DISPLAY METHODS

    def display(self):
        print("Fiber Sequence:", self.sequence)
        print("Buffer Color:", self.buffer)
        print("Fiber Color:", self.color)
        print("Equipment Status:", self.status)
        if self.equipment == None:
            print("Attached equipment: None")
            return
        print("---Equipment---")
        self.equipment.display()

    #endregion

