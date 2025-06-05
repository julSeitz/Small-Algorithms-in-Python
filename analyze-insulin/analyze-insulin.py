import re

def get_cleaned_seq(source_file_name, target_file_name, length_of_cleaned_seq):
    """Reads in sequence from source file, cleans it into a sequence of lower letters without whitespaces, then writes it to taget file."""
    # Reads in unprocessed protein sequence from file
    with open(source_file_name) as input_file:
        preproinsulin_seq = input_file.read()
        result = re.findall(r"(([a-z]+\s*)+\n)", preproinsulin_seq)
        # Converting sequence into single string of lower case letters
        cleaned_seq = ""
        for x in range (0, len(result)):
            cleaned_seq = cleaned_seq + result[x][0].strip()
        cleaned_seq = cleaned_seq.replace(" ", "")
        if len(cleaned_seq) != length_of_cleaned_seq:
            print("Cleaned sequence does not match projected length")
            return
        # Writing cleaned sequence to file
        with open(target_file_name, "w") as cleaned_seq_file:
            cleaned_seq_file.write(cleaned_seq)
            print(f"Wrote cleaned sequence to {target_file_name}")

def  extract_peptide_sequence(source_file_name, target_file_name, start_of_seq, length_of_seq):
    """Extracts the sequence of the desired peptide from the sequence contained in the source file, writes result to target file."""
    # Reads in cleaned sequence from file
    with open(source_file_name) as source_file:
        sequence = source_file.read()
        # Extracts sequence of target peptide
        end_of_sequence = start_of_seq + length_of_seq
        peptide_sequence = sequence[start_of_seq:end_of_sequence]
        # Checks if extracted sequence matches projected length
        if len(peptide_sequence) != length_of_seq:
            print("Target peptide sequence length does not match its projected length")
            return
        # Writes sequence of target peptide to file
        with open(target_file_name, "w") as target_file:
            target_file.write(peptide_sequence)
            print(f"Wrote target peptide sequence to {target_file_name}")

input_file_name = "analyze-insulin/preproinsulin-seq.txt"
cleaned_seq_file_name = "analyze-insulin/preproinsulin-seq-clean.txt"
length_of_cleaned_seq = 110

ls_insulin_file_name = "analyze-insulin/lsinsulin-seq-clean.txt"
start_of_sig_peptide_seq = 0
length_of_sig_seq = 24

get_cleaned_seq(input_file_name, cleaned_seq_file_name, length_of_cleaned_seq)
# Extracting signal peptide sequence
extract_peptide_sequence(cleaned_seq_file_name, ls_insulin_file_name, start_of_sig_peptide_seq, length_of_sig_seq)