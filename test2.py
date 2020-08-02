class Human:
    def __init__(self,name,age=22,mileage=0):
        self.name = name
        self.age = age
        self.mileage = mileage
    def saved(self,mileage):
        self.mileage += mileage
        print(f"マイレージ:{mileage}ポイント貯めました。総ポイント:{self.mileage}")
    def used(self,num):
        if not (0<=num<=2):
            print("コースは0~2の範囲で指定してください!")
        if num==0: #沖縄
            if 5000 <= self.mileage:
                self.mileage -= 5000
                print(f"福岡 ‐ 沖縄間の航空券を取得しました。 現在のマイレージ:{self.mileage}")
            else:
                print(f"福岡 ‐ 沖縄間の航空券を取得することができません。 現在のマイレージ:{self.mileage}")
        if num==1: #大阪
            if 10000 <= self.mileage:
                self.mileage -= 10000
                print(f"福岡 ‐ 大阪間の航空券を取得しました。 現在のマイレージ:{self.mileage}")
            else:
                print(f"福岡 ‐ 大阪間の航空券を取得することができません。 現在のマイレージ:{self.mileage}")
        if num==2: #東京
            if 20000 <= self.mileage:
                self.mileage -= 20000
                print(f"福岡 ‐ 東京間の航空券を取得しました。 現在のマイレージ:{self.mileage}")
            else:
                print(f"福岡 ‐ 東京間の航空券を取得することができません。 現在のマイレージ:{self.mileage}")

sakai = Human("酒井")
sakai.saved(12000)
sakai.used(2)
sakai.used(1)
sakai.used(4)
sakai.saved(5500)
sakai.used(0)