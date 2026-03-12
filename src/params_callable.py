from typing import Callable

def add(
        a: int,
        b: int
      ) -> int:
  return a + b

def mul(
        m: int,
        n: int
      ) -> int:
  return m * n

def aggregate_function(a: int,
                       b: int,
                       c: int,
                       action: Callable[[int, int], int]
                       ) -> int:
  """Функція застосовує ФУНКЦІЮ 'action' до трьох
  доданків (множників) і повертає суму (добуток)"""
  first_result = action(a, b)
  return action(first_result, c)

def main():
  print(aggregate_function(1, 2, 3, add))
  print(aggregate_function(1, 3, 5, mul))

if __name__=='__main__':
  main()
