import time


def products(mood):
    recommendations = {
        "Mutlu": {"Kola": "35", "Şekersiz Kola": "35", "Gazoz": "35", "Tatlı Bisküvi": "25",
                  "Çikolatalı Bisküvi": "25"},
        "Üzgün": {"Sıcak Çikolata": "30", "Çikolatalı Bisküvi": "35", "Çay": "20", "Tatlı Bisküvi": "25",
                  "Çikolata": "25"},
        "Stresli": {"Bitki Çayı": "25", "Tuzlu Bisküvi": "35", "Hafif Gazlı İçecek": "35"},
        "Yorgun": {"Kahve": "35", "Enerji İçeceği": "45", "Protein Bar": "45"},
        "Odaklanmaya İhtiyaç": {"Su": "15", "Fındık, Ceviz Karışımı": "50", "Yeşil Çay": "25"},
        "Rahatsız": {"Soda": "30", "Meyve Suyu": "35", "Hafif Krakerler": "30"}
    }

    return recommendations.get(mood, None)


def ask_questions():
    questions = [
        ("Nasıl bir gün temposu içerisindesiniz?",
         ["Mutlu ve enerjik", "Üzgün, moralsiz", "Stresli ve kaygılı", "Yorucu", "Odaklanma gerektiren",
          "Rahatsız, huzursuz"]),
        ("Günün geri kalanında en çok neye ihtiyacınız var?",
         ["Halimden memnunum", "Morale ihtiyacım var", "Zihnimi boşaltmaya ihtiyacım var", "Enerjiye ihtiyacım var",
          "Odaklanmam lazım", "Rahatlamaya ihtiyacım var"]),
        ("Bugün ne kadar streslisiniz?", ["Hiç stresli değilim", "Biraz stresliyim", "Çok stresliyim"]),
        ("Son zamanlarda günlük zorluklarla başa çıkma yeteneğiniz ne kadar yüksek?",
         ["Bu açıdan iyi durumdayım", "Çok düşük", "Güçlü ama stresliyim", "Yorucu olmaya başladı",
          "Dikkatimi toplamakta zorlanıyorum", "Zorluklar beni huzursuz ediyor"]),
        ("Günün kalanı için nasıl bir aktivite planı içerisindesiniz?",
         ["Eğlence, keyifli zaman", "Bir şey yapacak moralim yok", "Yemek yiyeceğim", "Sportif aktivite",
          "yoğun stresli iş, ders çalışma", "Dinleneceğim"])
    ]

    mood_scores = {
        "Mutlu": 0,
        "Üzgün": 0,
        "Stresli": 0,
        "Yorgun": 0,
        "Odaklanmaya İhtiyaç": 0,
        "Rahatsız": 0
    }

    for question, answers in questions:
        print(question)
        for idx, answer in enumerate(answers, 1):
            print(f"{idx}. {answer}")
        choice = int(input("Seçiminizi belirtiniz: "))

        if question == "Nasıl bir gün temposu içerisindesiniz?":
            if choice == 1:
                mood_scores["Mutlu"] += 2
            elif choice == 2:
                mood_scores["Üzgün"] += 2
            elif choice == 3:
                mood_scores["Stresli"] += 2
            elif choice == 4:
                mood_scores["Yorgun"] += 2
            elif choice == 5:
                mood_scores["Odaklanmaya İhtiyaç"] += 2
            elif choice == 6:
                mood_scores["Rahatsız"] += 2

        if question == "Günün geri kalanında en çok neye ihtiyacınız var?":
            if choice == 1:
                mood_scores["Mutlu"] += 2
            elif choice == 2:
                mood_scores["Üzgün"] += 2
            elif choice == 3:
                mood_scores["Stresli"] += 2
            elif choice == 4:
                mood_scores["Yorgun"] += 2
            elif choice == 5:
                mood_scores["Odaklanmaya İhtiyaç"] += 2
            elif choice == 6:
                mood_scores["Rahatsız"] += 2
        if question == "Bugün ne kadar streslisiniz?":
            if choice == 1:
                mood_scores["Mutlu"] += 1
            elif choice == 2:
                mood_scores["Stresli"] += 1
            elif choice == 3:
                mood_scores["Stresli"] += 2

        if question == "Son zamanlarda günlük zorluklarla başa çıkma yeteneğiniz ne kadar yüksek?":
            if choice == 1:
                mood_scores["Mutlu"] += 2
            elif choice == 2:
                mood_scores["Üzgün"] += 2
            elif choice == 3:
                mood_scores["Stresli"] += 2
            elif choice == 4:
                mood_scores["Yorgun"] += 2
            elif choice == 5:
                mood_scores["Odaklanmaya İhtiyaç"] += 2
            elif choice == 6:
                mood_scores["Rahatsız"] += 2
        if question == "Günün kalanı için nasıl bir aktivite planı içerisindesiniz?":
            if choice == 1:
                mood_scores["Mutlu"] += 2
            elif choice == 2:
                mood_scores["Üzgün"] += 2
            elif choice == 3:
                mood_scores["Stresli"] += 2
            elif choice == 4:
                mood_scores["Yorgun"] += 2
            elif choice == 5:
                mood_scores["Odaklanmaya İhtiyaç"] += 2
            elif choice == 6:
                mood_scores["Rahatsız"] += 2
    max_mood = max(mood_scores, key=mood_scores.get)
    return max_mood


print("Merhaba, ben Helix. Ben, sizin ruh halinize uygun ürünler seçmek için tasarlanmış bir yapay zekayım.")
time.sleep(1)

user_mood = ask_questions()

if user_mood:
    suggestions = products(user_mood)
    if suggestions:
        #print(f"\nRuh haliniz: {user_mood}")
        print("\nÖnerilen içecek ve atıştırmalıklar:")
        for i, (product, price) in enumerate(suggestions.items(), 1):
            print(f"{i}. {product}: {price} TL")

        user_choice = input("Seçiminizi yapınız: ")
        chosen_product = list(suggestions.items())[int(user_choice) - 1]
        print(f"\nSeçiminiz: {chosen_product[0]} - Borcunuz: {chosen_product[1]} TL")

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
