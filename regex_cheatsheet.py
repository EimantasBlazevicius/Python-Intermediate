import re

# Base for Cheatsheet
play_string = '''abcdefghijklmnopqurtuvwxyz
abcDefghijklmNopqurtuvwxyZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
lietuva.com
ac
+37060482010
}37060482010
+370.604.82.010
+370-604-82-010
+aaa-604-82-010
+ddd-604-82-010
-37060482010
111.999.6699
eima.blaz@gmail.com_'''

test_full_match = "abcdd"

patternText = re.compile(r'ac')
patternAnyCharacter = re.compile(r'.')
patternDigits = re.compile(r'\d')
patternNotDigits = re.compile(r'\D')
patternCharacters = re.compile(r'\w')
patternNotCharacters = re.compile(r'\W')
patternWhitespaces = re.compile(r'\s')
patternNoWhitespaces = re.compile(r'\S')

patternWordBoundry = re.compile(r'\bHa')
patternNoWordBoundry = re.compile(r'\BHa')
patternStartOfTheString = re.compile(r'^abc')
patternEndOfTheString = re.compile(r'.com_$')

patternListOfOptions = re.compile(r'[+-]37060482010')
patternListOfNOTOptions = re.compile(r'[+-]37060482010')
patternGrouping = re.compile(r'\+(\d\d\d).(\d\d\d).(\d\d.\d\d\d)')
patternGroupingWithOr = re.compile(r'\+(\d\d\d|\w\w\w).(\d\d\d).(\d\d.\d\d\d)')
patternZeroOrMore = re.compile(r'\+370*')
patternOneOrMore = re.compile(r'\+370+')
patternOptionalCharacters = re.compile(r'ab?c')
patternExactNumber = re.compile(r'\d{3}\.\d{3}\.\d{2}')
patternWithRange = re.compile(r'\d{3}\.\d{3}\.\d{2,4}')

patternForSplit = re.compile(r'\.')
pattern = re.compile(r'abcdefghijklmnopqurtuvwxyz', re.I)

# Finds first occurance of the pattern
resultSearch = pattern.search(play_string)
# Matching the start of the string
resultMatchStartOfTheString = pattern.match(play_string)
# Testing if string is exactly as per pattern
resultExactMatch = pattern.fullmatch(test_full_match)
# print(result)
# finds all the occurrences and returns the list
resultFindAll = pattern.findall(play_string)
# Same as FindAll, but returns Iterator of Regex objects
resultFindIter = pattern.finditer(play_string)
# Splits by Pattern occurance
resultSplit = pattern.split(play_string)
# Substitutes the value with new one
resultSub = pattern.sub("dog", play_string)
# Substitutes the value with new one and shows how many times it happened
result = pattern.subn("dog", play_string)
print(result)

for match in result:
    print(match)


