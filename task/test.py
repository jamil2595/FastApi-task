from fastapi.testclient import TestClient
from .main import app
client = TestClient(app)
import json
#test get category
def test_get_categories():
    response = client.get("/categories/")
    print(response.text)
    assert response.status_code == 200
#test get category

#test create category 
def test_create_category_wrong_request_body():
    response = client.post(
        "/categories/",
        json={
            "mame":"quarks"
        },
    )
    assert response.status_code == 422


def test_create_category():
    response = client.post(
        "/categories/",
        json={
            "name":"test category"
        }
    )
    assert response.status_code == 200
    j =  json.loads(response.text)
    assert j['name'] == "test category"

def test_create_category_existingcategory():
    response = client.post(
        "/categories/",
        json={
            "name":"test category"
        },
    )
    assert response.status_code == 409
    assert json.loads(response.text)["detail"] == "Category exists!"

#test create category

#test get category by id
def test_get_category_by_id_wrong_requests_integer():
    response = client.get("/categories/-1/")
    assert response.status_code == 400

def test_get_category_by_id_wrong_requests_float():
    response = client.get("/categories/2.9/")
    assert response.status_code == 422

def test_get_category_by_id_wrong_requests_string():
    response = client.get("/categories/a/")
    assert response.status_code == 422
#test get category by id

#test update category by id
def test_update_category_by_id_wrong_requests_integer():
    response = client.put("/categories/-1/")
    assert response.status_code == 422

def test_update_category_by_id_wrong_requests_float():
    response = client.put("/categories/2.9/")
    assert response.status_code == 422

def test_update_category_by_id_wrong_requests_string():
    response = client.put("/categories/a/")
    assert response.status_code == 422
#test update category by id

#test delete category by id
def test_delete_category_by_id_wrong_requests_integer():
    response = client.delete("/categories/-1/")
    assert response.status_code == 400

def test_delete_category_by_id_wrong_requests_float():
    response = client.delete("/categories/2.9/")
    assert response.status_code == 422

def test_delete_category_by_id_wrong_requests_string():
    response = client.delete("/categories/a/")
    assert response.status_code == 422
#test delete category by id

#test get products
def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
#test get products

#test create products
def test_create_products_wrong_body():
    response = client.post(
        "/products/",
        json={
            "mame":"quarks"
        },
    )
    assert response.status_code == 422

#test create products
def test_create_products():
    response = client.post(
        "/products/",
        json={
            "name":"test product"
        },
    )
    assert response.status_code == 200
    assert json.loads(response.text)["name"] == "test product"

#test update product by id
def test_update_product_by_id_wrong_requests_integer():
    response = client.put("/products/-1/")
    assert response.status_code == 422

def test_update_product_by_id_wrong_requests_float():
    response = client.put("/products/2.9/")
    assert response.status_code == 422

def test_update_product_by_id_wrong_requests_string():
    response = client.put("/products/a/")
    assert response.status_code == 422
#test update product by id

#test delete product by id
def test_delete_product_by_id_wrong_requests_integer():
    response = client.delete("/products/-1/")
    assert response.status_code == 400

def test_delete_product_by_id_wrong_requests_float():
    response = client.delete("/products/2.9/")
    assert response.status_code == 422

def test_delete_product_by_id_wrong_requests_string():
    response = client.delete("/products/a/")
    assert response.status_code == 422


#test add category to product by id
def test_add_category_to_product_by_id():
    response = client.post("/products/1/category/1/")
    assert response.status_code == 200

def test_add_category_to_product_by_id_wrong_integer():
    response = client.post("/products/-1/category/-1/")
    assert response.status_code == 400

def test_add_category_to_product_by_id_wrong_float():
    response = client.post("/products/2.9/category/-1/")
    assert response.status_code == 422

def test_add_category_to_product_by_id_wrong_string():
    response = client.post("/products/b/category/a/")
    assert response.status_code == 422
#test add category to product by id

#test delete category to product by id
def test_delete_category_to_product_by_id_wrong_integer():
    response = client.delete("/products/-1/category/-1/")
    assert response.status_code == 400

def test_delete_category_to_product_by_id_wrong_float():
    response = client.delete("/products/2.9/category/3.2/")
    assert response.status_code == 422

def test_delete_category_to_product_by_id_wrong_string():
    response = client.delete("/products/aa/category/bcd/")
    assert response.status_code == 422
#test delete category to product by id


#test delete category to product by id
def test_delete_category_to_product_by_id():
    response = client.delete("/products/1/category/1/")
    assert response.status_code == 200

#test delete product by id
def test_delete_product_by_id():
    response = client.delete("/products/1/")
    assert response.status_code == 200

#test delete category by id
def test_delete_category_by_id():
    response = client.delete("/categories/1/")
    assert response.status_code == 200
