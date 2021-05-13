def reverse(DNA_sequence):
    DNA_sequence=DNA_sequence.upper()
    reverse_sequence=''
    for i in range(len(DNA_sequence)):
        if DNA_sequence[i] == 'A':
            reverse_sequence=reverse_sequence+'T'
        if DNA_sequence[i] == 'T':
            reverse_sequence = reverse_sequence + 'A'
        if DNA_sequence[i] == 'C':
            reverse_sequence = reverse_sequence + 'G'
        if DNA_sequence[i] == 'G':
            reverse_sequence = reverse_sequence + 'C'
    reverse_sequence=reverse_sequence[::-1]
    return reverse_sequence
#give an example
print(reverse('AtCg'))




