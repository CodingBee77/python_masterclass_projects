import zlib, base64


def compress(input_file, output_file):
    """
    Compresses a file using zlib and base64 encoding.
    :param input_file:
    :param output_file:
    :return:
    """
    data = open(input_file, 'r').read()
    # Convert data into bytes in order to compress it with zlib library
    data_bytes = bytes(data, 'utf-8')
    # Encode compressed data
    compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))

    # We need to decode data to write it to the file
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(output_file, 'w')
    compressed_file.write(decoded_data)


def decompress(input_file, output_file):
    """
    Decompresses a file using zlib and base64 decoding.
    :param input_file:
    :param output_file:
    :return:
    """
    file_content = open(input_file, 'r').read()
    encoded_data = file_content.encode('utf-8')
    decoded_data = base64.b64decode(encoded_data)
    decompressed_data = zlib.decompress(decoded_data)
    decompressed_data_decoded = decompressed_data.decode('utf-8')
    with open(output_file, 'w') as output_file:
        output_file.write(decompressed_data_decoded)


# ----------------Example usage---------------------
# compress('demo.txt', 'compressed_final.txt')
decompress('compressed_final.txt', 'decompressed_final.txt')