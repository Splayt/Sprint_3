import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

#напиши геттеры

    @property
    def name_items(self):
        return self.__name_items

    @property  
    def number_items(self):
        return self.__number_items
    
#добавь товар в чек
   
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

#удали товар из чека

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

#посчитай общую стоимость товара

    def check_amount(self):
        total = 0
        for item in self.__name_items:
            total += self.__item_price[item]
        if self.__number_items > 10:
            total *= 0.9
            return total
        else:
            return total    

#вычисли НДС для товаров со ставкой 20%

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = 0
        for item in self.__name_items:
            if self.__tax_rate.get(item) == 20:
                total += self.__item_price[item] * 0.2
        if self.__number_items > 10:
            total *= 0.9       
        return total

#вычисли НДС для товаров со ставкой 10%

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = 0
        for item in self.__name_items:
            if self.__tax_rate.get(item) == 10:
                total += self.__item_price[item] * 0.1
        if self.__number_items > 10:
            total *= 0.9       
        return total

#посчитай общую сумму налогов
    def total_tax(self):
        total_tax_amount = 0
        for item in self.__name_items:     
            price = self.__item_price[item]
            tax_rate = self.__tax_rate[item]
            if tax_rate == 20:
                total_tax_amount += price * 0.2
            elif tax_rate == 10:
                total_tax_amount += price * 0.1
        if self.__number_items > 10:
            total_tax_amount *= 0.9

        return total_tax_amount

#верни номер телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number): 

        try:
            phone = int(telephone_number)
        except ValueError:
            print('Необходимо ввести цифры')
        
        if len(telephone_number) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        
        return f'+7{phone}'
    
#доп задание
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]

        for time in date:
            interval = time[0]
            func = time[1]
            date_and_time.append(f'{interval}: {func(now)}')

        return date_and_time