# Given data
alphanumerical = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(){}_?'
key = '5up3r_s3cr3t_k3yyyy' # Same key used in encryption
encrypted = 'i$UYc8H{#p?)eo^cPCv'

# Step 1: Recreate the matrix
matrix = []
for i in alphanumerical:
    matrix.append([i])

idx = 0
for i in alphanumerical:
    matrix[idx][0] = (alphanumerical[idx:len(alphanumerical)] + alphanumerical[0:idx])
    idx += 1

# Step 2: Recompute key indices (key_arr)
key_arr = []
for y in key:
    for i in range(len(alphanumerical)):
        if matrix[i][0][0] == y:
            key_arr.append(i)

# Step 3: Map encrypted characters to original flag
decrypted = []
for i in range(len(encrypted)):
    enc_char = encrypted[i]
    key_idx = key_arr[i]
    # Find the original character in the matrix row `key_idx`
    for row in matrix:
        if row[0][key_idx] == enc_char:
            decrypted.append(row[0][0])
            break

# Join the decrypted characters to form the original flag
original_flag = ''.join(decrypted)
print("Decrypted message:", original_flag)
