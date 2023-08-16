import time
nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt']
many_people = ['nemo' for i in range(100000)]
def find_nemo(arr):
    t0 = time.perf_counter()
    for item in arr:
        if item == 'nemo':
            print('Found Nemo!')
    t1 = time.perf_counter()
    print(f'Time taken: {round(t1, 2) - round(t0, 2)}ms')
find_nemo(nemo)
find_nemo(everyone)
find_nemo(many_people)