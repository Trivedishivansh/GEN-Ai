seat_info = input("Enter your preferseat(Ac/luxery/sleeper/genral) :").lower()

match seat_info:
  case "Ac":
    print("Ac-Air conditional")

  case "luxery":
    print('luxeru-seats with free meals')
  case "sleeper":
    print("sleepr-without air condition seats for sleper")

  case "genral":
    print('genral-no reservation is require')

  case _:
    print("invalid seats")
