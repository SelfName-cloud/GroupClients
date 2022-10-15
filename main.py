import numpy as np
from collections import Counter


class CountGroupClients:

    def count_client_group(self, n_customers: int):
        """Принимает на вход количество клиентов или id клиентов от 0 до n"""

        """Проверка на корректность входных данных """
        if type(n_customers) == str:
            try:
                n_customers = int(n_customers)
            except Exception:
                message_error = "TypeError: input correct argument, please"
                return message_error

        client_id = np.arange(n_customers + 1)
        group_client = [i for i in map(self.__make_groups, client_id)]
        count_client_in_groups = Counter(group_client)

        """Возвращаем лист кортежей, где в каждом из кортежей два значения, 
        1. Номер группы
        2. Количество клиентов в ней """

        return count_client_in_groups.most_common()

    def count_client_groups_first_id(self, first_id: int, n_customers: int):
        """Принимает на вход id первого клиента и количество клиентов """

        """Проверка на корректность входных данных """
        if type(n_customers) == str or type(first_id) == str:
            try:
                n_customers = int(n_customers)
                first_id = int(first_id)
            except Exception:
                message_error = "TypeError: input correct argument, please"
                return message_error
        if n_customers < first_id:
            message_error = 'Id first client more than count all clients'
            return message_error

        client_id = np.arange(first_id, n_customers + 1)
        group_client = [i for i in map(self.__make_groups, client_id)]
        count_client_in_groups = Counter(group_client)

        """Возвращаем лист кортежей, где в каждом из кортежей два значения, 
            1. Номер группы
            2. Количество клиентов в ней """

        return count_client_in_groups.most_common()

    def __make_groups(self, num):
        number = 0
        for i in str(int(num)):
            number += int(i)
        return number


if __name__ == "__main__":
    count_group_clients = CountGroupClients()
    first_id = input('Введите Id первого клиента: ')
    n_customers = input('Введите общее число клиентов: ')
    print('(Номер группы, Количество клиентов)')
    if first_id:
        print(count_group_clients.count_client_groups_first_id(first_id=first_id, n_customers=n_customers))
    else:
        print(count_group_clients.count_client_group(n_customers=n_customers))





