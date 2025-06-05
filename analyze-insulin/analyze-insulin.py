import re

# Reads in unprocessed protein sequence from file
with open('preproinsulin-seq.txt') as preproinsulin_seq_file:
    preproinsulin_seq = preproinsulin_seq_file.read()
    result = re.findall(r"(([a-z]+\s*)+\n)", preproinsulin_seq)
    # Converting sequence into single string of lower case letters
    cleaned_seq = ""
    for x in range (0, len(result)):
        cleaned_seq = cleaned_seq + result[x][0].strip()
    cleaned_seq = cleaned_seq.replace(" ", "")
    # Writing cleaned sequence to file
    with open("preproinsulin-seq-clean.txt", "w") as preproinsulin_seq_clean_file:
        preproinsulin_seq_clean_file.write(cleaned_seq)