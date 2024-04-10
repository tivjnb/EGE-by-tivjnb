f = open('24.txt').read()

counter = dict()


for i in range(2, len(f)):
    if f[i-2] == f[i-1]:
        char = f[i]
        if char in counter.keys():
            counter[char] += 1
        else:
            counter[char] = 1
m_char, m_char_count = '', 0
for k, v in counter.items():
    if v > m_char_count:
        m_char = k
        m_char_count = v
print(m_char, m_char_count)
