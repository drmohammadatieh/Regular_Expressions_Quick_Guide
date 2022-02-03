# This is a quick guide on regular expressions in python, I hope it helps.
# Author: @drmohammdatieh :https://github.com/drmohammadatieh
# Reference: https://www.programiz.com/python-programming/regex

import re

# Different examples of match patterns
digit ='\d'
digit_and_count = '\d{6}'
non_digit = '\D'
white_space ='\s'
no_white_space='^\s'
alpha_numeric = '\w'
non_alpha_numeric = '\W'
set_pattern = '([^1-3])'
group_patterns = '(\d{6})([a-bA-Z])'
any_character = '.'
starts_with_123 = '^123'
starts_with_123_2 = '\A123'
does_not_start_with_123 = '^\A123'
ends_with = 'A$'
contains_zero_or_more_123 = '123*'
contains_one_or_more_123 = '123+'
contains_zero_or_one_123 ='123?'
contains_1_to_four_123 = '123{1,4}'
containts_the_first_or_second = 'a|b'
contains_metacharacters = '\[[] . ^ $ * + ? {} () \ |]' # Metacharacters have a
#special meaning that is different than regular characters; they are used in the regular expression patterns.

print("Examples of match patterns:")
print("") # Print new line
print("\
digit ='\d'\n\
digit_and_count = '\d{6}'\n\
non_digit = '\D'\n\
white_space ='\s'\n\
no_white_space='^\s'\n\
alpha_numeric = '\w'\n\
non_alpha_numeric = '\W'\n\
set_pattern = '([^1-3])'\n\
group_patterns = '(\d{6})([a-bA-Z])'\n\
any_character = '.'\n\
starts_with_123 = '^123'\n\
starts_with_123_2 = '\A123'\n\
does_not_start_with_123 = '^\A123'\n\
ends_with = 'A$'\n\
contains_zero_or_more_123 = '123*'\n\
contains_one_or_more_123 = '123+'\n\
contains_zero_or_one_123 ='123?'\n\
contains_1_to_four_123 = '123{1,4}'\n\
containts_the_first_or_second = 'a|b'\n\
contains_metacharacters = '\[[].^$*+?{}()\|]'\
")

# Test strings
numeric_string = '123456'
alphanumeric_string = '123456A'
alphabetic_string ='abcdefg'
starts_and_ends_with_A= 'A123123123456A'
metacharacter_string = '$'
string_with_spaces ='a space next   to this'
string_without_spaces ='abcdefg'
non_alpha_numeric_string = ' %^%'

print("") # Print new line
print("Test strings:")
print("") # Print new line
print("\
numeric_string = '123456'\n\
alphanumeric_string = '123456A'\n\
alphabetic_string ='abcdefg'\n\
starts_and_ends_with_A= 'A123123123456A'\n\
metacharacter_string = '$'\n\
string_with_spaces ='a space next   to this'\n\
string_without_spaces ='abcdefg'\n\
non_alpha_numeric_string = ' %^%'\n\
")

# Search if there is a match (This method search for the first match only)
is_there_a_digit = re.match(digit,numeric_string)
print(
    f"The result of digit search using 're.match(digit,numeric_string)' is a match object :\
{is_there_a_digit}\n" if is_there_a_digit 
else "There was no any digit found\n")

# Find the matches and return them in a form of a list
find_and_return_match = re.findall(digit, alphanumeric_string)
print(
    f"The result of find and return match using 're.findall(digit, alphanumeric_string)' is: {find_and_return_match}\n"
if find_and_return_match 
else "There were no matches found\n" )

# Split at the match and return the splits
split_at_match = re.split('\*', string_with_spaces)
print(
    f"The result of split at match using 're.split(' ', string_with_spaces)' is: {split_at_match}\n" if split_at_match 
else f"{split_at_match} if match is not found\n" )

# Split at the match for a maximum of two splits and resturn the splits
split_at_match_max_2_splits = re.split(' ', string_with_spaces,2)
print(
    f"The result of split at match with maximum of two splits using 're.split(' ', string_with_spaces,2)'\
with maxsplit argument set at 2 is: {split_at_match_max_2_splits}\n" if split_at_match_max_2_splits 
else "There were no matches so no splits were done\n" )

# Substitute the match
substitute_the_match = re.sub(' ', '*', string_with_spaces)
print(
    "The result of subsitute at the match using 're.sub(' ', '*', string_with_spaces)' is: ",
substitute_the_match,"\n")

# Search and retrun a match object or None if there is no  match
search_for_a_match = re.search('(\d *)(\d *)(\d *)',"1 2 3" )
print(
    f"The result of search for a match using 're.search('(\d *)(\d *)(\d *)','1 2 3')' is a match object that looks like: {search_for_a_match}\n"\
         if search_for_a_match else "No match was found\n")

print('You can use different match objects methods like the following:\n')
print("search_for_a_match.groups() will give a tuple of the match",search_for_a_match.groups(),"\n")
print("search_for_a_match.group() will give a string of the match",search_for_a_match.group(),"\n")
print("search_for_a_match.group(1) will give the first part of the match",search_for_a_match.group(1),"\n")
print("search_for_a_match.group(2) will give the second part of the match",search_for_a_match.group(2),"\n")
print("search_for_a_match.group(3) will give the third part of the match",search_for_a_match.group(3),"\n")
print('The match started at index: ', search_for_a_match.start(),"\n")
print('The match ended at index: ', search_for_a_match.end(),"\n")
print('The match span was: ', search_for_a_match.span(),"\n")

# Finding a raw string using the r prefix to ignore the metacharacters

search_for_a_raw_string = re.findall(r'\n','This string contains escape character\n')
print(f"The result of searching for a raw string using 're.findall(r'\\n','This string contains escape character\\n'): {search_for_a_raw_string}")

