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

def list_all_warehouse(voce):

    for index in voce:
        print index.vrsta, index.kol

def save_data(voce):

    f = open("skladiste.txt", "w")

    for i in voce:
        f.write("%s: %s\n" % (i.vrsta, i.kol))

    f.write("------------------")
    f.close()


if __name__ == "__main__":
    print "welcome to warehouse manager program!\n"

    f = open("skladiste.txt", "r")

    voce = []

    for line in f:
        try:
            vrsta, kol = line.split(": ")
            create_voce_object(vrsta, kol, voce)
        except ValueError:
            continue


    if voce == []:
        add_new_voce("jabuke", 0, voce)
        add_new_voce("kruske", 0, voce)

    while True:
        print ""
        akcija = raw_input("> Ako ste kupili novo voce odaberite 1, a ako ste prodali voce odaberite 2 -> ")
        vrsta = raw_input("> Koje voce ste kupili/prodali? -> ")
        kol = int(raw_input("> Koliko voca ste kupili/prodali? -> "))


        if akcija == "1" and vrsta.lower() == "jabuke":
            selected = voce[0]
            selected.add_kol(kol)
            list_all_warehouse(voce)

        elif akcija == "1" and vrsta.lower() == "kruske":
            selected = voce[1]
            selected.add_kol(kol)
            list_all_warehouse(voce)

        elif akcija == "2" and vrsta.lower() == "jabuke":
            selected = voce[0]
            selected.less_kol(kol)
            list_all_warehouse(voce)

        elif akcija == "2" and vrsta.lower() == "kruske":
            selected = voce[1]
            selected.less_kol(kol)
            list_all_warehouse(voce)

        else:
            print "Niste unjeli odgovarajuce parametre!\n"

        want_more = raw_input("> Novi unos? [da/ne] -> ")

        if want_more == "ne":
            save_data(voce)
            break