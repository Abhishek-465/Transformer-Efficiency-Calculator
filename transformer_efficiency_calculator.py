

def calculate_efficiency(output_power, core_losses, copper_losses):
    """
    Calculate the efficiency of a transformer.
    
    Parameters:
    - output_power (float): Power delivered to the load (in watts).
    - core_losses (float): Core losses (in watts).
    - copper_losses (float): Copper losses (in watts).
    
    Returns:
    - efficiency (float): Efficiency of the transformer in percentage.
    """
    # Calculate input power
    input_power = output_power + core_losses + copper_losses
    
    # Calculate efficiency
    efficiency = (output_power / input_power) * 100
    
    return efficiency

def main():
    print("Transformer Efficiency Calculator")
    
    try:
        # Input values
        output_power = float(input("Enter the output power (in watts): "))
        core_losses = float(input("Enter the core losses (in watts): "))
        copper_losses = float(input("Enter the copper losses (in watts): "))
        
        # Validate inputs
        if output_power < 0 or core_losses < 0 or copper_losses < 0:
            raise ValueError("Power values must be non-negative.")
        
        # Calculate efficiency
        efficiency = calculate_efficiency(output_power, core_losses, copper_losses)
        
        # Output result
        print(f"\nTransformer Efficiency: {efficiency:.2f}%")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
