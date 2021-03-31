from typing import List, Optional

from pydantic import BaseModel

#pydantic schema
class ProductsBase(BaseModel):
    name: str

class CategoriesBase(BaseModel):
    name: str

class CategoriesInline(CategoriesBase):
    id: int
    class Config:
        orm_mode = True

class ProductsInline(ProductsBase):
    id: int
    class Config:
        orm_mode = True

class CategoriesCreate(CategoriesBase):
    pass

class ProductsCreate(ProductsBase):
    pass

class Products(ProductsBase):
    id: int
    categories: List[CategoriesInline] = []

    class Config:
        orm_mode = True


class Categories(CategoriesBase):
    id: int
    products: List[ProductsInline] = []

    class Config:
        orm_mode = True