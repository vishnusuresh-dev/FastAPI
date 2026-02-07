from typing import Any

def custom_sign(sign: str) -> Any:
  def sign_logic(func):
    def wrapper():
      print(sign * 10)
      func()
      print(sign * 10)
    return wrapper
  return sign_logic


@custom_sign("*")
def print_log():
  print("decorated")

print_log()