from lib.var_dec import VarDec
from lib.var_name import VarName

class BinaryOp:
  def __init__(self, op, left, right):
    self.left = left
    self.right = right
    self.op = op
  
  def __repr__(self):
    return f"{self.left} {self.op} {self.right}"
  
  def exec(self, context):
    if self.op == '=':
      if type(self.right) is BinaryOp:
        context[self.left.name] = self.right.exec(context)
      else:
        context[self.left.name] = self.right
    elif self.op in ['+', '-', '*', '/']:
      left = self.left.exec(context) if type(self.left) in [BinaryOp, VarName] else self.left
      right = self.right.exec(context) if type(self.right) in [BinaryOp, VarName] else self.right
      
      return eval(f"{left} {self.op} {right}")
      