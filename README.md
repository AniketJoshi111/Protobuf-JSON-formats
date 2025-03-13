# Protobuf vs JSON Benchmark

This repo compares **Protocol Buffers (Protobuf) and JSON** in terms of **serialization and deserialization speed** as well as **data size efficiency**. Protobuf is used by linkedin in order to maintain low latency.
In total of 1 million objects are used for testing of above constrants.

## 📌 Features
- Serialize and deserialize data using **JSON** and **Protobuf**.
- Compare **size** and **processing time**.
- Menu-driven interface for easy testing.

## 🔧 Setup

### 1️⃣ Install Dependencies 
```sh
pip install protobuf
```

### 2️⃣ Compile the Protobuf Schema
``` sh
protoc --proto_path=. --python_out=. example.proto
```

### 3️⃣ Run the Program
``` sh
python main.py
```

### 📂 File Structure
``` bash
/PROTOBUF-BENCHMARK
│-- example.proto       # Protobuf schema
│-- example_pb2.py      # Generated Protobuf code (ignored in Git)
│-- main.py             # Main script
│-- .gitignore          # Ignore unnecessary files
│-- README.md           # Project documentation
```

![Results](https://res.cloudinary.com/drmf1p99g/image/upload/v1741877111/WhatsApp_Image_2025-03-13_at_20.02.39_cd6fa40f_xptydj.jpg)

### Conclusion
Protobuf is more efficient because it uses a binary format, making it faster and smaller than JSON.




