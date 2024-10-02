class ReceiptGenrator:
    def __init__(self):
        self.items = []

    def add_item(self, name,price,quantity):
        item ={
            "name": name,
            "price":price,
            "quantity": quantity,
            "total":price * quantity            
        }
        self.items.append(item)  
            
    def calculat_totals(self, tax_rate,discount_rate):     
        subtotal = sum(item["total"] for item in self.items)   
        tax = subtotal * (tax_rate/ 100)
        discount = subtotal * (discount_rate / 100)
        final_total = subtotal + tax - discount
        return subtotal,tax,discount,final_total
    
    def display_receipt(self,tax_rate,discount_rate):
        subtotal,tax,discount_rate,final_total = self.calculat_totals(tax_rate,discount_rate)
        print("\n---RECEIPT---")
        print("Items:")
        
        for item in self.items:
            print(f"{item['name']}-{item['quantity']}{item['price']} = ₹{item['total']}")
            print(f"\nsubtotal:₹{subtotal}")
            print(f"\nDiscount:-₹{discount_rate}")        
            print(f"\nTax:-₹{tax}")        
            print(f"\nfinal Total:-₹{final_total}") 
            print("--- Thank you! ---")       
        
    def save_recepit(self,filename="recipt.txt"):
        with open(filename,"w", encoding="utf-8") as file:
            file.write("---REC---\n")
            file.write("Items:\n")
            
            for item in self.items:
                file.write(f"{item['name']} -{item['quantity']} x ₹{item['price']} = ₹{item['total']}\n")
           
            subtotal,tax,final_total,discount = self.calculat_totals(0,0)
            
            file.write("\nSubtotal: ₹" + str(round(subtotal)) + "\n")
            file.write("Discount: -₹" + str(round(discount)) + "\n")        
            file.write("Tax: +₹" + str(round(tax, 2)) + "\n")        
            file.write("Final Total: ₹" + str(round(final_total)) + "\n") 
            file.write("--- Thank you! ---\n")

receipt =ReceiptGenrator()

while True:
    name = input("Enter item name(or'done' And 'finish'):")
    if name.lower() == 'done':
        break
    price =float(input("Enter item price: ₹"))
    quantity =int(input("Enter item quantity: ₹"))
    receipt.add_item(name, price,quantity)
    
tax_rate = float(input("Enter tax rate(%): "))
discount_rate = float(input("Enter discount rate(%):"))

receipt.display_receipt(tax_rate, discount_rate)
receipt.save_recepit()    
    
    