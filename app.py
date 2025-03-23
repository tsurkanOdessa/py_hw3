from Connector import engine, Base, session
from Category import Category
from Product import Product

Base.metadata.create_all(engine)

parent_category = Category(name="Electronics", description="Devices and gadgets")
session.add(parent_category)
session.commit()

subcategory_s = Category(name="Smartphones", description="Mobile devices", parent_id=parent_category.id)
session.add(subcategory_s)
session.commit()

subcategory_l = Category(name="Laptops", description="Laptop devices", parent_id=parent_category.id)
session.add(subcategory_l)
session.commit()

new_product = Product(name="IPhon 16", price=999.99, in_stock=True, category_id=subcategory_s.id)
session.add(new_product)
session.commit()

new_product = Product(name="Lenovo B71", price=599.99, in_stock=True, category_id=subcategory_l.id)
session.add(new_product)
session.commit()

new_product = Product(name="ASUS N99", price=799.99, in_stock=True, category_id=subcategory_l.id)
session.add(new_product)
session.commit()

categories = session.query(Category).all()
products = session.query(Product).all()

for category in categories:
    print(f"Category: {category.name}, Parent: {category.parent_id}, Description: {category.description}")

for product in products:
    print(f"Product: {product.name}, Price: {product.price}, In Stock: {product.in_stock}, Category ID: {product.category_id}")
