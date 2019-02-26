answers ={
    'Привет': 'Привет',
    'Что делаешь?': 'Программирую',
    'Как дела?': 'Отлично'
}


def get_answer(question, answers):
    return answers.get(question)

def ask_user(answers):
    while True:
        try:
            user_input = input('Пользователь:')
            answer = get_answer(user_input,answers)
            print(f'Программа: {answer}')
        except KeyboardInterrupt:
            print('\n Программа: Пока')
            break

if __name__ == '__main__':
    ask_user(answers)
