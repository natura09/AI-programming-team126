#お試し
def menu():
  functions = ["乗車駅選択","チャージ機能"]
  print("【ウチダ電鉄交通系ICカード検証システム】")
  for i in range(len(functions)):
    print(f"{i + 1}：{functions[i]}")
  print("使用する機能を入力してください（終了する場合には99を入力）")
  return int(input(""))

def select_station():
  stations = ["秋葉原","山梨","長野"]
  fares = [133,4128,7990]
  print("【乗車駅選択】")
  for i in range(len(stations)):
    print(f"{i + 1}:{stations[i]}:{fares[i]}円")
  print("乗車した駅を入力してください（キャンセルする場合には99を入力）")
  destination = int(input(""))
  if destination == 99:
    print("駅の選択をキャンセルしました")
    return 0
  print(f"乗車駅は{stations[destination - 1]}で料金は{fares[destination - 1]}円です")
  return fares[destination - 1]

def pay(balance,fare):
  print(f"チャージ残高は{balance}円です")
  if balance < fare:
    print("残高不足です")
    while balance < fare:
      balance += 3000
      print("3000円を自動チャージします")
  balance -= fare
  print(f"精算後のチャージ残高は{balance}円です")
  if balance < 500:
    balance += 3000
    print("残高が500円未満のため3000円自動チャージします")
    print(f"チャージ残高は{balance}円です")
  return balance

def charge(balance):
  charges = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
  print("【チャージ機能】")
  print(f"チャージ残高は{balance}円です")
  for i in range(len(charges)):
    print(f"{i + 1}:{charges[i]}円")
  print("チャージする金額を入力してください（キャンセルする場合には99を入力）")
  charge = int(input(""))
  if 1 <= charge <= 10:
      print(f"{charges[charge - 1]}円をチャージします")
      balance += charges[charge - 1]
  elif charge == 99:
      print("チャージをキャンセルしました")
  print(f"チャージ残高は{balance}円です")
  return balance
    
def main():
  balance = 500
  while True:
    choice = menu()
    if choice == 1:
      fare = select_station()
      if fare != 0:
        balance = pay(balance,fare)
    elif choice == 2:
      balance  = charge(balance)
    elif choice == 99:
      print("システムを終了します")
      break

if __name__ == "__main__":
  main()
        
