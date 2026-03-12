def add(a, b):
  return a + b

def mul(m, n):
  return m * n

def aggregate_function(a, b, c, action):
  """Функція застосовує ФУНКЦІЮ 'action' до трьох
  доданків (множників) і повертає суму (добуток)"""
  first_result = action(a, b)
  return action(first_result, c)


def main():
  print(aggregate_function(1, 2, 3, add))
  print(aggregate_function(1, 3, 5, mul))

if __name__=='__main__':
  main()
