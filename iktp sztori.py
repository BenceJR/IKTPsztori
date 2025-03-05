def kezd():
    print("Egyszer volt, hol nem volt, egy kis falu szélén egy hatalmas erdő volt.")
    print("Egy napon egy fiatal kalandor úgy döntött, hogy felfedezi az erdőt.")
    print("Mit szeretnél tenni?")
    print("1. Belépni az erdőbe.")
    print("2. Visszafordulni és hazamenni.")
    valasztas = input("Válassz egy lehetőséget (1 vagy 2): ")
    
    if valasztas == "1":
        erdo()
    elif valasztas == "2":
        print("Visszafordultál és biztonságosan hazamentél. A kalandod itt véget ért.")
    else:
        print("Érvénytelen választás. Kérlek válassz 1-et vagy 2-t.")
        kezd()

def erdo():
    print("Beléptél az erdőbe, és a fák sűrűjében eltévedtél.")
    print("Hirtelen két út áll előtted.")
    print("Mit szeretnél tenni?")
    print("1. A bal oldali úton folytatni.")
    print("2. A jobb oldali úton folytatni.")
    valasztas = input("Válassz egy lehetőséget (1 vagy 2): ")
    
    if valasztas == "1":
        bal_ut()
    elif valasztas == "2":
        jobb_ut()
    else:
        print("Érvénytelen választás. Kérlek válassz 1-et vagy 2-t.")
        erdo()

def bal_ut():
    print("A bal oldali úton haladva egy titkos barlangra bukkantál.")
    print("Az ajtó zárva van, de egy titkos kulcsot találtál az út mentén.")
    print("Mit szeretnél tenni?")
    print("1. Bemész a barlangba.")
    print("2. Megpróbálod kinyitni a barlangot a kulccsal.")
    print("3. Tovább mész az úton.")
    valasztas = input("Válassz egy lehetőséget (1, 2 vagy 3): ")
    
    if valasztas == "1":
        print("A barlang sötét és titokzatos, de egy kincsre bukkansz. Életed legnagyobb felfedezése lett!")
        tovabbi_kaland()
    elif valasztas == "2":
        print("A kulcs illeszkedik, és a barlang kinyílik. Odabent egy ősi kincs vár rád!")
        tovabbi_kaland()
    elif valasztas == "3":
        print("Újabb titokzatos dolgokat találtál az erdő mélyén, de a kalandod véget ért.")
    else:
        print("Érvénytelen választás. Kérlek válassz 1-et, 2-t vagy 3-t.")
        bal_ut()

def jobb_ut():
    print("A jobb oldali úton egy régi hidat találtál.")
    print("A híd alatt egy folyó csobog, és a híd régi és instabilnak tűnik.")
    print("Mit szeretnél tenni?")
    print("1. Át akarsz kelni a hídon.")
    print("2. Körülnézel és visszafordulsz.")
    print("3. Megpróbálod megjavítani a hidat.")
    valasztas = input("Válassz egy lehetőséget (1, 2 vagy 3): ")
    
    if valasztas == "1":
        print("A híd alatt veszélyes folyó csobog, de sikerül átjutnod! Előtted egy új világ tárul fel.")
        tovabbi_kaland()
    elif valasztas == "2":
        print("Visszafordultál, de a híd titkait sosem fogod megtudni.")
    elif valasztas == "3":
        print("A híd javítása hosszú időt vesz igénybe, de végül sikerül. A híd stabil lesz, és át tudsz kelni.")
        tovabbi_kaland()
    else:
        print("Érvénytelen választás. Kérlek válassz 1-et, 2-t vagy 3-t.")
        jobb_ut()

def tovabbi_kaland():
    print("Miközben folytatod a kalandodat, egy rejtélyes erdő mélyén egy titkos szigetet találsz.")
    print("Egy titokzatos alak lép eléd, aki úgy tűnik, hogy segíthet a további úton.")
    print("Mit szeretnél tenni?")
    print("1. Beszélsz a titokzatos alakkal.")
    print("2. Megpróbálsz elbújni és elkerülni őt.")
    valasztas = input("Válassz egy lehetőséget (1 vagy 2): ")

    if valasztas == "1":
        print("A titokzatos alak egy bölcs varázsló, aki segít neked egy erős varázsigével. Ezáltal sokkal erősebb lettél!")
        uj_utas()
    elif valasztas == "2":
        print("Bár elrejtőztél, a varázsló észrevett és elmondja neked a legnagyobb titkait az erdőben.")
        uj_utas()
    else:
        print("Érvénytelen választás. Kérlek válassz 1-et vagy 2-t.")
        tovabbi_kaland()

def uj_utas():
    print("Miután megkaptad a varázsló segítségét, új lehetőségek nyílnak meg előtted.")
    print("A varázsló egy térképet ad, amely az erdő legmélyebb titkait rejti.")
    print("Mit szeretnél tenni?")
    print("1. Követed a térképen jelölt utat.")
    print("2. Megpróbálsz visszatérni a faluba a varázsló segítsége nélkül.")
    valasztas = input("Válassz egy lehetőséget (1 vagy 2): ")

    if valasztas == "1":
        print("A térkép segítségével egy elrejtett városra találsz, ahol varázslatos lények élnek!")
        boldog_vege()
    elif valasztas == "2":
        print("Visszatérsz a faluba, de sosem felejted el az erdő titkait. A kalandod véget ér.")
    else:
        print("Érvénytelen választás. Kérlek válassz 1-et vagy 2-t.")
        uj_utas()

def boldog_vege():
    print("A varázslatos városban egy különleges varázslatot tanulsz, ami örökre megváltoztatja az életed.")
    print("Egy új világba léptél, és a kalandod sosem ér véget. A történet boldogan zárul.")

kezd()
