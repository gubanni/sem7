

def view_data(data, title):
    print(f'{title} = {data}')

def get_value(text):
    return int(input(f'{text}'))

def get_operation():
    operation = str(input(f"Введите операцию(варианты:+,-,/,*,mod,pow,div): "))
    return operation