import PersonClass as p


def main():
    name = "John"
    address = "123 James"
    phone_number = "123-456-7899"
    cust_number = 1234
    mailing_list = False

    john_person = p.Person(name, address, phone_number)

    john_customer = p.Customer(
        name, address, phone_number, cust_number, mailing_list)

    john_person.print_person()

    print()
    print()

    john_customer.print_person()


main()
