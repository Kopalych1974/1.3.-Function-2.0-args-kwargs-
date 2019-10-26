'''
Домашнее задание к лекции 1.3. «Function 2.0 *args, **kwargs»
Создать приложение "Телефонная книга". класс Contact имеет следующие поля:
Имя, фамилия, телефонный номер - обязательные поля;
Избранный контакт - необязательное поле. По умолчанию False;
Дополнительная информация(email, список дополнительных номеров, ссылки на соцсети) - необходимо использовать *args, **kwargs.
Переопределить "магический" метод str для красивого вывода контакта. Вывод контакта должен быть следующим

    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print(jhon)
Вывод

Имя: Jhon
Фамилия: Smith
Телефон: +71234567809
В избранных: нет
Дополнительная информация:
	 telegram : @jhony
	 email : jhony@smith.com
класс PhoneBook:
Название телефонной книги - обязательное поле;
Телефонная книга должна работать с классами Contact.
Методы:

Вывод контактов из телефонной книги;
Добавление нового контакта;
Удаление контакта по номеру телефона;
Поиск всех избранных номеров;
Поиск контакта по имени и фамилии.
'''
class Contact(object):

    def __init__(self, first_name, last_name, phone_number, favorite_contact=False, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favorite_contact = favorite_contact

        self.additional_info_args_list = []
        for a in args:
            self.additional_info_args_list.append(a)

        self.additional_info_kwargs_dict = {}
        for item_name, item_value in kwargs.items():
            self.additional_info_kwargs_dict[item_name] = item_value

    def __str__(self):
        if self.favorite_contact:
            favorite_contact_ru = 'yes'
        else:
            favorite_contact_ru = 'no'

        return str(
            "Name: " + self.first_name + "\n" +
            "Last name: " + self.last_name + "\n" +
            "Cell number: " + self.phone_number + "\n" +
            "In favorites: " + favorite_contact_ru + "\n" +
            "Additional information: " + "\n" +
            "\t" + '\n\t'.join(self.additional_info_args_list) + "\n" +
            "\t" + "\n\t".join('{}: {}'.format(item_name, item_value) for item_name, item_value
                               in sorted(self.additional_info_kwargs_dict.items()))
            )


class PhoneBook:

    def __init__(self, phonebook_name):
        self.phonebook_name = phonebook_name

# Вывод контактов из телефонной книги
    def get_contacts(phonebook):
        contacts = []
        for contact in phonebook:
            contacts.append(contact)
        return contacts

# Добавление нового контакта
    def create_contact(contact, phonebook):
        phonebook = phonebook.append(contact)
        return phonebook

# Удаление контакта по номеру телефона
    def delete_contact_by_number(phone_number, phonebook):
        if contact.__dict__['phone_number'] == phone_number:
            phonebook.remove(contact)
        return phonebook

# Поиск всех избранных номеров
    def get_favorite_contacts(phonebook):
        favorite_contacts = []
        for contact in phonebook:
            if contact.__dict__['favorite_contact']:
                favorite_contacts.append(contact)
        return favorite_contacts

# Поиск контакта по имени и фамилии
    def get_contact_by_name(phonebook, first_name, last_name):
        found_contacts = []
        for contact in phonebook:
            if contact.__dict__['first_name'] == first_name and (contact.__dict__)['last_name'] == last_name:
                found_contacts.append(contact)
        return found_contacts


contact1 = Contact('Homer', 'Simpson', '+5551110000', True, ' Springfield, 742 Evergreen Terrace', '+79000000000', 'engineer', telegram='@Homer', email='Homer@simpson.com')

contact2 = Contact('Marge', 'Simpson', '+5551112222', False, 'Springfield, 742 Evergreen Terrace', '+79555555555', 'doctor', telegram='@Marge', email='Marge@simpson.com')

contact3 = Contact('Bart', 'Simpson', '+5551114444', False, 'Springfield, 742 Evergreen Terrace', '+77777777777', 'schoolboy', telegram='@Bart', email='Bart@simpson.com')

contact4 = Contact('Lisa ', 'Simpson', '+5551113333', True, 'Springfield, 742 Evergreen Terrace', '+79000000000', 'schoolgirl', telegram='@Lisa', email='Lisa@simpson.com')

contact5 = Contact('Maggie', 'Simpson', '+5551112222', False, 'Springfield, 742 Evergreen Terrace', '+79555555555', 'baby', telegram='@Marge', email='Marge@simpson.com')

contact6 = Contact('Abe', 'Simpson', '+5551111111', False, 'Springfield, 742 Evergreen Terrace', '+77777777777', 'Grandpa', telegram='@Abe', email='Abe@simpson.com')


work_phonebook = []
PhoneBook.create_contact(contact1, work_phonebook)
PhoneBook.create_contact(contact2, work_phonebook)
PhoneBook.create_contact(contact3, work_phonebook)
PhoneBook.create_contact(contact4, work_phonebook)
PhoneBook.create_contact(contact5, work_phonebook)
PhoneBook.create_contact(contact6, work_phonebook)

print('=' * 50)
print('Список всех контактов:\n')

contacts = PhoneBook.get_contacts(work_phonebook)
for contact in contacts:
    print(contact)

print('=' * 50)
print('Список контактов после удаления по номеру телефона:\n')

for contact in contacts:
    PhoneBook.delete_contact_by_number('+5551112222', work_phonebook)

contacts = PhoneBook.get_contacts(work_phonebook)
for contact in contacts:
    print(contact)

print('=' * 50)
print('Избранные контакты:\n')

favorite_contacts = PhoneBook.get_favorite_contacts(work_phonebook)
for contact in favorite_contacts:
    print(contact)

print('=' * 50)
print('Найденный по имени и фамилии контакт:\n')

found_contacts = PhoneBook.get_contact_by_name(work_phonebook, 'Maggie', 'Simpson')
for contact in found_contacts:
    print(contact)



