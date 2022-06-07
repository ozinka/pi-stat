pi_st1 = ''
with open('pi_1m.txt') as f:
    pi_st1 = f.readline()

pi_st2 = ''
with open('pi_10m.txt') as f:
    pi_st2 = f.readline()

e_2m = ''
with open('e_2m.txt') as f:
    e_2m = f.readline()

def stat(pi_st):
    num = len(pi_st)
    for i in range(10):
        cnt = pi_st.count(str(i))
        print(f'{i}: {cnt} - {(cnt * 10000 // num) / 100} %')


# stat(pi_st1)

print(len(e_2m))
stat(e_2m)
print('-' * 20)
stat(pi_st2)

print('done')
