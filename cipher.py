def caesar_cipher(text, shift):
    shift = shift % 26
    result = []
    for char in text:
        if ord('a') <= ord(char) <= ord('z'):
            normalized_char = (ord(char) - ord('a') + shift) % 26
            new_char = chr(normalized_char + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)

tests = [
    ("hello world", 0, "hello world"),
    ("abc", 1, "bcd"),
    ("xyz", 3, "abc"),
    ("Caesar Cipher", 2, "Ecguct Ekrjgt"),
    ("Python", -2, "Nwrfml"),
    ("", 5, ""),
    ("Hello, World!", 5, "Mjqqt, Btwqi!"),
    ("Shift 123!", 4, "Wlmjx 123!"),
    ("Zebra", 25, "Ydaqz"),
]

for test in tests:
    text, shift, result = test
    actual_result = caesar_cipher(text, shift)
    test_res = actual_result == result and "PASSED ✅" or f"FAILED ❌ got ({actual_result})"
    print(f"Caesar cipher with params ({text, shift}), {test_res}")

'A' - z = 65 to 91
'a' = 97 to 123

'x' mod 26

# ord("z") == 122
# ord('a') == 97
#
caesar_cipher('z', 1) == 'a'




32


for i in :
