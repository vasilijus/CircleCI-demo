from main import Add

def TestAdd():
  assert Add(3,6) == 9, "Assert Failed, number doesnt match"
  print("Assert Add Pass")

if __name__ == '__main__':
  TestAdd()