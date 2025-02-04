'''\
Unified Computational State Transformer Module

This module integrates number system conversions, truth table processing,
K-Map generation, and Gray code mapping into a single unified transformation
engine.

Modules:
  - NumberSystemTransformer: converts numbers between bases.
  - TruthTableProcessor: generates truth tables from numeric states.
  - KMapGenerator: creates K-Map projections.
  - GrayCodeIdentifier: maps binary states to Gray code.
  - UnifiedNumberTransformer: integrates the above components.

Author: Your Name
Date: 2023-10-XX
'''

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../conversions/python"))
from number_conversion_interactive import show_decimal_to_binary_steps, show_ieee754_visualization, show_multi_base_layout

class NumberSystemTransformer:
    def convert(self, value):
        # Convert the input number to a binary string representation
        try:
            n = abs(int(float(value)))
            return format(n, 'b')
        except ValueError:
            return ''


class TruthTableProcessor:
    def process(self, binary_str):
        # Generate a simple truth table from a binary string
        # Each row is a dictionary with the bit position and bit value
        truth_table = []
        for index, bit in enumerate(binary_str):
            truth_table.append({'position': index, 'bit': bit})
        return truth_table


class KMapGenerator:
    def generate(self, truth_table):
        # Create a dummy K-Map projection for demonstration purposes
        # Assuming a simple 2-variable K-Map with columns: '00', '01', '11', '10'
        kmap = {'x2_0': [0, 0, 0, 0], 'x2_1': [0, 0, 0, 0]}
        if truth_table:
            # For demonstration, fill the first cell with the first bit's integer value
            try:
                kmap['x2_0'][0] = int(truth_table[0]['bit'])
            except ValueError:
                pass
        return kmap


class GrayCodeIdentifier:
    def apply_gray_code_mapping(self, truth_table):
        # Apply Gray code conversion to each row in the truth table
        # Gray code conversion: gray = binary ^ (binary >> 1)
        def to_gray(n):
            return n ^ (n >> 1)
        gray_table = []
        for row in truth_table:
            try:
                bit_val = int(row['bit'])
                gray_val = to_gray(bit_val)
                new_row = dict(row)
                new_row['gray'] = gray_val
                gray_table.append(new_row)
            except ValueError:
                new_row = dict(row)
                new_row['gray'] = row['bit']
                gray_table.append(new_row)
        return gray_table


class DefaultLanguageAdapter:
    def adapt(self, computational_state, target_language='python'):
        # For now, simply return the computational state without changes
        return computational_state


class UnifiedNumberTransformer:
    def __init__(self, language_adapter=None):
        self.language_adapter = language_adapter or DefaultLanguageAdapter()
        self.number_converter = NumberSystemTransformer()
        self.truth_table_processor = TruthTableProcessor()
        self.kmap_generator = KMapGenerator()
        self.gray_code_analyzer = GrayCodeIdentifier()

    def transform_computational_state(self, input_value):
        # Convert number using number system transformer
        converted_state = self.number_converter.convert(input_value)

        # Process the truth table from the binary representation
        truth_table = self.truth_table_processor.process(converted_state)

        # Generate the K-Map representation
        kmap_rep = self.kmap_generator.generate(truth_table)

        # Apply Gray code mapping to the truth table
        gray_coded_states = self.gray_code_analyzer.apply_gray_code_mapping(truth_table)

        # Adapt the computational state if needed
        adapted_state = self.language_adapter.adapt(kmap_rep, target_language='python')

        return {
            'converted_state': converted_state,
            'truth_table': truth_table,
            'kmap_representation': kmap_rep,
            'gray_coded_states': gray_coded_states,
            'adapted_state': adapted_state
        }


def display_transformation_result(result):
    print("\n=== Unified Transformation Result ===\n")
    print(f"Converted State: {result['converted_state']}\n")
    print("Digital Design Best Practices Summary:")
    print("  1. Begin with a comprehensive truth table that captures all input combinations and their outputs.")
    print("  2. Leverage Karnaugh Maps (K-maps) with Gray code ordering to simplify and validate Boolean expressions.")
    print("  3. Adapt the computational state into Python for effective simulation and further analysis.")
    print("Follow these guidelines to design, analyze, and validate digital circuits accurately.\n")

    for i, tt in enumerate(result['truth_tables']):
        print(f"Truth Table {i+1}:")
        print("This section provides a detailed view of each bit's logic state and its Gray code conversion.")
        print("{:<10} {:<10} {:<10}".format("Index", "Bit", "Gray"))
        for row in result['gray_coded_states_list'][i]:
            print("{:<10} {:<10} {:<10}".format(row['position'], row['bit'], row['gray']))

        print("\nK-Map Representation:")
        print("The Karnaugh Map (K-Map) aids in simplifying Boolean expressions by visually grouping adjacent bits.")
        for key, value in result['kmap_representations'][i].items():
            print(f"{key}: {value}")

        print("\nAdapted State:")
        print("The Adapted State bridges the raw digital computations and their representation in Python.")
        print("{:<10} {:<30}".format("Key", "Value"))
        for key, value in result['adapted_states'][i].items():
            print("{:<10} {:<30}".format(key, str(value)))
        print("\n" + "="*40 + "\n")


def add_extra_rows(truth_table):
    print("Adding extra rows to the current truth table.")
    while True:
        row_input = input("Enter extra row as 'position,bit' (or type 'done' to finish, 'view' to display table, 'bulk:' to enter multiple rows): ")
        if row_input.lower() == 'done':
            break
        elif row_input.lower() == 'view':
            print("\nCurrent Truth Table:")
            for row in truth_table:
                print(row)
            continue
        elif row_input.lower().startswith('bulk:'):
            bulk_data = row_input[5:].strip()
            entries = [entry.strip() for entry in bulk_data.split(';') if entry.strip()]
            for entry in entries:
                parts = entry.split(',')
                if len(parts) != 2:
                    print(f"Invalid bulk entry: {entry}. Expected format 'position,bit'.")
                    continue
                try:
                    pos = int(parts[0].strip())
                    bit = parts[1].strip()
                    truth_table.append({'position': pos, 'bit': bit})
                except Exception as e:
                    print(f"Error processing entry {entry}: {e}")
            continue
        elif row_input.strip() == "":
            print("Empty input. Please enter valid data.")
            continue
        else:
            parts = row_input.split(',')
            if len(parts) != 2:
                print("Invalid input format. Please enter in the format 'position,bit'.")
                continue
            try:
                pos = int(parts[0].strip())
                bit = parts[1].strip()
                truth_table.append({'position': pos, 'bit': bit})
            except Exception as e:
                print(f"Error processing input: {e}")
    # Sort the truth table by position
    truth_table = sorted(truth_table, key=lambda x: x['position'])
    return truth_table


def create_new_truth_table():
    print("Creating a new truth table.")
    new_table = []
    while True:
        row_input = input("Enter row as 'position,bit' (or type 'done' to finish, 'view' to display current table, 'bulk:' for multiple rows): ")
        if row_input.lower() == 'done':
            break
        elif row_input.lower() == 'view':
            print("\nCurrent New Truth Table:")
            for row in new_table:
                print(row)
            continue
        elif row_input.lower().startswith('bulk:'):
            bulk_data = row_input[5:].strip()
            entries = [entry.strip() for entry in bulk_data.split(';') if entry.strip()]
            for entry in entries:
                parts = entry.split(',')
                if len(parts) != 2:
                    print(f"Invalid bulk entry: {entry}. Expected format 'position,bit'.")
                    continue
                try:
                    pos = int(parts[0].strip())
                    bit = parts[1].strip()
                    new_table.append({'position': pos, 'bit': bit})
                except Exception as e:
                    print(f"Error processing entry {entry}: {e}")
            continue
        elif row_input.strip() == "":
            print("Empty input. Please enter valid data.")
            continue
        else:
            parts = row_input.split(',')
            if len(parts) != 2:
                print("Invalid input format. Please enter in the format 'position,bit'.")
                continue
            try:
                pos = int(parts[0].strip())
                bit = parts[1].strip()
                new_table.append({'position': pos, 'bit': bit})
            except Exception as e:
                print(f"Error processing input: {e}")
    new_table = sorted(new_table, key=lambda x: x['position'])
    return new_table


def main():
    sys.stdout.write("Enter a decimal number: ")
    sys.stdout.flush()
    input_value = input()
    try:
        decimal_value = float(input_value)
    except ValueError:
        print("Invalid decimal number.")
        return

    # Display conversion details
    show_decimal_to_binary_steps(decimal_value)
    show_ieee754_visualization(decimal_value)
    show_multi_base_layout(decimal_value)

    transformer = UnifiedNumberTransformer()
    result = transformer.transform_computational_state(input_value)

    # Prepare lists to hold multiple truth tables and their corresponding data
    truth_tables = [result['truth_table']]
    kmap_representations = [result['kmap_representation']]
    gray_coded_states_list = [result['gray_coded_states']]
    adapted_states = [result['adapted_state']]

    # Interactive prompt to modify the default truth table or add new ones
    while True:
        print("Do you want to modify the truth tables?", flush=True)
        print("1: Add extra rows to the default truth table", flush=True)
        print("2: Add a completely new truth table", flush=True)
        print("3: Continue", flush=True)
        sys.stdout.write("Enter your choice (1/2/3): ")
        sys.stdout.flush()
        choice = input()
        if choice == '1':
            new_tt = add_extra_rows(truth_tables[-1])
        elif choice == '2':
            new_tt = create_new_truth_table()
        elif choice == '3':
            break

    # After exiting interactive prompt, display the final transformation result
    final_result = {
        'converted_state': result['converted_state'],
        'truth_tables': truth_tables,
        'kmap_representations': kmap_representations,
        'gray_coded_states_list': gray_coded_states_list,
        'adapted_states': adapted_states
    }
    display_transformation_result(final_result)


if __name__ == "__main__":
    main()