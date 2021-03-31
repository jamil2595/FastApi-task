from sqlalchemy.orm import Session
from fastapi import  HTTPException

from . import models, schemas

#get_categories
def get_categories(db: Session,skip: int = 0, limit:int = 50):
    return  db.query(models.Category).all()
#get_categories

#create category
def create_category(db:Session, category:schemas.CategoriesCreate):
    if db.query(models.Category).filter(models.Category.name == category.name).first():
        raise HTTPException(status_code=409, detail="Category exists!")
    new_cat_obj = models.Category(name = category.name)
    db.add(new_cat_obj)
    db.commit()
    db.refresh(new_cat_obj)
    return new_cat_obj
#create category

#update category
def update_category(db:Session, category_id: int, category:schemas.CategoriesCreate):
    if category_id <=0:
        raise HTTPException(status_code=400, detail="Invalid argument!")
    if not db.query(models.Category).filter(models.Category.id == category_id).first():
        raise HTTPException(status_code=404, detail="Category does not exist!")
    new_cat_obj = db.query(models.Category).filter(models.Category.id == category_id).first()
    new_cat_obj.name  = category.name
    db.add(new_cat_obj)
    db.commit()
    return new_cat_obj
#update category

#delete category
def delete_category(db:Session, category_id: int):
    if category_id <=0:
        raise HTTPException(status_code=400, detail="Invalid argument!")
    if not db.query(models.Category).filter(models.Category.id == category_id).first():
        raise HTTPException(status_code=404, detail="Not found!")
    cat_obj_deleted = db.query(models.Category).filter(models.Category.id == category_id).first()
    db.delete(cat_obj_deleted)
    db.commit()
#delete category

#get list of products
def get_listOf_product(db:Session, category_id:int):
    if category_id <=0:
        raise HTTPException(status_code=400, detail="Invalid argument!")
    object_got = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not object_got:
        raise HTTPException(status_code=404, detail="Not found!")
    return object_got
#get list of products

#get products
def get_products(db: Session,skip: int = 0, limit:int = 50):
    return  db.query(models.Product).all()
#get products

#create product
def create_product(db:Session, product:schemas.ProductsCreate):
    if db.query(models.Product).filter(models.Product.name == product.name).first():
        raise HTTPException(status_code=409, detail="Product exists!")
    new_prod_obj = models.Product(name = product.name)

    db.add(new_prod_obj)
    db.commit()
    db.refresh(new_prod_obj)
    return new_prod_obj
#create product

#update product 
def update_product(db:Session, product_id: int, product:schemas.ProductsCreate):
    if product_id <=0:
        raise HTTPException(status_code=400, detail="Invalid argument!")
    if not db.query(models.Product).filter(models.Product.id == product_id).first():
        raise HTTPException(status_code=404, detail="Category does not exist!")
    new_prod_obj = db.query(models.Product).filter(models.Product.id == product_id).first()
    new_prod_obj.name = product.name
    db.add(new_prod_obj)
    db.commit()
    return new_prod_obj
#update product

#delete product
def delete_product(db:Session, product_id: int):
    if product_id <=0:
        raise HTTPException(status_code=400, detail="Invalid argument!")
    if not db.query(models.Product).filter(models.Product.id == product_id).first():
        raise HTTPException(status_code=404, detail="Not found!")
    pro_obj_deleted = db.query(models.Product).filter(models.Product.id == product_id).first()
    db.delete(pro_obj_deleted)
    db.commit()
#delete product

#add category to product relationship
def add_category_to_product(db:Session, product_id:int, category_id:int):
    if product_id <=0 or category_id<=0:
        raise HTTPException(status_code=400, detail="Invalid argument!")
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not exists!")
    category =  db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not exists!")
    category.products.append(product)
    db.add(category)
    db.commit()
#add category to product relationship

#delete category to product relationship
def delete_category_to_product(db:Session, product_id:int, category_id:int):
    if product_id <=0 or category_id<=0:
        raise HTTPException(status_code=400, detail="Invalid argument!")
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not exists!")
    category =  db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not exists!")
    category.products.remove(product)
    db.commit()
#delete category to product relationship