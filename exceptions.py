def get_summ(num_one, num_two):
    try: 
        result_sum = int(num_one) + int(num_two)
        print(result_sum)
    except ValueError:
        print('Приведение типов не сработало')

get_summ('wdew','3')

get_summ('3.8','3')

get_summ('4','3')

