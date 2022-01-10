import random as random

for i in range(100):
            print("\n")
print("Aleksa Vukićević 2022")

wordlist = ["alat","bodlja","devet","dva","previše","štand","šeroa","ašov","avala","autobus","automobil","azija","afrika","anonimno"
,"azbuka","bukvar","buba","bandit","biblija","biljka","broš","božić","berba","britva","boca","borba","bič","banana","vuk","vožnja"
,"vila","vampir","vaza","voz","vakum","vulkan","vino","grb","gradovi","gora","gradnja","gimnastika","gubitak","gomila","gruzija"
,"đurđevak","đurđevdan","đak","ekipa","energija","ekonomija","ekologija","enciklopedija","žuto","žalba","žbunje","žargon"
,"dobitak","drama","dnevnica","diskusija","dabrota","dubina","daljina","divizija","duga","znak","zubar","zvanično","zbunjeno"
,"igra","igla","indigo","izmišljotina","imovina","investicija","imenjak","izgovor","jabuka","jablan","jeftino","jednako","skupo"
,"jednostavno","jogurt","jezik","krava","korona","kina","kokoška","klik","kanta","lopta","ljubav","lov","lignja","lepota"
,"ljuljaška","ljigavac","mačka","miš","montaža","ministarstvo","mišljenje","miris","magija","munja","noga","nož","nebo","nikada"
,"njuška","organ","orgulje","ovca","prozor","pristup","pismo","pesma","pijanstvo","puška","pištolj","pingvin","praznik","ponovo"
,"riba","realizacija","reka","romb","stiker","slika","snimak","strela","svetlost","smeh","tema","trka","takmičenje","traka"
,"torba","trigonometrija","tajna","ukras","ugao","uvreda","film","folija","firma","fen","fenjer","funkcija","formula","hram"
,"himna","honda","hrana","havaji","hvala","crkva","civil","cura","devojka","cilj","čizma","čarobnjak","čvor","čigra","džem"
,"džin","štap","škola","štuka","šljiva","šolja","šaka"]

word = wordlist[random.randint(0, len(wordlist))]
guessed = ""
missed = ""
err = 0

while err <= 6:

    print("\n")
    wordguess = ""
    numofletters = 0
    for i in range(len(word)):
        if(word[i] in guessed):
            wordguess += word[i] + " "
            numofletters +=1
        else:
            wordguess += "  "
    print(wordguess)

    lines = ""
    for i in range(len(word)):
        lines += "‾ "
    print (lines) 
    print("                       X: " + missed)

    def hangman(errors):
        def head():
            if errors > 0:
                return "O"
            else:
                return " "
        def body():
            if errors > 1:
                return "|"
            else:
                return " "
        def armr():
            if errors > 2:
                return "\\"
            else:
                return " "
        def arml():
            if errors > 3:
                return "/"
            else:
                return " "
        def legr():
            if errors > 4:
                return "\\"
            else:
                return " "
        def legl():
            if errors > 5:
                return "/"
            else:
                return " "
        print(f" _______\n |     |\n {head()}     |\n{arml()}{body()}{armr()}    |\n{legl()} {legr()}    |\n       |\n      ‾‾‾‾")
    hangman(err)

    if err >= 6:
        print("Izgubili ste :(")
        print("Reč je "+ word)
        exit()
    elif numofletters == len(word):
        print("Pobedili ste! :)")
        exit()
    else:
        inp = input("Pogodi slovo: ")
        if inp in word:
            guessed += inp
        elif inp not in missed:
            missed += inp
            err += 1

        for i in range(100):
            print("\n")




