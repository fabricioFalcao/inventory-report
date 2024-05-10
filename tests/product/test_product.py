from inventory_report.product import Product


def test_create_product() -> None:

    id = '220462'
    product_name = 'Pitty'
    company_name = 'Falcon Enterprises'
    manufacturing_date = '2005-14-11'
    expiration_date = '2022-22-03'
    serial_number = '1234567890'
    storage_instructions = 'She likes to lay down in the center of the bed'

    
    product = Product(id, product_name, company_name, manufacturing_date, expiration_date, serial_number, storage_instructions)

    assert product.id == id
    assert product.product_name == product_name
    assert product.company_name == company_name
    assert product.manufacturing_date == manufacturing_date
    assert product.expiration_date == expiration_date
    assert product.serial_number == serial_number
    assert product.storage_instructions == storage_instructions