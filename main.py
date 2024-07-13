import time
def products(mood):
    recommendations = {
        "Mutlu": {"kola": "35", "şekersiz kola": "35", "Gazoz": "35", "Tatlı Bisküvi": "25",
                  "çikolatalı Bisküvi": "25"},
        "üzgün": {"Sıcak çikolata": "30", "Çikolatalı Bisküvi": "35", "Çay": "20", "Tatlı Bisküvi": "25",
                  "çikolata": "25"},
        "Stresli": {"Bitki çayı": "25", "Tuzlu bisküvi": "35", "Hafif gazlı içecek": "35"},
        "Yorgun": {"Kahve": "35", "Enerji içeceği": "45", "Protein bar": "45"},
        'Odaklanmaya ihtiyaç': {"Su": "15", "Fındık,ceviz karışımı": "50", "Yeşil çay": "25"},
        'Rahatsız': {"Soda": "30", "Meyve suyu": "35", "Hafif krakerler": "30"}
    }

    if mood in recommendations:
        return recommendations[mood]
    else:
        return None


def questions():
    happy = 0
    sad = 0
    stressed = 0
    tired = 0
    need_focus = 0
    uncomfortable = 0
    wrong = 0
    print("Merhaba, ben Helix. Ben, sizin ruh halinize uygun ürünler seçmek için tasarlanmış bir yapay zekayım.")
    time.sleep(1)

    while happy < 3 and sad < 3 and stressed < 3 and tired < 3 and need_focus < 3 and uncomfortable < 3:

        first_quest = input(
            f"Nasıl bir gün temposu içerisindesiniz?:  \n1- Mutlu ve enerjik  \n2- Üzgün, moralsiz \n3- Stresli ve kaygılı \n4- Yorucu, \n5- Odaklanma gerektiren \n6- Rahatsız, huzursuz \nSeçiminizi belirtiniz: ")

        if first_quest.isdigit and 0 < int(first_quest) < 7:
            first_quest = int(first_quest)
            if first_quest == 1:
                happy += 1
            elif first_quest == 2:
                sad += 1
            elif first_quest == 3:
                stressed += 1
            elif first_quest == 4:
                tired += 1
            elif first_quest == 5:
                need_focus += 1
            elif first_quest == 6:
                uncomfortable += 1
            else:
                print("Geçersiz değer girdiniz.")
        else:
            wrong += 1
            print(f"wrong : {wrong}")
            print("Lütfen Geçerli bir sayı giriniz .")
            if wrong == 3:
                print("3 kez hatalı tuşlama yaptınız. Çıkış yapılıyor.")
                break
        time.sleep(1)
        print(
            f"Mutlu: {happy}, Üzgün: {sad}, Stresli: {stressed}, Yorucu: {tired}, Odaklanma: {need_focus}, Rahatsız: {uncomfortable}")
        second_quest = input("Günün geri kalanında en çok neye ihtiyacınız var? \n1- Halimden memnunum \n2- Morale ihtiyacım var \n3- Zihnimi boşaltmaya ihtiyacım var "
                             "\n4- Enerjiye ihtiyacım var"
                             "\n5- Odaklanmam lazım \n6- Rahatlamaya ihtiyacım var"
                             "\nSeçiminizi belirtiniz: " )

        if second_quest.isdigit and 0 < int(second_quest) < 7:
            second_quest = int(second_quest)
            if second_quest == 1:
                happy += 1
            elif second_quest == 2:
                sad += 1
            elif second_quest == 3:
                stressed += 1
            elif second_quest == 4:
                tired += 1
            elif second_quest == 5:
                need_focus += 1
            elif second_quest == 6:
                uncomfortable += 1
            else:
                print("Geçersiz değer girdiniz.")
        else:
            wrong += 1
            print(f"wrong : {wrong}")
            print("Lütfen Geçerli bir sayı giriniz .")
            if wrong == 3:
                print("3 kez hatalı tuşlama yaptınız. Çıkış yapılıyor.")
                break
        print(
            f"Mutlu: {happy}, Üzgün: {sad}, Stresli: {stressed}, Yorucu: {tired}, Odaklanma: {need_focus}, Rahatsız: {uncomfortable}")


questions()

user_mood = input("Ruh halinizi girin (Mutlu, Üzgün, Stresli, Yorgun, Odaklanmaya ihtiyaç, Rahatsız): ")
suggestions = products(user_mood)

if suggestions:
    num = 1
    print("Önerilen içecek ve atıştırmalıklar:")
    for product, price in suggestions.items():
        print(f"-{num} {product}: {price} TL")
        num += 1

    user_choose = input("Seçiminizi yapınız: ")
    chosen_product = list(suggestions.items())[int(user_choose) - 1]
    print(f"\nSeçiminiz {chosen_product[0]} - Borcunuz: {chosen_product[1]} TL")

    pay = int(input("Ödeme yapınız: "))
    remaining_payment = int(chosen_product[1]) - pay

    while remaining_payment > 0:
        print(f"Eksik ödeme yaptınız \nEksik tutar = {remaining_payment} TL")
        pay_second = int(input("Kalan ödemeyi yapınız: "))
        remaining_payment -= pay_second

    if remaining_payment < 0:
        print(f"Ödeme alınmıştır. Para üstünüz = {-remaining_payment} TL. Afiyet olsun.")
    else:
        print("Ödeme alınmıştır, Afiyet olsun.")
else:
    print("Geçerli bir ruh hali girin.")
