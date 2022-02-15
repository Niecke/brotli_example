import lorem
import brotli

print("Generating test data...")
test_string = lorem.get_sentence(50000)

print("Writing uncompressed test data to disk...")
with open("test_data", "w") as f:
    f.write(test_string)

print("Compressing test data...")
# string needs to be encoded to bytes
test_string_compressed = brotli.compress(test_string.encode())

print("Writing compressed test data to disk...")
# keep in mind we are writing binary data to a file -> "wb"
with open("test_data.compressed", "wb") as f:
    f.write(test_string_compressed)
