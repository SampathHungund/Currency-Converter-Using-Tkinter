import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

class CurrencyConverter:
    def __init__(self,root):
        self.root = root
        self.root.title("Currency Converter")
                
        self.amount_label = tk.Label(root , bg="orange" , text="Amount:")
        self.amount_label.pack()

        self.enter_amount = tk.Entry(root)
        self.enter_amount.pack()

        self.from_currency_label = tk.Label(root ,text="From Currency")
        self.from_currency_label.pack()

        self.from_currency_var = tk.StringVar(root)
        self.from_currency_var.set("INR")  
        self.from_currency_dropdown = ttk.Combobox(root, textvariable=self.from_currency_var)
        self.from_currency_dropdown['values'] = ["USD", "EUR", "JPY", "NZD", "RUB", "SAR", "LKR", "ZAR", "TWD", "ILS", "IDR", "ISK"]
        self.from_currency_dropdown.pack()

        self.to_currency_label = tk.Label(root, bg="lime green" , text="To Currency:")
        self.to_currency_label.pack()

        self.to_currency_var = tk.StringVar(root)
        self.to_currency_var.set("USD")  
        self.to_currency_dropdown = ttk.Combobox(root, textvariable=self.to_currency_var)
        self.to_currency_dropdown['values'] = ["INR", "EUR", "JPY", "GBP", "NZD", "RUB", "SAR", "LKR", "ZAR", "TWD", "ILS", "IDR", "ISK"]
        self.to_currency_dropdown.pack()
        
        self.convert_button = tk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
        root.geometry("400x400")
        root.configure(bg="blue")

    def convert_currency(self):
        amount = float(self.enter_amount.get())
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()

        c = CurrencyRates()
        converted_amount = c.convert(from_currency, to_currency, amount)

        self.result_label.config(text=f"{amount:} {from_currency} = {converted_amount:} {to_currency}")

if __name__ == "__main__":
    root = tk.Tk()
    converter = CurrencyConverter(root)
    root.mainloop()
