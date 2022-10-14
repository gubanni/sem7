import view, model
import logger as log
def start():
    value_a = view.get_value("Первое число = ")
    value_b = view.get_value("Второе число = ")
    value_operation = view.get_operation()
    result = model.calc(value_a, value_b, value_operation)
    log.calc_logger(f'{value_a} {value_operation} {value_b} = {result}')
    view.view_data(result, "Результат = ")
