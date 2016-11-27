#!/usr/bin/python

import itertools

def get(filename):
  return set(line.strip() for line in open(filename))

def combine(phrases = [], syllables_count = 3):
  return list(itertools.permutations(phrases, syllables_count))

def join(units):
  return "".join(units)

def eliminate(phrase_combinations, filters = []):
  return filter(evaluate_filters(filters), phrase_combinations)  

def evaluate_filters(filters):
  def filter_input(value):
    cursor = iter(filters)
    while True:
      try:
        f = next(cursor)
        if not f(value):
          return False
      except StopIteration:
        break
    return True
  return filter_input

def filter_invalid_phrase(phrase_combination):
  return True

def filter_similar_adjacent_terminals(phrase_combination):
  print("here")
  cursor = iter(phrase_combination)
  a = next(cursor)
  while True:
    try:
      b = next(cursor)
      print("{} and {} for {}".format(a, b, phrase_combination))
      if b[0] == a[-1]:
        return False
      a = b
    except StopIteration:
      break
  return True
  
in_file = 'syllables.txt'
out_file = 'gen.txt'

filters = [filter_similar_adjacent_terminals]
options = list(map(lambda x: join(x), eliminate(combine(get(in_file)), filters)))

with open(out_file, 'w') as fp:
  print("\n".join(options),  file=fp) #list(map(lambda x: , options)))
