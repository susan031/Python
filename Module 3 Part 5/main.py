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
print("Фигура а:")
figure_a(size)
print("\nФигура b:")
figure_b(size)
print("\nФигура v:")
figure_v(size)
print("\nФигура g:")
figure_g(size)
print("\nФигура d:")
figure_d(size)
print("\nФигура e:")
figure_e(size)
print("\nФигура ж:")
figure_j(size)
print("\nФигура з:")
figure_z(size)
print("\nФигура и:")
figure_i(size)
print("\nФигура k:")
figure_k(size)

input("")
