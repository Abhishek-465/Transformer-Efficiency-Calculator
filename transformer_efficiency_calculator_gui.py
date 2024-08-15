

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class TransformerEfficiencyCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Transformer Efficiency Calculator")
        
        # Create the main frame
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        self.title = ttk.Label(self.frame, text="Transformer Efficiency Calculator", font=("Helvetica", 16))
        self.title.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Input fields
        self.create_input_field("Output Power (W):", 1)
        self.create_input_field("Core Losses (W):", 2)
        self.create_input_field("Copper Losses (W):", 3)
        
        # Calculate Button
        self.calculate_button = ttk.Button(self.frame, text="Calculate Efficiency", command=self.calculate_efficiency)
        self.calculate_button.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Result label
        self.result_label = ttk.Label(self.frame, text="", font=("Helvetica", 14))
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    def create_input_field(self, label_text, row):
        """Create an input field with a label."""
        label = ttk.Label(self.frame, text=label_text)
        label.grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        entry = ttk.Entry(self.frame, width=20)
        entry.grid(row=row, column=1, padx=5, pady=5)
        setattr(self, f"entry_{row}", entry)

    def calculate_efficiency(self):
        """Calculate and display the efficiency."""
        try:
            # Retrieve input values
            output_power = float(self.entry_1.get())
            core_losses = float(self.entry_2.get())
            copper_losses = float(self.entry_3.get())
            
            # Validate inputs
            if output_power < 0 or core_losses < 0 or copper_losses < 0:
                raise ValueError("Power values must be non-negative.")
            
            # Calculate input power
            input_power = output_power + core_losses + copper_losses
            
            # Calculate efficiency
            efficiency = (output_power / input_power) * 100
            
            # Display result
            self.result_label.config(text=f"Transformer Efficiency: {efficiency:.2f}%")
        
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

def main():
    root = tk.Tk()
    app = TransformerEfficiencyCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
