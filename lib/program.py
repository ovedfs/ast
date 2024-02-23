class Program:
  def __init__(self, *exp):
    self.instructions = exp

  def __repr__(self):
    return "\n".join([repr(item) for item in self.instructions]) or ""
  
  def exec(self, context = {}):
    try:
      for inst in self.instructions:
        inst.exec(context)
      print(context)
    except Exception as e:
      print(f"Error: {e}")
