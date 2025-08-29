# Smartphone Class Example

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.is_on = False  # default state

    # Method to turn on the phone
    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    # Method to turn off the phone
    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    # Method to check storage
    def check_storage(self):
        print(f"{self.brand} {self.model} has {self.storage} GB storage.")

# Creating objects
phone1 = Smartphone("Apple", "iPhone 14", 128)
phone2 = Smartphone("Samsung", "Galaxy S23", 256)

phone1.power_on()
phone1.check_storage()

phone2.power_on()
phone2.power_off()
