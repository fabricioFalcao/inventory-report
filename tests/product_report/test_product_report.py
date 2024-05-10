from inventory_report.product import Product


def test_product_report() -> None:
    id = '220462'
    product_name = 'Pitty'
    company_name = 'Falcon Enterprises'
    manufacturing_date = '2005-14-11'
    expiration_date = '2022-22-03'
    serial_number = '1234567890'
    storage_instructions = 'She likes to lay down in the center of the bed'

    
    product = Product(id, product_name, company_name, manufacturing_date, expiration_date, serial_number, storage_instructions)

    assert product.__str__() == (
            f"The product {id} - {product_name} "
            f"with serial number {serial_number} "
            f"manufactured on {manufacturing_date} "
            f"by the company {company_name} "
            f"valid until {expiration_date} "
            "must be stored according to the following instructions: "
            f"{storage_instructions}."
        )
