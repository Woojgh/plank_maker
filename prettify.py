import json

def to_string(pairs): 
  
  str_pairs = ''.join(str(e) for e in pairs)

  return str_pairs

def clean_square(pairs):
    return pairs.replace('[', '').replace(']','') 

def clean_semi(pairs): 

    return pairs.replace('(', '').replace(')', '\n')

def clean_quotes(pairs): 

  return pairs.replace("'", " ").replace("'", " ")

def correct_name(pairs): 
 
  return pairs.replace('ilker zaimoglu', 'James Bond')

# def add_new_line(pairs):
#   pairs.

def make_pretty(pairs): 
  pretty_pairs = to_string(pairs)
  pretty_pairs = clean_square(pretty_pairs)    
  pretty_pairs = clean_semi(pretty_pairs)
  pretty_pairs = clean_quotes(pretty_pairs)
  pretty_pairs = correct_name(pretty_pairs)

  return pretty_pairs
