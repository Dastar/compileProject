import sys
import enum


class SyntaxError(Exception):
   def __init__(self, error):
      self.Error = error


class Symbols(enum.Enum):
   Number = 0
   Char = 1


class Reader:
   def __init__(self, input_file):
      self._file = input_file
      self.content = ""
      self.runner = 0
      self.length = 0
      
   def open_file(self):
      with open(self._file, 'r') as f:
         self.content = f.read()
      self.length = len(self.content)
         
   def get_expr(self): 
      if self.content[self.runner].isdigit():
         return self.read_number(), Symbols.Number
      else:
         return self.read_symbol(), Symbols.Char
         
   def read_number(self, depth = 1):
      if depth < 0:
         raise SyntaxError("Bad character")
      number = 0
      content = self.content
      while content[self.runner].isdigit():           
         number *= 10
         number += int(content[self.runner])
         self.runner += 1
         
      if content[self.runner] == '.':
         self.runner += 1
         dec = 1.0 / self.read_number(depth - 1)
         number += dec
         
      return number
      
   
      
   def read_symbol(self):
      symbol = self.content[self.runner]
      self.runner += 1
      return symbol
      
   def is_end_file(self):
      return self.runner >= self.length
      

class SimpleCalcualtor:
   def __init__(self, input_file):
      self.reader = Reader(input_file)
      self.stack = []
      self.stmts = {Symbols.Number : self.read_number, Symbols.Char : self.read_char}
   
   def run(self):
      try:
         self.reader.open_file()
         while not self.reader.is_end_file():
            expr, symbol = self.reader.get_expr()
            self.stmts[symbol](expr)
         
         if len(self.stack) != 1:
            raise SyntaxError("Too many numbers")
         print(self.stack.pop())
         
      except SyntaxError as e:
         print(e.Error)
      except Exception as e:
         print(e)
   
   def read_number(self, expr):
      self.stack.append(expr)
   
   def read_char(self, expr):
      if expr == '+':
         a = self.stack.pop()
         b = self.stack.pop()
         self.stack.append(b + a)
      elif expr == '-':
         a = self.stack.pop()
         b = self.stack.pop()
         self.stack.append(b - a)
   
      

er = SimpleCalcualtor("prog.calc")
er.run()
#for arg in sys.argv:
#   print(arg)
