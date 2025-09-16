import re

Sentence = "Pure mathematics is, in its way, the poetry of logical ideas"
Vowels = "aeiouyåäö"
VowelsSearch = f"[{Vowels}]"
match_list = re.findall(VowelsSearch, Sentence.lower())
NrOfVowels = len(match_list)
print(f"There are {NrOfVowels} vowels in this Sentence")