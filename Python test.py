import art
print(art.logo)


def caesar(message, key, mode):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    message = message.upper()
    key = key % 26
    mode = mode.strip().lower()

    if mode.startswith("e"):
        shift = key
    elif mode.startswith("d"):
        shift = -key
    else:
        return "Mode must be 'encrypt' or 'decrypt'"

    for ch in message:
        if ch not in letters:         
            result += ch
            continue

        idx = letters.index(ch)
        idx = (idx + shift) % 26      
        result += letters[idx]

    return result


while True:
    msg = input("Enter your message: ")
    key = int(input("Enter the key: "))
    mode = input("Encrypt or Decrypt? ")

    print(caesar(msg, key, mode))