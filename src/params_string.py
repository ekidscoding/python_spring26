# стандартна версія з РЯДКОМ тексту

def aggregate_standard(a: int,
                       b: int,
                       c: int,
                       action: str
                       ) -> int:
  """Функція застосовує операцію 'action' до трьох
  доданків (множників) і повертає суму (добуток)"""
  first_result = end_result = None
  if action.lower() in ["+",
                        "add",
                        "plus",
                        "addition"]:
    first_result = a + b
    end_result = first_result + c
  if action.lower() in ["*",
                        "mul",
                        "multi",
                        "multiply",
                        "multiplication"]:
    first_result = a * b
    end_result = first_result * c
  if end_result is None:
    raise ValueError(f"Unknown {action=}")
  return end_result

def main():
  print(aggregate_standard(1, 2, 3, "+"))
  print(aggregate_standard(1, 3, 5, "mul"))

if __name__=='__main__':
  main()
