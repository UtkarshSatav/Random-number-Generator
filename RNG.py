state = (1 << 127) | 1

while range(10):
    print(state & 1, end=' ')
    newbit =(state ^ (state >> 1) ^ (state >> 2) ^ (state >> 7))
    state = (state >> 1) | (newbit << 127)
    