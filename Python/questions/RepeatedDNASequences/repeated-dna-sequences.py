from collections import Counter

def find_repeated_dna_sequences(s: str) -> list[str]:
        if len(s) < 10:
            return []
        
        counter = Counter(s[i: i + 10] for i in range(len(s) - 10 + 1))
        
        return [key for key in counter if counter[key] > 1]


if __name__ == "__main__":
    print(find_repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print(find_repeated_dna_sequences("AAAAAAAAAAAAA"))