class warehouse(object):

    def __init__(self, vrsta, kol):
        self.vrsta = vrsta
        self.kol = kol

    def __str__(self):
        return self.vrsta + " " + self.kol

    def add_kol(self,new_kol):
        self.kol += new_kol

    def less_kol(self,new_kol):
        if self.kol < new_kol:
            print "Unjeli ste krivu kolicinu!"
        else:
            self.kol -= new_kol



def add_new_voce(vrsta,kol,voce):

    result = create_voce_object(vrsta, kol, voce)

def create_voce_object(vrsta, kol, voce):
    try:
        voce_kol = int(kol)

        new_voce = warehouse(vrsta,voce_kol)
        voce.append(new_voce)

        return True

    except ValueError:
        return False

def list_all_warehouse(voce, iteracija):

    iteracija += 1
    print ("Stanje skladista %s.\n" % (iteracija))

    for index in voce:
        print index.vrsta, index.kol

    save_data(voce, iteracija)
    return iteracija

def save_data(voce, iteracija):

    f = open("skladiste_v2.txt", "a")
    f.write("Stanje skladista: %s\n" % (iteracija))

    for i in voce:
        f.write("%s: %s\n" % (i.vrsta, i.kol))

    f.write("------------------\n")
    f.close()


if __name__ == "__main__":
    print "welcome to warehouse manager program!\n"

    f = open("skladiste_v2.txt", "r")

    voce = []
    it = 0
    kol_jabuke = 0
    kol_kruske = 0

    for line in f:

        if line.find("Stanje") != -1:
            w1,it = line.split(": ")
        elif line.find("jabuke") != -1:
            vrsta, kol_jabuke = line.split(": ")
        elif line.find("kruske") != -1:
            vrsta, kol_kruske = line.split(": ")



    iteracija = int(it)

    add_new_voce("jabuke", kol_jabuke, voce)
    add_new_voce("kruske", kol_kruske, voce)


    while True:
        print ""
        akcija = raw_input("> Ako ste kupili novo voce odaberite 1, a ako ste prodali voce odaberite 2 -> ")
        vrsta = raw_input("> Koje voce ste kupili/prodali? -> ")
        kol = int(raw_input("> Koliko voca ste kupili/prodali? -> "))


        if akcija == "1" and vrsta.lower() == "jabuke":
            selected = voce[0]
            selected.add_kol(kol)
            iteracija = list_all_warehouse(voce, iteracija)

        elif akcija == "1" and vrsta.lower() == "kruske":
            selected = voce[1]
            selected.add_kol(kol)
            iteracija = list_all_warehouse(voce, iteracija)

        elif akcija == "2" and vrsta.lower() == "jabuke":
            selected = voce[0]
            selected.less_kol(kol)
            iteracija = list_all_warehouse(voce, iteracija)

        elif akcija == "2" and vrsta.lower() == "kruske":
            selected = voce[1]
            selected.less_kol(kol)
            iteracija = list_all_warehouse(voce, iteracija)

        else:
            print "Niste unjeli odgovarajuce parametre!\n"

        want_more = raw_input("> Novi unos? [da/ne] -> ")

        if want_more == "ne":
   #         save_data(voce)
            break