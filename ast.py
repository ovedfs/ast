from lib.program import Program
from lib.binary_op import BinaryOp
from lib.var_dec import VarDec
from lib.var_name import VarName

program1 = Program(
  # var a = 5
  BinaryOp('=', VarDec('a'), 5),

  # var b = 8
  BinaryOp('=', VarDec('b'), 8),

  # var res = a * 2 + b / 4
  BinaryOp('=', 
    VarDec('res'), 
    BinaryOp('+', 
             BinaryOp('*', 
                      VarName('a'), 2), 
              BinaryOp('/', 
                      VarName('b'), 4))),

  # var res2 = a + b
  BinaryOp('=', 
           VarDec('res2'), 
           BinaryOp('+', 
                    VarName('a'), 
                    VarName('b'))),

  # var res3 = 24 / res + res2 * a
  BinaryOp('=', 
           VarDec('res3'), 
           BinaryOp('+', 
                    BinaryOp('/', 
                             24, 
                             VarName('res')), 
                    BinaryOp('*', 
                             VarName('res2'), 
                             VarName('a'))))
)

print(program1)
program1.exec()
