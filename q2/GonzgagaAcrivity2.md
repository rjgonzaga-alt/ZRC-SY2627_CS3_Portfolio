class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return self.name
        
    def set_name(self, name):
        self.name = name
        
    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount

    def calculate_bill(self):
        pass
        
class SeniorPatient(Patient):
    def calculate_bill(self):
        super().calculate_bill()  
        self.bill_amount *= 0.8
        print(f"Patient Name: {self.name}")
        print(f"Original bill of {self.name}: {self.bill_amount / 0.8} with a 20% senior citizen discount")
        print(f"final bill amount for {self.name} after senior citizen discount: {self.bill_amount}")

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        super().calculate_bill()  
        self.bill_amount *= 0.85 
        print(f"Patient Name: {self.name}")
        print(f"Original bill of {self.name}: {self.bill_amount / 0.85} with a 15% PhilHealth discount")
        print(f"final bill amount for {self.name} after PhilHealth discount: {self.bill_amount}")

patient1 = SeniorPatient("John Doe", 1000.0)
patient2 = PhilHealthPatient("Jane Smith", 1500.0)

patient1.calculate_bill()
patient2.calculate_bill()




