import json

with open (r"C:\Users\iolan\PycharmProjects\PythonProjects\lendoarquivojson\itens.txt", "r") as file:
        array = []
        key = "elb.amazonaws.com"
        for line in file:
            if key in line:
                array.append(line.strip())

print(array)

with open(r"C:\Users\iolan\PycharmProjects\PythonProjects\lendoarquivojson\resultado.txt", 'w') as resultado:
    for x, item in enumerate(array):

        resultado.write(f"{x}.")
        resultado.write(item + '\n')