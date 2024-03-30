class Stack():
    def __init__(self, stack):
        self.stack = stack

    # проверка стека на пустоту. Метод возвращает True или False
    def is_empty(self):
        if len(self.stack) == 0:
            return False
        else:
            return True

    # Добавляет новый элемент на вершину стека. Метод ничего не возвращает
    def push(self, item):
        self.stack.append(item)

    # Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    # Возвращает верхний элемент стека, но не удаляет его. Стек не меняется
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]

    # Возвращает количество элементов в стеке
    def size(self):
        lenght = len(self.stack)
        return lenght


    def is_balanced_brackets(self):
        opening_brackets = ['(', '{', '[']
        closing_brackets = [')', '}', ']']
        bracket_stack = []
        for bracket in self.stack:
            if bracket in opening_brackets:
                bracket_stack.append(bracket)
            elif bracket in closing_brackets:
                if len(bracket_stack) == 0:
                    return f'{self.stack} - несбалансированная последовательность'
                popped_bracket = bracket_stack.pop()
                if popped_bracket == '(' and bracket == ')':
                    return f'{self.stack} - сбалансированная последовательность'
                if popped_bracket == '{' and bracket == '}':
                    return f'{self.stack} - сбалансированная последовательность'
                if popped_bracket == '[' and bracket == ']':
                    return f'{self.stack} - сбалансированная последовательность'
                return f'{self.stack} - несбалансированная последовательность'
        if len(bracket_stack) != 0:
            return f'{self.stack} - несбалансированная последовательность'
        return f'{self.stack} - сбалансированная последовательность'




if __name__ == '__main__':
    check_balance = Stack("(((([{}]))))")
    print(check_balance.is_balanced_brackets())
    check_balance_2 = Stack("}{}")
    print(check_balance_2.is_balanced_brackets())


