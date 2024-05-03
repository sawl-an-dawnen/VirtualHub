import Hub

Egypt_06 = Hub.Hub("Egypt", "TXEG", 244)

Egypt_06.add_equipment(104, "MX0158.TXEG", "cwdm", "Proposed")

#Egypt_06.add_customer(104, 1591, 1611, "JB00001541", "Texas Medical Center", "1234 APlace St", "12/05/2024", "This is where we write notes. The customer conduit is exposed on the 5th floor of the building.")

Egypt_06.display()

Egypt_06.display_sequence(104)

Egypt_06.display_all_traffic(104)