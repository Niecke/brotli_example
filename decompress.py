import brotli

test_string = None
test_string_compressed = None

print("Read uncompressed test data from disk...")
with open("test_data", "r") as f:
    test_string = f.read()

print("Read compressed test data from disk...")
# keep in mind we are reading binary data from disk -> "rb"
with open("test_data.compressed", "rb") as f:
    test_string_compressed = f.read()

print("Decompress test data...")
# string needs to be decoded from bytes to string
test_string_decompressed = brotli.decompress(test_string_compressed).decode()

print(
    f"test_data and test_data.compressed have the same content: {test_string_decompressed == test_string}")
