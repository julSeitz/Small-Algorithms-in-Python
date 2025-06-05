import re

def get_cleaned_seq(input_file_name, cleaned_seq_file_name, length_of_cleaned_seq):
    # Reads in unprocessed protein sequence from file
    with open(input_file_name) as input_file:
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
        with open(cleaned_seq_file_name, "w") as cleaned_seq_file:
            cleaned_seq_file.write(cleaned_seq)
            print(f"Wrote cleaned sequence to {cleaned_seq_file_name}")

input_file_name = "analyze-insulin/preproinsulin-seq.txt"
cleaned_seq_file_name = "analyze-insulin/preproinsulin-seq-clean.txt"
length_of_cleaned_seq = 110

get_cleaned_seq(input_file_name, cleaned_seq_file_name, length_of_cleaned_seq)