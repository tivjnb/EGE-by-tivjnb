f = open('26.txt', 'r')

k, n = map(int, f.readline().split())
ls = []
for x in f:
    start_time, duration = map(int, x.split())
    ls.append([start_time, start_time+duration])
ls = sorted(ls)

was_started_at = 0
end_at = 0

count = 0
for start_time, end_time in ls:
    if end_time < end_at:
        end_at = end_time
    if start_time >= end_at:
        count += k
        end_at = end_time
        was_started_at = start_time
print(count, was_started_at)