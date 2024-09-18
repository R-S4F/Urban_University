text = 'abcdef'
_len = len(text) + 1
for i in range(1, _len):
    for k in range(0, _len - i):
        print(text[k:k+i])
