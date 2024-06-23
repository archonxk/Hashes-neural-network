import hashlib
import os
import json

cwd = os.getcwd()
hashes_store_file = os.path.join(cwd , "main.txt") 

main_storage_arr = []

total_count = 0
for i in range(0 , 16777216):
    string_of_bits = (bin(i)[2:].zfill(24))
    
    bit_array = []

    byte_size = 8
    number_of_bytes = len(string_of_bits)//8
    for j in range(1 , number_of_bytes+1):
        bit_array_sub = string_of_bits[((j-1)*8):(j*8)]
        bit_array.append(bit_array_sub)
    
    try:
        full_str = ""
        for byte in bit_array:
            utf_8 = chr(int(byte , 2))
            full_str = full_str + utf_8
    except:
        print(f"Error with {bit_array}")

    full_hash = hashlib.sha256(full_str.encode()).hexdigest()
    full_hash = "{0:08b}".format(int(full_hash, 16)) 

    hash_pair = {"hash":full_hash,
                "cleartext":full_str,
                "clearbits":string_of_bits}

    main_storage_arr.append(hash_pair)

    

    if len(main_storage_arr) == 20000:
        f = open(hashes_store_file , "a+")
        f.write(json.dumps(main_storage_arr))
        f.write("\n")
        f.close()
        main_storage_arr = []
        total_count = total_count + 20000
        print(f"Added 20000 hashes. Percentage --> {((total_count/16777216)*100)}")
        
else:
    f = open(hashes_store_file , "a+")
    f.write(json.dumps(main_storage_arr))
    f.write("\n")
    f.close()

    


