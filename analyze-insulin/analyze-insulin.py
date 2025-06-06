import re

def get_seq_from_file(source_file_name):
    """Reads a sequence from a file with the given name"""
    with open(source_file_name) as source_file:
        seq = source_file.read()
        return seq

def get_cleaned_seq(preproinsulin_seq, length_of_cleaned_seq):
    """Cleans given sequence and returns it as sequence of lower letters without whitespaces or None."""
    result = re.findall(r"(([a-z]+\s*)+\n)", preproinsulin_seq)
    # Converting sequence into single string of lower case letters
    cleaned_seq = ""
    for x in range (0, len(result)):
        cleaned_seq = cleaned_seq + result[x][0].strip()
    cleaned_seq = cleaned_seq.replace(" ", "")
    if len(cleaned_seq) != length_of_cleaned_seq:
        print("Cleaned sequence does not match projected length")
        return
    return cleaned_seq

def  extract_peptide_sequence(peptide_seq, start_of_seq, length_of_seq):
    """Extracts the sequence of the desired peptide from the given sequence and returns it or None"""
    # Extracts sequence of target peptide
    end_of_sequence = start_of_seq + length_of_seq
    peptide_sequence = peptide_seq[start_of_seq:end_of_sequence]
    # Checks if extracted sequence matches projected length
    if len(peptide_sequence) != length_of_seq:
        print("Target peptide sequence length does not match its projected length")
        return
    return peptide_sequence

def write_to_file(target_file_name, seq):
    """Writes the given sequence to target file"""
    if seq == None:
        print("Given sequence is empty, cant write to file.")
        return
    # Writes sequence of target peptide to file
    with open(target_file_name, "w") as target_file:
        target_file.write(seq)
        print(f"Wrote target sequence to {target_file_name}")

input_file_name = "analyze-insulin/preproinsulin-seq.txt"
cleaned_seq_file_name = "analyze-insulin/preproinsulin-seq-clean.txt"
length_of_cleaned_seq = 110

# Extracting and cleaning sequence
prepro_seq = get_seq_from_file(input_file_name)
cleaned_prepro_seq = get_cleaned_seq(prepro_seq, length_of_cleaned_seq)
# write_to_file(cleaned_seq_file_name, cleaned_prepro_seq)

ls_insulin_file_name = "analyze-insulin/lsinsulin-seq-clean.txt"
start_of_sig_peptide_seq = 0
length_of_sig_seq = 24

# Extracting signal peptide sequence
sig_insulin_seq = extract_peptide_sequence(cleaned_prepro_seq, start_of_sig_peptide_seq, length_of_sig_seq)
# write_to_file(ls_insulin_file_name, sig_insulin_seq)

b_insulin_file_name = "analyze-insulin/binsulin-seq-clean.txt"
start_of_b_peptide_seq = 24
length_of_b_seq = 30
# Exctracting sequence of B insulin
b_insulin_seq = extract_peptide_sequence(cleaned_prepro_seq, start_of_b_peptide_seq, length_of_b_seq)
# write_to_file(b_insulin_file_name, b_insulin_seq)

c_insulin_file_name = "analyze-insulin/cinsulin-seq-clean.txt"
start_of_c_peptide_seq = 54
length_of_c_seq = 35
# Exctracting sequence of C insulin
c_insulin_seq = extract_peptide_sequence(cleaned_prepro_seq, start_of_c_peptide_seq, length_of_c_seq)
# write_to_file(c_insulin_file_name, c_insulin_seq)

a_insulin_file_name = "analyze-insulin/ainsulin-seq-clean.txt"
start_of_a_peptide_seq = 89
length_of_a_seq = 21
# Exctracting sequence of C insulin
a_insulin_seq = extract_peptide_sequence(cleaned_prepro_seq, start_of_a_peptide_seq, length_of_a_seq)
# write_to_file(a_insulin_file_name, a_insulin_seq)

# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:")
print(cleaned_prepro_seq)

# Printing to console using concatenated stings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + a_insulin_seq)