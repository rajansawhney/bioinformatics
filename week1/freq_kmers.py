text = input('Enter text: ')
k = int(input('Enter k: '))

def generate_kmer_freq_map(text, k):
    n = len(text)
    pattern_to_freq = {}
    max_freq = 0
    for i in range(n - k+1):
        kmer = text[i:i+k]
        if kmer in pattern_to_freq:
            pattern_to_freq[kmer]+=1
        else:
            pattern_to_freq[kmer]=1
        if pattern_to_freq[kmer] > max_freq:
            max_freq = pattern_to_freq[kmer]
    return pattern_to_freq, max_freq

def get_max_freq_kmers(kmer_freq_map, max_freq):
    max_freq_kmers = []
    for kmer in kmer_freq_map:
        if kmer_freq_map[kmer] == max_freq:
            max_freq_kmers.append(kmer)
    return max_freq_kmers

kmer_freq_map, max_freq = generate_kmer_freq_map(text, k)
# print('\n**\nkmer_freq_map =\n', kmer_freq_map)
print('\n\n**\nmax_freq =\n', max_freq)

max_freq_kmers = get_max_freq_kmers(kmer_freq_map, max_freq)

print('\n\n**\nmax_freq_kmers =\n', max_freq_kmers)
