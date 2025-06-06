import re

"""Small Tasks for analyzing the amino acid sequence of the human insulin protein. Sequence taken from https://www.ncbi.nlm.nih.gov/protein/AAA59172.1"""

def get_seq_from_file(source_file_name):
    """Reads a sequence from a file with the given name and returns sequence"""
    with open(source_file_name) as source_file:
        seq = source_file.read()
        return seq

def get_cleaned_seq(raw_input_seq, length_of_cleaned_seq):
    """Cleans given sequence and returns it as sequence of lower letters without whitespaces or None."""
    result = re.findall(r"(([a-z]+\s*)+\n)", raw_input_seq)
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

def calculate_net_charge(sequence, pH):
    """Calculates and returns the net-charge of the protein with the given sequence at the given pH value"""
    # Dictionary with the pKR value, the charge state of an amino acid.
    # Only the amino acids Y, C, K, H, R, D, and E are relevant for net-charge calculation
    pKR = {
        "y" : 10.07,
        "c" : 8.18,
        "k" : 10.53,
        "h" : 6.00,
        "r" : 12.48,
        "d" : 3.65,
        "e" : 4.25
    }
    # Counts the occurance of each amino acid in the sequence that influences the net-charge calculation
    seq_count = ({x: float(sequence.count(x)) for x in ["y", "c", "k", "h", "r", "d", "e"]})

    # Calculates and returns net-charge
    return (
        +(sum({x: ((seq_count[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seq_count[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values())))
    

prepro_insulin_file_name = "analyze-insulin/preproinsulin-seq.txt"
cleaned_prepro_insulin_file_name = "analyze-insulin/preproinsulin-seq-clean.txt"
cleaned_prepro_insulin_seq_length = 110

# Extracting and cleaning sequence
prepro_insulin_seq = get_seq_from_file(prepro_insulin_file_name)
cleaned_prepro_insulin_seq = get_cleaned_seq(prepro_insulin_seq, cleaned_prepro_insulin_seq_length)
# write_to_file(cleaned_prepro_insulin_file_name, cleaned_prepro_insulin_seq)

sig_peptide_insulin_file_name = "analyze-insulin/sig-peptide-insulin-seq-clean.txt"
sig_peptide_seq_start = 0
sig_seq_length = 24

# Extracting signal peptide sequence
sig_insulin_seq = extract_peptide_sequence(cleaned_prepro_insulin_seq, sig_peptide_seq_start, sig_seq_length)
# write_to_file(sig_peptide_insulin_file_name, sig_insulin_seq)

b_insulin_file_name = "analyze-insulin/binsulin-seq-clean.txt"
b_insulin_seq_start = 24
b_insulin_seq_length = 30
# Exctracting sequence of B insulin
b_insulin_seq = extract_peptide_sequence(cleaned_prepro_insulin_seq, b_insulin_seq_start, b_insulin_seq_length)
# write_to_file(b_insulin_file_name, b_insulin_seq)

c_insulin_file_name = "analyze-insulin/cinsulin-seq-clean.txt"
c_insulin_seq_start = 54
c_insulin_seq_length = 35
# Exctracting sequence of C insulin
c_insulin_seq = extract_peptide_sequence(cleaned_prepro_insulin_seq, c_insulin_seq_start, c_insulin_seq_length)
# write_to_file(c_insulin_file_name, c_insulin_seq)

a_insulin_file_name = "analyze-insulin/ainsulin-seq-clean.txt"
a_insulin_seq_start = 89
a_insulin_seq_length = 21
# Exctracting sequence of C insulin
a_insulin_seq = extract_peptide_sequence(cleaned_prepro_insulin_seq, a_insulin_seq_start, a_insulin_seq_length)
# write_to_file(a_insulin_file_name, a_insulin_seq)

# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:")
print(cleaned_prepro_insulin_seq)

# Printing to console using concatenated stings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + a_insulin_seq)

# Complete sequence of human insulin protein composed of A-chain and B-chain
insulin_seq = b_insulin_seq + a_insulin_seq

# pH value influences the net-charge calculation
pH = 0
# Iterating over pH values and printing the calculated net-charge for the human insulin protein
while (pH <= 14):
    netCharge = calculate_net_charge(insulin_seq, pH)
    print("{0:.2f}".format(pH), netCharge)
    pH += 1