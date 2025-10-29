def figure_a(size):
    for i in range(size):
        for j in range(size):
            if i <= j:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_b(size):
    for i in range(size):
        for j in range(size):
            if i + j >= size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_v(size):
    for i in range(size):
        for j in range(size):
            if i <= j and i + j <= size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_g(size):
    for i in range(size):
        for j in range(size):
            if i >= j and i + j >= size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_d(size):
    for i in range(size):
        for j in range(size):
            if (i <= j and i + j <= size - 1) or (i >= j and i + j >= size - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_e(size):
    for i in range(size):
        for j in range(size):
            if (i <= j and i + j >= size - 1) or (i >= j and i + j <= size - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_j(size):
    for i in range(size):
        for j in range(size):
            if i + j >= size - 1 and i >= j:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_z(size):
    for i in range(size):
        for j in range(size):
            if i <= j and i + j <= size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_i(size):
      for i in range(size):
          for j in range(size):
              if i + j <= size - 1:
                  print("*", end="")
              else:
                  print(" ", end="")
          print()


def figure_k(size):
      for i in range(size):
          for j in range(size):
              if i >= j:
                  print("*", end="")
              else:
                  print(" ", end="")
          print()

size = 5
print("Фигура А:")
figure_a(size)
print("\nФигура Б:")
figure_b(size)
print("\nФигура В:")
figure_v(size)
print("\nФигура Г:")
figure_g(size)
print("\nФигура Д:")
figure_d(size)
print("\nФигура Е:")
figure_e(size)
print("\nФигура Ж:")
figure_j(size)
print("\nФигура З:")
figure_z(size)
print("\nФигура И:")
figure_i(size)
print("\nФигура К:")
figure_k(size)

input("")

