def charge(balance):
  charges = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
  print("【チャージ機能】")
  print(f"チャージ残高は{balance}円です")
  for i in range(len(charges)):
    print(f"{i + 1}:{charges[i]}円")
  print("チャージする金額を入力してください（キャンセルする場合には99を入力）")

  try:
    charge = int(input(""))
  except ValueError:
    print("整数以外が入力されました。")
  
  else:
    if 1 <= charge <= 10:
      print(f"{charges[charge - 1]}円をチャージします")
      balance += charges[charge - 1]
    if charge == 99:
      print("チャージをキャンセルしました")
    else:
      print("1~10または99の数値を入力してください")
  print(f"チャージ残高は{balance}円です")
  return balance