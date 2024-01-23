def gc_duplets(base_seq):
 seq = base_seq.upper()
 valid = seq.count("A") + seq.count("C") + seq.count("G")+seq.count("U")
 if valid !=len(seq):
   print("invalid sequence")
 else:
   print ("Cs:",seq.count('C'))
   print ("GVs:",seq.count('GC'))
 seq1 = 'AAGCGCUUGCG'
 gc_duplets(seq1)
