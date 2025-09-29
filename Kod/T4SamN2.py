import random

def roll_dice():
  dice_value = random.randint(1, 6)
  print("Значение кубика:", dice_value)

  if dice_value in [5, 6]:
    print("Вы победили")
  elif dice_value in [3, 4]:
    print("Повторяем бросок...")
    roll_dice()
  else:
    print("Вы проиграли")


if __name__ == "__main__":
  roll_dice()