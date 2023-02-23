# reverse complement
complement_dict = {
    'A': 'T',
    'G': 'C',
    'T': 'A',
    'C': 'G'
}

text = 'CGTCGATTCGCACCCATTCTCGGTACGAGTGAGGCCGCTTTACAACGGAAAATTTCTCACTGGGACGACAGGTGTTTTTATTGGAATAGTCGTGTCGCATCGAGTTCTGAGTTGGTCGAGAGTGTACGTGGGGAATTGGCAGACAGTTGTCAAACGTGAATGTCACAAACCCATGTGATCTGCGATAAAAAACCATGCTGCTATTACCACGAGCCTGACGTTTACAAAAGGTGGAAAGGTCCCGAATTAGAAAGCTAAAGAAAGTGAGTCAGACTTACGTTTGCTGTATCACACGCGTACGCACTAACACGTTCGCGGAATCTGGTGAGCATAATCCCATTTTCTGCCAATGATGTGTTCTGCCCTCGAAAATGCAGTGTCACGTTGGCCACCGCGGCCCACAGCCGACCGGCGCTGGGAGAGGTTTGCGGGACCAGGCTTCTGCGTGGAAGCATGCTAGTCCGCCGGTGTAGTGTTATTCGTCAATCGCCTATCCAACTTTTTAGGGAAGGGTATGTACGCTGGAGTGGAGTTCCCAGGCCACAGCGTGTTGGAGGTCTCTAGCGATCGAGGTACAATATTCTGTAGTTGGGTTCTCTGACCTCTGGAAACCCAGAGTATTTACAAGATTTCTTTACAGATAGCCTAAAATTGTGGCTAGTAGTTGGTTTAAAAAATTGGGCTATATGAACTATAAAATTCCCGTTATAAATAGCTCCTATACGTCTTTCACAGCATCTCAGAAGACGAACTGACATACACACGTAATTTCGCGGTCATCGGGATAAATCAGACAGGCAACGGTTTCCTCACTATGTGTGGGCACTCCTAGCAGCAATAAGGTACCTGGCTAAACGTTCATGAGGGGCCGCGAGGAAGGAGTAGAACTTCTACCAAATTGGATTCCGTGTAGAAGGGTGTATCAGTTGGTGCGCACTCATTCTGAAGAACCTTGTCACGTCCCGAGTCGAGGGGTGAAGGACGCCGAAACCAACCGACTTATTCGGGCCATTATCGCACATTCAGATAGATATTCTGTTTTTGCAGTGATGTCTCTGCACGCACGCCATCTACTGGCGTTTGCGTTTGAGAGGATATACCGCCGTGTGTGCGCTCTCAGCGCTGATTCCCTCCGTCTCCCGCATAAAAAATCCGACAGTGATGCCGTTCTGGTATACGCCTTGTTAAATCGCGACAACGCTAGAGTACGTACGTACAGTCCCTGTTACACCTGTCACATCGTTCTCCGTTAAGGAGAATCTTAAATCTCCACGCGATGTTCGAGCAATGCTACGCTGATGTGTGGTTTACGGTATATATGCGACACCGTTCCAGCCAGTAATACATAGCTGCGGATAGCGGCTTATAATACTGCCAATATCAGTAAGCACTTCACCCGCGTACATACGACGAGAACACTTGGAATTTAGACAGACGGGCTTTAGTTTTAGTGGAGCGCCGCCTAAGAACCATATATTCCACTGGGCACGGTCACCAGAATTAGGACATCCTTCTATATCGATAGCTCACGAGCGTCAGGGCGGCGTGGAAAATTCACCACTCCGGCCTCCCCCATGTTATTTGGTGATAAAGAGGATCCACACACTGCTCTACCGGTGGACTGTATGGCATATGATTCGCCCCAGACCAAAACACGTGTTCATTCTAGTCTGTGAGGATACGTGGGTATGATTCTCCTGAGGTGTACGCCGTGATAGCCTACCGGTGCAACTCTATATCGGTGCGAGGAGGTCATGGTTTGTCCCACTTCACTACGAATGCGTCGTTCAAATCTAAACCCATCCATCCTTCGGGTTAGGGCACTGGAAGCGCGGAGTACGCGGCCTAGTGAAAGCGCATTCGAGATGTAGAGTCCGCGAGCATGTCTTATGTGACCGCCTAATGCGAAAAGAAACGAAAATTAGTTTACTGTAGCTCCGGGCGAAGAGCATGGGCTTTATTATCATTCGATCTGTTAACATTACCGGTTGCCTAGCGTGCAGATTGGCTGACGACGCGCGAGTGGTTCGCTTAAGGGCAACTCCAGACATACAATCCAAGCCCCATCTTTGACAACCCGTATACCATGAGAAGAATGATCACGGGGGCCTGGTATAGTCAACCTTCTGAGGCCTAAGTTTTGTTTCGCTGGGACAAGGTCCCCGACCTAGAAGGCTCCCACCCCTCGTAGTGGTGGTTCTTGGGGCAAACATAATCTGACCGGCAAGGCTCACTGTGACGCGCACAAGTTACTTTACGGATGGGACCCACAGTATCGATACTCGAACGCTAACCCAGATAATCTAAGGAGAAAGAAAAGGTTCGGGATACTAGAATGTCTATGACGCCGTACCAATCTGGCGAATAATATGTTTTGAGCACGTTAAACGCTACTATCGACCCCCATACAACTGAACTGGGCTGACGGTGCCGTATACGAATTGTAGAACGCCCCGCGTCTATAGTAGCAGGGCAGTAAGAGTCCCACTCTACAACTTCGGAGGGGTACTGCAGGAGCTTTAGCCGTATAGCGGGCACTGTTACCTGACGGGGGGTTAACAATTAAAAAATCTTACGCACATGACTACTCGGTATAAGCACGGCGCTAATCGAGCTTTCGTACAATAGGAAGAGCACTCGCTCACACGTACACCGTCACCAGAACATATAATCGTGTCACCTTGCACAACGGAAGCCAGCATCCGGCCGTTTCAAGCTCGAATGCAGCGGCGTTGATTAGTCCCTGCCGCGCTCCAGTATTGCATGTCTACCCGGACCGCAGCGTCACACCGACGACATACCCTTTTCTAGGCAAACATTACTTGACATCTACCGACGTACTTACCCAAATTCTCCTGATATTTCCCACGGAATGTGATCTCTGGCGTGCAACTCAAACGGTGTATTCACTGGTTAGGTTGACTCGAAGCCCTCTTGATGCACAAGGAAACCAGTGGCGAAAGCCAATTTGGATCTGGTCGGGGTCGTCGAATACTCCACGCCTGGACGGCCGGCTCGCGACACATTCGGACTAAGCGGAATCTGCCAGCTATCGCACCAGCGCTCATAGGTTAATAGGTTAATCCAATTGCAAAGTCGTTGAATCGCGATGCTCGTTGGGTGATGGGCGATCTGTCCTTCCCTATTGCGTAAGCGTAGTTCGCGTGCCACATGCGATTCTACAATGCCGCGGTGTCAGACCACCAAGCTACGGACTGCGATGATACAAGCCCTAAGCAGGTTCTTCAGCCGGCCTCCCTGTCCCTTTGAGCTGCCGCGGCAAGATGTCAGATAGAATTGCTTGAGTTGGCAAGAGTAGAGGTTTTGGTGTAGGGCATCGGTGTAATGAAGTATTAGCACATGGACGTTGAACCCCAGTGTAACGGGCACGCTGGATGGGCTGATTCAATTGGGGCTTATAAAGGTAGGAAGGCATTTTTGATTCTCGCTCCTGATGTCGCTAGTGCGAATATCGCTTTGCTAAACAGTGCGTACACCTCTTATTCGGCTCCTATGCAGGTGAAGAACTATCTTAGTGTGCAACGACTCGCTCCGCTGTACTGGTAGGCCTTACTGAGTCCGGTACGATTTAAAGAACGTTCTGACGTACACGTGTCAACCTCGAGATGCTGTCTCCAAGGTGCTGATCGTCAGGACATAGTTCCACAAATAAGTTATTACAAAGAGGTCGTTGGAGTGAGCTGTGCCCGTATCGAGACCTGTAAAACTCCTCTGTTTCAGACGCCTGGCCGCTGCGGGATAATTCCCATATACCCTCGTAATTACTCCCACGCGCTACTCTTTGTTGGATTAATTGATGGACACCGTCCTGTGGTCGTGTTACACGGCCGATAGATTGCGTTAGGGGACGATTGTCATTCCGCTGGAGGATTAAGACTGAATATATCCTCAGCAATACAAGCTTGGAGAGCGCAGAGGCGCACCACCAATTATGATAGTCGGGCTTCGTAAACACATGTTGTGAGTCTTTGCTATGCGCTTATGGCTAGGTTGACGTGTCTATAAAAAAGGCGTGGTCCTAAAAGAAACAGCGTCTCCGTGGCCCACTTACCGTGTATTGTTCGGATCGAACAAGATAGTTCAGAGGTGATAGTCATTACTTCGGTTGATTAAAGGGATTGATTCTTGACAGTCGCGTCTTGGCGACCCGCGGCACTTCTAGTGTTTCATGCTGTCTGCAGTTTACTACCCGTCTCCTGTCAGGCTGACCGGTGTAAGGCTGACCACTTGTTCGAGGAGACGAGCTGAGGTGCTTACGTTGAGCCGGGTACTCTATATCTTCGTTATACGAACTGCTCTGGGACAAAAGTACGGATGCATGCTCGTGGATTAGAAATCAATATTTAACGGAGATCTAGGGTGAAATCCATCTCTACACAAGCCACGTATCAATATCCTGCAGCCGCGCGTAAGCTAAGGAACGAATCAAGAGGTACCCCAGTCGGGCGGGGGACGAGTGAGTCTCAGGTACAGGCACGTGAACCGAGGAATTAGGGCGGTAATATGACTGCCCTCAAACCATAGCCTCATCCGAGCGAGCATCCTGGTCCTTGGTTTAAAATGAGATCTCTGAGATCCCCTTCAGGCGCTTACGCACTAACTTGTCTGACCTCAACTCTGCGGATTTGCTGCGCGTGACATAGTACGCCGGGTACAAGGTCAAACTGGGGAGTAGAATAAGCCCACTATCTTCCTGCACCAACAACGTTCGCCCGCAACGTCACGAACCGAGCTGGCCTCTCGGCCTTCGGAAAGTCGGTACAGCAGGGCGACCGCGGTTTTAACCTTGCATTTTCGAGACATGTTTTCGGTAATCAAACCGGATCCCCGTTTTCTATCGTTGCAGTGCCCCAGGGCAAACTAAATTATTAAGCTGCCTGGTACTGACCTCAGGTTTGGGCGACAAGTCCGTGCCTTGCTGCTAGCTTGTATCCCCTTTAGTCGTGCTATTGCTACTGCAATTCAATATGACGGCGACGCTGAAGTTATATTTCTGCGCCACTCGACACTCCTAAGGATGGAGTACGTTTAACAACTTCGGCGCTATTCCTGGACAATCGTTATCTATTGTATCCAACCGCATCTCACGAATTAGGTATGGTGGTTCTTCGCGTAAGGCCTAATCTGCAGTTTAGTAAAATCAGCCCTTATCAGTTCACCTTTCAGTCAATCTTGTTTCTCCGACATTGGAAGGGCTTCTGACCGCGCCCCTGACAGCCGAGCGTTTTGATCAGGCAAATATCAGTCTGCTGCCACTATCCAGATGTAAAGAGGACAAGGGCTGAAGTGAGGAGTTTTCCACCCCTGAAGAGGGCGTAATGTACCACTGATTTTGTACGGCAGTGGCCGCCCTTCACCCCCGCTGTAATAAATTTCGATCCTGTGGTTATAGAGTACCCACGCCCTGTCCGGGCGGGAGCAGATCACTACCACCTACGGGTCACGATACTGTTGTACGATTTAGGGCGGCCGTTCTAAGAAGACACTTCTATAGGTGAAGATGCAACGGAAATGGAATCTGTTCTACCTAGTAGGATACATAAATAGTGTAACGGTGGCCGCGCGACCGACCGCGGTTTGATCCGAGTCTAGTTCGTTTGGTGGCTACTATTCTTACGTGACGAGCGACGACCCGTAAGGGCGATACGCGCACACACTTGCGGTTGTTGCCCTATGCAGCCCTGTTGACCGGTACACTCAAATGTGGTAGATATTTACGCCCCAGCTCGACGCACGGTCCGCGTCTCGCTAAACCTGGAAGCATTTCTCATAAAGGTTCTACAATGTGGGCACTTGAAAAAATCATTTTACCGCACAGGTGTAACGCCATCGAACTGCAGTTTCAGCTACAGTACTCTTATTGACAATGAGTTAACCTTCCTCATAAACACTTGATACAAGCAGCAGGCCGACTGCATTGTGCCTATCATACTGAACTCCGCTTAGCAAGATTCAACTGCTTGGTAGATTCTCTAGTGATCCCCCCCATAAGTATAGCTCGTGTATAACGCCTCTAAGTGGCGATCCCAGGACTTGCGTCGTCTGGTCTTAGCATAACCGACTTTTTAATTGAAAAAAAGGGATCGGAATGCGCAAAGGTCTATTACCTACACGGGTTGCAAGCGTAAGCTGTCTAGCGTGCCTCGAACATACGCATGGTCCCACGACCATTACACACACTAGCTCACCGATGGTTTTGTCTGGCGATCCCGCACGAGACTCAACAAAGAGTGTTCCCTTAGAGATGGCCGCTTGACAGACTGCACCAAGCCGCAGTAACCCTTGAGGTCGCCCAATACAGGCGAATGTTAGCTTCGAACCCGGGTAAAGATCCGTAACGGTCTCGAATTATTGGCAACAACCGTTGTCCTGTATGTATCCATAGATCGTAAAGCTAGATTCAGCTTACGCGAGAATGTATAGCTGAAAGCAGGGGTTAAACGGCTAAAGCGACAGCAGTTATTCTAGAAGATTAAAGGCTCTCCGTTTTGGCCGATTCTCCAAACAATCGAAGTTTAGTATCGTAGCCCCCGTCCGTATAATGCGAGAGTTAGGCCCACACCGTGGGGTGGTAGTACGGACCCAGAATGTGTAGTCGGCAAGAACTCTACGTGCTTCGCTCCTTTATATCGTTGATTTCAATTGGCATCCGGGCAGGTGGCCTTGGCGTCAAAATGCGCGTCTGCACATGCGGGAATGAATTCCCGATAGATTCTTTTATATCAAGGGTCCATCCGGAAAGGGAAAGTAGGTGGTCCAGATACGAAAATCGCCATGTCCATTAATTGATCTCAGTGTTACTGAGAGCGGTATTCGTATTGCAAGTTGCTTGGGGCAGTCAATCGTCTCACTCATGCTACTTGCATTTGTCTTACTAGTATATGGATCAGTTAATTATCTAGCAATTTGTGACCAGAAAGATCCACCGAGGCTTCTCCAACGGGTCCAATCCGTGCCCATACAATCTGTCCCGTGCTGGTTTGATTCCGCCACAAGCGCTTCGAACTTTCGTCCAGCTCTGCGCCTGAATTCCGTTGCAATGACAACATGGTAGGCTCGGTATGTTCGCCTAAAGAGCAGATCGATTTTGATTTCTTGCCGCGACTCTATCGCGTTGGACATGCAGCTAACCGAACTGACCTGTCCCGCCGGACCATAGAGAGTCTATGCTCCCGGGTCTGTCGCGGCACTGTCCCTCTAAAAACAGGGCACGTGAGCCTGAGGCATCCACCTAGCGTATCCGTAGGGCGATTGCCTATTAGTGCCAAACGCTTCAATTGTTCACTGTCCCTGGGCAAGATGGGTCTCGCGTAGAGACTTTTCGTCTGGTCTGTACCCGACTTCTTCAGGTTGCTTAGAACAATTGGCCCAGCGGGTAACGATTATCTAGGGTAGTCTAGCCTTCCGTTTTCCCTATTCTTCATTGGCCAAGGCTTGTCTTTGAAACTTGCACGGGGGACGAGCTGGCTATGCTTCCTTGTGTCCGATTACCGCTACTACCATGTGACCGAGTGTAGGCGTACATGAGGCGAACTACGTTCAAGTAGTGTTCAGACTGCCCCAATGGGATAAATATGTGCCTCTCCACCCGATCCATCTAAGGAAAGCGAAAAGTAGGAGGTTACATCGGTGCGGACTCTACACTCCCCGGGCAAATTGGGATATTAGAGTAGTGCTATGAGCGAAGTTGTGCGGATGCCTGCCGGCGCTGGAAAGAATCGCGTAGAGTTTTCTAATCTGACTTGGCTTTTCTGGATGGCGGAACAATTCAAAATAGCCCTAAGTGCGGAGAGCGATCGCAGCCGAGGCCATGGACCCTGACCTGGGTTCGTCCGTTTGATCCACACAACCCCAGGTACTGCGCTTACTTATATGAAAGTATCTTCAGATCAGAACTCTTGCGGAACTTACAAGAGTACGCCTCCGGCATTCCCGATAAGGGCTGTTGGAATCCAGGCATTTGGATAAACGCCATTGACTCTGCTTGTCTGGTTTGGCTATCTATCCGTACTACCTCTCCTAGCCATGGGTGCATGGGTTCCCCCGGACGGTCGTCAATAGCACGTATTGACTCCATGTTCTCCGGAGTCAAGTTCACTACGTCTCTTTTGTGCGAGTAAGCTTTTTTCAGTAACATAGGGGGGTGTTTTGTTCGAGCCCGTCTATATTGACACATAATGAAACCCTCAGAGACCCATCTTGTCAGGGTATGTTGAGTTTAGCTTTTGCGACTAAAGTTGGCGCTTCATCAAATTCGGAG'

rev_comp = ''
for char in text:
    rev_comp+=complement_dict[char]
rev_comp = rev_comp[::-1]

print(rev_comp)