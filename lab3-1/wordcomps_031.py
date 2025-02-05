#!/usr/bin/env python3

# s/i = read words from sys.stdin & stores them in a list

import sys

words = [word.strip() for word in sys.stdin]
# print([word for word in words if len(word) == 17])
# [word for word in words if len(word) == 17]

def fourAs(word):
	count = 0
	for i in range(0, len(word)):
		if word[i] in "aA":
			count += 1
	if count == 4:
		return True
	else:
		return False
def plusQs(word):
	count = 0
	for i in range(0, len(word)):
		if word[i] in "qQ":
			count += 1
	if count > 1:
		return True
	else:
		return False

def anagram(word):
	matched = True
	angel = "angle"
	word = word.casefold()
	if word != angel:
		for char in word:
			if char in angel:
				angel = angel.replace(char, "", 1)
				word = word.replace(char, "", 1)
		if not(len(word) == 0 and len(angel) == 0):
			matched = False
	else:
		matched = False

	return(matched)

print("Words containing 17 letters:", [word for word in words if len(word) == 17])
print("Words containing 18+ letters:", [word for word in words if len(word) > 17])
print("Words with 4 a's:", [word for word in words if fourAs(word)])
print("Words with 2+ q's:", [word for word in words if plusQs(word)])
print("Words containing cie:", [word for word in words if ("cie" in word) or "Cie" in word])
print("Anagrams of angle:", [word for word in words if anagram(word)])


# python3 wordcomps_031.py < dictionary05.txt
# Words containing 17 letters: ['contradistinguish', 'counterproductive', 'counterrevolution', 'electrocardiogram', 'indistinguishable', 'paleoanthropology', 'psychotherapeutic', 'spectrophotometer']
# Words containing 18+ letters: ['arteriolosclerosis', 'counterrevolutionary', 'diethylstilbestrol', 'electrocardiograph', 'electroencephalogram', 'electroencephalograph', 'electroencephalography', 'immunoelectrophoresis', 'triphenylphosphine']
# print(len(['Alabama', 'Alabamian', 'amalgamate', 'Anastasia', 'Appalachia', 'Atalanta', 'Athabascan', 'baccalaureate', 'bacchanalian', 'Bhagavadgita', 'extravaganza', 'Macadamia', 'Madagascar', 'maharaja', 'Maharashtra', 'Mahayana', 'Nakayama', 'Panamanian', 'Paraguayan', 'paraphernalia', 'parliamentarian', 'Santayana', 'sarsaparilla', 'tarantara']))
# Words with 2+ q's: ['Albuquerque']
# Words containing cie: ['ancient', 'coefficient', 'concierge', 'conscience', 'conscientious', 'deficient', 'efficient', 'financier', 'glacier', 'hacienda', 'inefficient', 'insufficient', 'Muncie', 'omniscient', 'proficient', 'science', 'scientific', 'scientist', 'societal', 'Societe', 'society', 'specie', 'species', 'sufficient']
# Anagrams of angle: ['angel', 'Galen', 'glean', 'Lange']