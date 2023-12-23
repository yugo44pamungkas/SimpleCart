import json

from .settings import DEFAULT_PRICE

def test_product_detail_api(client):
    id = 3
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get('id')
    assert DEFAULT_PRICE * id


def test_product_api(client):
    response = client.get("/api/products")
    assert response.status_code == 200
    
# post new cart
def test_post_cart(client):
    cart_data = {
        "coupon_code": "25AB",
        "shipping_fee": 0,
        "cart_items": [
            {
                "product_id": 1,
                "qty": 5
            }
        ]
    }
    response = client.post("/api/cart", data=json.dumps(cart_data), content_type="application/json")
    assert response.status_code == 200

def test_get_cart(client):
    # Test GET /api/cart
    response = client.get("/api/cart")
    assert response.status_code == 200

def test_get_cart_detail(client):
    cart_id = 1
    response = client.get(f"/api/cart/{cart_id}")
    assert response.status_code == 200

def test_put_cart(client):
    cart_id = 1
    data = {
        "coupon_code": "25AB",
        "cart_items": [
            {
                "product_id": 1,
                "qty": 3
            }
        ]
    }

    response = client.put(f"/api/cart/{cart_id}", json=data)
    assert response.status_code == 200

