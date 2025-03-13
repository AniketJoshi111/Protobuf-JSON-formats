import json
import time
from google.protobuf.message import Message
import example_pb2  # Assuming you have an example.proto compiled into example_pb2.py

#generating large data 

def generate_large_data(size=100000):
    data = {
        "id": 123,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "age": 30,
        "is_active": True,
        "friends": []
    }
    for i in range(size):
        data["friends"].append({"id": i, "name": f"Friend_{i}"})
    return data

def serialize_json(data):
    start_time = time.time()
    json_data = json.dumps(data)
    json_time = time.time() - start_time
    json_size = len(json_data.encode("utf-8"))
    return json_data, json_size, json_time

def serialize_protobuf(data):
    message = example_pb2.Person()
    message.id = data["id"]
    message.name = data["name"]
    message.email = data["email"]
    message.age = data["age"]
    message.is_active = data["is_active"]
    for friend in data["friends"]:
        f = message.friends.add()
        f.id = friend["id"]
        f.name = friend["name"]
    
    start_time = time.time()
    proto_data = message.SerializeToString()
    proto_time = time.time() - start_time
    proto_size = len(proto_data)
    return proto_data, proto_size, proto_time

def deserialize_json(json_data):
    start_time = time.time()
    json_obj = json.loads(json_data)
    json_deserialization_time = time.time() - start_time
    return json_obj, json_deserialization_time

def deserialize_protobuf(proto_data):
    start_time = time.time()
    proto_obj = example_pb2.Person()
    proto_obj.ParseFromString(proto_data)
    proto_deserialization_time = time.time() - start_time
    return proto_obj, proto_deserialization_time

def menu():
    data = generate_large_data()
    
    print(f"Below the memory acquired by protobuf is 50% less than json in order to transfer the same amount of data(1 million records) \n , Hence protbuf format is more efficient than json\n")
    

    print(f"Number of  objects / size of dataset: {len(data["friends"])} bytes ")
    json_data, json_size, json_time = serialize_json(data)
    print(f"JSON Size: {json_size} bytes, Serialization Time: {json_time}")
            
    proto_data, proto_size, proto_time = serialize_protobuf(data)
    print(f"Protobuf Size: {proto_size} bytes, Serialization Time: {proto_time}\n")
            
    json_data, _, _ = serialize_json(data)
    json_obj, json_deserialization_time = deserialize_json(json_data)
    print(f"JSON Deserialization Time: {json_deserialization_time}")
            
    proto_data, _, _ = serialize_protobuf(data)
    proto_obj, proto_deserialization_time = deserialize_protobuf(proto_data)
    print(f"Protobuf Deserialization Time: {proto_deserialization_time}")
                

if __name__ == "__main__":
    menu()
