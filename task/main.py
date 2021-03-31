from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#getcategories
@app.get("/categories/", response_model = List[schemas.CategoriesInline])
def get_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_category = crud.get_categories(db, skip, limit)
    return db_category
#getcategories


#createcategory
@app.post("/categories/",response_model = schemas.Categories)
def create_category(category:schemas.CategoriesCreate,db: Session = Depends(get_db)):
    return crud.create_category(db,category)
#createcategory

#updatecategory
@app.put("/categories/{category_id}/",response_model = schemas.Categories)
def update_category(category_id:int, category:schemas.CategoriesCreate, db: Session = Depends(get_db)):
    return crud.update_category(db,category_id, category)
#updatecategory


#deletecategory
@app.delete("/categories/{category_id}/",status_code = 200)
def delete_category(category_id:int,db: Session = Depends(get_db)):
    crud.delete_category(db,category_id)
#deletecategory


#getting the list of products of the concrete category
@app.get("/categories/{category_id}/",response_model = schemas.Categories)
def get_list_products(category_id:int, db: Session = Depends(get_db)):
   return crud.get_listOf_product(db,category_id)
#getting the list of products of the concrete category


#readcategory
@app.get("/products/", response_model = List[schemas.ProductsInline])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_product = crud.get_products(db, skip, limit)
    return db_product
#readcategory

#createproduct
@app.post("/products/",response_model = schemas.Products)
def create_product(product:schemas.ProductsCreate,db: Session = Depends(get_db)):
    return crud.create_product(db,product)
#createproduct

#updateproduct
@app.put("/products/{product_id}/",response_model = schemas.Products)
def update_product(product_id:int, product:schemas.ProductsCreate, db: Session = Depends(get_db)):
    return crud.update_product(db,product_id, product)
#updateproduct

#deleteproduct
@app.delete("/products/{product_id}/",status_code = 200)
def delete_product(product_id:int,db: Session = Depends(get_db)):
    crud.delete_product(db,product_id)
#deleteproduct

#addexistingproduct
@app.post("/products/{product_id}/category/{category_id}/")
def add_category_to_product(product_id:int, category_id:int,db: Session = Depends(get_db)):
    crud.add_category_to_product(db, product_id, category_id)
#addexistingproduct

#deleteexistingproduct
@app.delete("/products/{product_id}/category/{category_id}/")
def delete_category_to_product(product_id:int, category_id:int,db: Session = Depends(get_db)):
    crud.delete_category_to_product(db, product_id, category_id)
#deleteexistingproduct