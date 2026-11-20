"""Производственное задание (вариант 13).

Консольная программа сравнивает плановый и фактический выпуск изделий
мастерской за несколько смен и выводит отчёт и таблицу нарастающим итогом.
Автор: Сайтгареева Елена.
"""

PLAN_PER_SHIFT = 100  # плановый выпуск за одну смену, изделий
WIDTH = 60            # ширина отчёта в символах
LABEL_W = 40          # ширина поля подписи
VALUE_W = 20          # ширина поля значения
COL_W = 20            # ширина одного столбца таблицы


def read_shifts():
    """Запрашивает количество смен, пока оно не окажется от 1 до 10.

    Не получает параметров, возвращает int: корректное число смен.
    """
    shifts = int(input("Количество смен (1-10): "))
    while not (1 <= shifts <= 10):
        print("Ошибка: число смен должно быть от 1 до 10.")
        shifts = int(input("Количество смен (1-10): "))
    return shifts


def read_output():
    """Запрашивает выработку за смену, пока она не станет неотрицательной.

    Не получает параметров, возвращает int: выработка за смену, изделий.
    """
    output = int(input("Выработка за смену, изделий: "))
    while output < 0:
        print("Ошибка: выработка не может быть отрицательной.")
        output = int(input("Выработка за смену, изделий: "))
    return output


def get_status(fact, plan):
    """Определяет статус выполнения плана.

    Получает фактический выпуск и план (int), возвращает строку-статус.
    """
    if fact < plan:
        return "Недовыполнение"
    elif fact == plan:
        return "План выполнен"
    else:
        return "Перевыполнение"


def get_percent(fact, plan):
    """Считает выполнение плана как долю (для формата .1%).

    Получает факт и план (int), возвращает float: fact / plan.
    """
    return fact / plan


def ask_repeat():
    """Спрашивает, нужен ли новый расчёт, пока не будет ответа да или нет.

    Не получает параметров, возвращает bool: True для «да», False для «нет».
    """
    question = "Выполнить новый расчет производства? (да/нет): "
    answer = input(question).strip().lower()
    while answer != "да" and answer != "нет":
        print("Введите «да» или «нет».")
        answer = input(question).strip().lower()
    return answer == "да"


def print_row(label, value):
    """Печатает строку отчёта: подпись слева, значение справа."""
    print(f"{label:<{LABEL_W}}{value:>{VALUE_W}}")


def print_report(workshop, shifts, total_plan, total_fact):
    """Печатает итоговый отчёт по мастерской (ничего не возвращает)."""
    deviation = total_fact - total_plan
    percent = get_percent(total_fact, total_plan)
    status = get_status(total_fact, total_plan)

    print()
    print(f"{'ПРОИЗВОДСТВЕННЫЙ ОТЧЕТ':^{WIDTH}}")
    print("-" * WIDTH)
    print_row("Мастерская:", workshop)
    print_row("Количество смен:", f"{shifts:02d}")
    print_row("Общий план, изделий:", total_plan)
    print_row("Общий факт, изделий:", total_fact)
    print_row("Отклонение, изделий:", deviation)
    print_row("Выполнение плана:", f"{percent:.1%}")
    print_row("Статус:", status)
    print("-" * WIDTH)


def print_table(shifts, output):
    """Печатает таблицу плана и факта нарастающим итогом по сменам."""
    print()
    print(f"{'Смена':>{COL_W}}{'План, шт':>{COL_W}}{'Факт, шт':>{COL_W}}")
    print("-" * WIDTH)
    plan_sum = 0
    fact_sum = 0
    for shift in range(1, shifts + 1):
        plan_sum += PLAN_PER_SHIFT
        fact_sum += output
        shift_text = f"{shift:02d}"
        print(f"{shift_text:>{COL_W}}{plan_sum:>{COL_W}}{fact_sum:>{COL_W}}")
    print("-" * WIDTH)
    print()


running = True
while running:
    workshop = input("Название мастерской: ").strip()
    shifts = read_shifts()
    output = read_output()

    total_plan = PLAN_PER_SHIFT * shifts
    total_fact = output * shifts

    print_report(workshop, shifts, total_plan, total_fact)
    print_table(shifts, output)

    running = ask_repeat()

print("Работа программы завершена")
