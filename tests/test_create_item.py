import json
import os
from utils.api_client import APIClient

client = APIClient()

# Path to JSON
data_path = os.path.join(os.path.dirname(__file__), "..", "data", "test_data.json")

# Load data from JSON
with open(data_path) as f:
    test_data = json.load(f)

def test_full_item_lifecycle():
    # POST - create item
    post_payload = test_data["post_item"]
    post_response = client.post("/objects", json=post_payload)
    assert post_response.status_code == 200

    post_response_json = post_response.json()
    assert "id" in post_response_json
    item_id = post_response_json.get("id")

    assert post_response_json["name"] == post_payload["name"]
    assert post_response_json["data"] == post_payload["data"]
    #print(item_id)

    # GET — get item by ID
    get_response = client.get(f"/objects/{item_id}")
    assert get_response.status_code == 200
    get_response_json = get_response.json()
    assert get_response_json["name"] == post_payload["name"]
    assert get_response_json["data"] == post_payload["data"]

    # PUT - update item
    put_payload = test_data["put_item"]
    put_response = client.put(f"/objects/{item_id}", json=put_payload)
    assert put_response.status_code == 200
    put_response_json = put_response.json()
    assert put_response_json["name"] == put_payload["name"]
    assert put_response_json["data"] == put_payload["data"]

    # DELETE — delete item
    delete_response = client.delete(f"/objects/{item_id}")
    assert delete_response.status_code == 200

    # GET — check item does not exist
    get_after_delete = client.get(f"/objects/{item_id}")
    assert get_after_delete.status_code == 404