from collections import Counter

string = 'asdfasdfasdjfaklsjlkfajsdfaurowureionmxnvmnskfhjsakhfd'

freq = Counter(string)

print(freq)

print(freq.most_common(1))