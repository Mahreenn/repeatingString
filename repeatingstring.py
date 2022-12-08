import csv
import sys

def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit(f"Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable.
    database = sys.argv[1]
    f1 = open(database,'r')
    reader1 = csv.reader(f1)
    STRs = next(reader1)[1:]

    # TODO: Read DNA sequence file into a variable
    DNAsequence = sys.argv[2]
    with open(DNAsequence,'r') as f2:
        reader2 = f2.read()

    # TODO: Find longest match of each STR in DNA sequence
    #populating an empty dictionary to store number for each STR
    dna_received = [longest_match(reader2,str) for str in STRs]
    #STR_dna={}
    #for str in STRs:
    #    STR_dna[str] = longest_match(str,reader2)

    # TODO: Check database for matching profiles
    for row in reader1:
        person = row[0]
        values  = [int(val) for val in row[1:]]
        if values == dna_received:
            print(person)
            return
    print("No match")

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

if __name__=="__main__":
    main()