from aocd import get_data

my_list = get_data(day=7, year=2015).split("\n")
wire_operations_dict = {}
wire_values_dict = {}

for i in range(0, len(my_list)):
    instruction = my_list[i]
    wire = instruction.split("->")[1].strip(" ")
    operation = instruction.split("->")[0].strip(" ")
    wire_operations_dict[wire] = operation

    if(operation.isnumeric()):
        wire_values_dict[wire] = int(operation)

def get_signal(output_wire, wire_operations_dict, wire_values_dict):

    if(output_wire.isnumeric()):
        result = int(output_wire)
        wire_values_dict[output_wire] = result
        return result

    operation = wire_operations_dict[output_wire]

    if(str(operation).isnumeric() or output_wire in wire_values_dict.keys()):
        return wire_values_dict[output_wire]

    op_split = operation.split(" ")

    if(len(op_split) == 1):
        input_wire = op_split[0]
        result = get_signal(input_wire, wire_operations_dict, wire_values_dict)
        wire_values_dict[output_wire] = result
        return result

    elif(len(op_split) == 3 and "SHIFT" in op_split[1]):
        wire_to_shift = op_split[0]
        shift_amount = int(op_split[2])

        if(op_split[1] == "RSHIFT"):
            result = get_signal(wire_to_shift, wire_operations_dict, wire_values_dict) >> shift_amount
            wire_values_dict[output_wire] = result
            return result

        elif(op_split[1] == "LSHIFT"):
            result = get_signal(wire_to_shift, wire_operations_dict, wire_values_dict) << shift_amount
            wire_values_dict[output_wire] = result
            return result

    elif(len(op_split) == 3):
        input_wire1 = op_split[0]
        bitwise_op = op_split[1]
        input_wire2 = op_split[2]

        if(bitwise_op == "AND"):
            result = get_signal(input_wire1, wire_operations_dict, wire_values_dict) & get_signal(input_wire2, wire_operations_dict, wire_values_dict)
            wire_values_dict[output_wire] = result
            return result

        elif(bitwise_op == "OR"):
            result = get_signal(input_wire1, wire_operations_dict, wire_values_dict) | get_signal(input_wire2, wire_operations_dict, wire_values_dict)
            wire_values_dict[output_wire] = result
            return result

    elif(len(op_split) == 2):
        input_wire = op_split[1]
        result = ~ get_signal(input_wire, wire_operations_dict, wire_values_dict)
        wire_values_dict[output_wire] = result
        return result

print(get_signal("a", wire_operations_dict, wire_values_dict))
