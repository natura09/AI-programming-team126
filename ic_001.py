def menu():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


def select_station():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


def pay(untin,zandaka : int):
  
  print(f"チャージ残高は{zandaka}円です。")

  if zandaka < untin:
    print("残高が不足しています。")

    while zandaka < untin:
      print("3000円自動チャージします")
      zandaka += 3000

  elif zandaka >= untin + 500: 
    zandaka = zandaka - untin 
    print(f"精算後のチャージ残高は{zandaka}円です。")

  else:
    print("残高が500 円未満のため3000 円自動チャージします。")
    zandaka = zandaka - untin + 3000

  print(f"チャージ残高は{zandaka}円です。")
  
  return zandaka
 
  # pass #このpassは処理を書いた後消してよい。


def charge():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


def main():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


if __name__ == "__main__":
    main()
