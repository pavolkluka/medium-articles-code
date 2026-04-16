import re

def decryptor(fun_arg_1, fun_arg_2):
    len_fun_arg_2 = len(fun_arg_2)
    len_fun_arg_1 = len(fun_arg_1)

    var_2_value_len_fun_arg_1 = [0] * len_fun_arg_1
    var_3_value_len_fun_arg_1 = [0] * len_fun_arg_1

    var_unknown_1 = ""

    for var_index in range(1, len_fun_arg_1 + 1):
        for_var_1 = ((ord(fun_arg_2[(var_index - 1) % len_fun_arg_2]) * var_index) % len_fun_arg_1) + 1
        while var_2_value_len_fun_arg_1[for_var_1 - 1] != 0:
            for_var_1 = (for_var_1 % len_fun_arg_1) + 1
        var_2_value_len_fun_arg_1[for_var_1 - 1] = var_index

    for var_index in range(1, len_fun_arg_1 + 1):
        var_3_value_len_fun_arg_1[var_2_value_len_fun_arg_1[var_index - 1] - 1] = fun_arg_1[var_index - 1]

    for var_index in range(len(var_3_value_len_fun_arg_1)):
        var_unknown_1 += var_3_value_len_fun_arg_1[var_index]

    var_unknown_2 = ""

    for var_index in range(1, len(var_unknown_1) + 1):
        for_var_2 = ord(var_unknown_1[var_index - 1])
        for_var_3 = ord(fun_arg_2[(var_index - 1) % len_fun_arg_2])
        var_unknown_2 += chr((for_var_2 - 5) ^ for_var_3)

    return var_unknown_2

def dump_data(arg_data, arg_output):
    with open(arg_output, 'wb') as output_file:
        output_file.write(arg_data.encode('latin1'))

regular_ex = "(S30AV8ECM ?\( ?\"(.*?)\".*?\))"
regular_ex_compile = re.compile(regular_ex, re.IGNORECASE)
autoit_script = r'script.au3'

with open(autoit_script, 'rb') as script:
    data = script.read().decode('latin1')
    found_pattern = regular_ex_compile.findall(data)
    for match_pattern in found_pattern:
        #print(decryptor(match_pattern, '04'))
        decrypted_string = decryptor(match_pattern[1], '04')
        original_string = match_pattern[0]
        print(decrypted_string, '==', original_string)
        print("---")
        data = data.replace(original_string, '"' + decrypted_string + '"')
        dump_data(data, autoit_script + '.deob')
