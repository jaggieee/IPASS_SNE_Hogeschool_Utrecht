# modules die standaard in python zitten
import pip                                                                                                              # Module om packages te installeren
import os                                                                                                               # Module om terminal te clearen
import re                                                                                                               # Module om met regex te kunnen filteren
import argparse                                                                                                         # Module om CLI flags toe te staan
import sys                                                                                                              # Module om script af te sluiten
import importlib.util                                                                                                   # Module om te controleren of module geinstalleerd is
from configparser import ConfigParser, NoOptionError, NoSectionError                                                    # Module voor config file en fout afhandeling van config file
from collections import Counter                                                                                         # Module om items in een list te tellen
import datetime                                                                                                         # Module om huidige tijd te bepalen voor schrijven naar resultaatfile
import platform                                                                                                         # Module om platform te bepalen

# functie om niet standaard module te installeren
def ImportOptionalPackage():
    pakket = 'prettytable'                                                                                              # module naam

    spec = importlib.util.find_spec(pakket)                                                                             # varibale om te controleren of pakket geinstalleerd is
    while True:                                                                                                         # infinate while loop
        if spec is None:                                                                                                # als module naam niet voorkomt in spec dan...
            print(pakket +" is niet geinstalleerd")                                                                     # print output aan gebruiker
            vraag = input('wil je ' + pakket + ' proberen te installeren? Y/N ')                                        # vraag of gebruiker missende module wilt installeren
            if vraag.upper() == 'Y':                                                                                    # als Y dan...
                    pip.main(['install', 'prettytable'])                                                                # installeer prettytable via pip
                    break                                                                                               # break uit infinate while loop
            elif vraag.upper() == "N":                                                                                  # en als antwoord N is...
                os.system('cls' if os.name == 'nt' else 'clear')
                print('applicatie kan niet gestart worden zonder ' + pakket)                                            # print output naar gebruiker
                input('druk op enter om af te sluiten...')
                os.system('cls' if os.name == 'nt' else 'clear')                                                        # clear terminal
                sys.exit(0)                                                                                             # sluit applicatie
            else:                                                                                                       # anders...
                print('maak alstublieft een geldige keus ')                                                             # print output aan gebruiker
        else:                                                                                                           # als module wel voorkomt in spec dan...
            break                                                                                                       # break uit infinate while loop.

                                                                                                                        # Probeer niet standaard python module die gebruikt wordt te installeren
ImportOptionalPackage()

#modules die niet standaard in Python zitten
try:                                                                                                                    # try en except op Python exception te voorkomen wanneer module niet geimporteerd kan worden
    from prettytable import PrettyTable                                                                                 # Module om resultaattabellen aan te maken
except ModuleNotFoundError:
    os.system('cls' if os.name == 'nt' else 'clear')                                                                    # leegmaken terminal
    print('Module prettytable kan niet geimporteerd worden. \n'                                                         # print informatie voor gebruiker wanneer module niet geinstalleerd kan worden
          'Controleer uw internetverbinding of installeer prettytable handmatig')
    input('druk op enter om af te sluiten...')
    os.system('cls' if os.name == 'nt' else 'clear')                                                                    # leegmaken terminal
    sys.exit(0)                                                                                                         # sluit applicatie af aangezien applicatie niet werkt zonder prettytable module.




# Functie om Menu te weergeven #
def ToonMenu():
                                                                                                                        # De functies vragen om input om door te gaan, hiermee ga ik er vanuit dat de gebruiker de output van de functie gelezen en niet meer nodig hebben.
                                                                                                                        # Daarom wordt de terminal leeg gemaakt bij het aanroepen van het menu
    clear()
    menu = PrettyTable(['Keuze nummer',
                        'Omschrijving keuze'])                                                                          # Menu structuur aangemaakt in tabelvorm doormiddel van module "PrettyTable"
    menu.add_row(['1', 'Toon bestanden die niet gevonden konden worden'])
    menu.add_row(['2', 'Toon top 10 van meest gedownloade bestanden'])
    menu.add_row(['3', 'Toon lijst van verschillende clients die geconnect hebben'])
    menu.add_row(['4', 'Sluit de applicatie'])
    print(menu)


# Functie om invoer te vragen en invoer te valideren
def KeuzeInvoer():
    while True:                                                                                                         # While loop voor controle geldige invoer
        try:                                                                                                            # try en except om Python exception te voorkomen wanneer de applicatie met control-c wordt afgesloten ipv het menu
            menukeus = str(input("maak uw menu keuze: "))

            if menukeus == "1":                                                                                         # wanneer een geldige optie in het menu gekozen wordt zal de terminal worden leeggemaakt,
                clear()                                                                                                 # de bijbehorende functie uitgevoerd worden in input mode (functie(noinput) = false want de optie is interactief gekozen)
                notfound(False)                                                                                         # en uit de infinite while loop gebroken worden aangezien de invoer correct is.
                break
            elif menukeus == "2":
                clear()
                top10(False)
                break
            elif menukeus == "3":
                clear()
                ConnectedClients(False)
                break
            elif menukeus == "4":
                clear()
                break
            else:
                print("Ongeldige invoer, selecteer alstublieft een geldige menukeuze")
        except KeyboardInterrupt:
            clear()
            sys.exit(0)


# Functie om configuratiebestand uit te lezen en terug te geven
def ConfigFile(section, option):
    Parser = ConfigParser()                                                                                             # variabele om module aan te roepen
    OperatingSystem = platform.system()                                                                                 # haalt huidig OS op voor dash notatie
    scriptpath = (os.path.dirname(os.path.realpath(__file__)))                                                          # haalt huidige path op
    ConfiguratieBestand = ''                                                                                            # lege string voor bestandslocatie
    if OperatingSystem == "Linux" or "Darwin":                                                                          # als OS linux of macOS is dan...
        ConfiguratieBestand = (scriptpath + '/config.ini')                                                              # huidig path met dashlocatie voor linux en mac

    else:                                                                                                               # anders..
        ConfiguratieBestand =(scriptpath + '\config.ini')                                                               # ervanuit gaande dat andere besturingsystemen Windows zijn, dashlocatie voor windows.
                                                                                                                        # variabele om configuratiebestand te definieren
    ConfiguratieReader = Parser.read(ConfiguratieBestand)                                                               # variabele om configuratiebestand in te lezen
    if ConfiguratieBestand not in ConfiguratieReader:                                                                   # Als het configuratiebestand zich niet in de reader bevind kon het configuratiebestand niet gevonden worden, applicatie sluit zichzelf af.
        print(ConfiguratieBestand, "niet gevonden, applicatie wordt afgesloten")
        sys.exit(1)
    try:                                                                                                                # Wanneer het configuratiebestand wel gelezen kan worden, maar opgegeven section of optie niet gevonden kan worden, zal de applicatie worden afgesloten.
        return (Parser.get(section, option))
    except NoOptionError as error:
        print("Optie", option, "niet gevonden in sectie:", str(section), "van", ConfiguratieBestand), error
        sys.exit(1)
    except NoSectionError as error:
        print("Sectie", section, 'niet gevonden in', ConfiguratieBestand), error
        sys.exit(1)


# Functie om bestanden die niet gevonden konden worden te weergeven
def notfound(noinput):
    logfile = ConfigFile('logpath', 'AnalysatieLogfile')                                                                # locatie van logfile
    filenotfound = []                                                                                                   # list met filter resultaten
    zoekterm = "FAIL DOWNLOAD"                                                                                          # zoekterm in log bestand
    TransferRate = "0.00Kbyte/sec"
    try:                                                                                                                # TransferRate als zoekterm te bepalen of bestanden niet gevonden konden worden
        with open(logfile, 'r') as f:                                                                                   # het openen van de logfile in read mode als f

            for lines in f:                                                                                             # iteratie in alle regels van de logfile die geopend is als f
                if zoekterm in lines:                                                                                   # Als de zoekterm "FAIL DOWNLOAD"" duidt op een gefaalde download.
                    if TransferRate in lines:                                                                           # "0.00Kbyte/sec"  en het ontbreken van een file grootte duiden erop dat de file niet bestaat
                        r = re.search(r'".*?".*".*\/(.*)"', lines)                                                      # Regex om enkel de bestandsnamen eruit te filteren
                        MissendeBestanden = (r.group(1))                                                                # Missendebestanden verwijst naar Capturegroep 1 van regex
                        filenotfound.append(MissendeBestanden)                                                          # Bestandsnamen in een list plaatsen

        resultaat = PrettyTable(['Ontbrekend bestand',
                                 'Aantal download pogingen'])                                                           # Tabel voor resultaten doormiddel van de prettytable module
        CountObjects = dict(Counter(filenotfound).most_common())                                                        # Aantal pogingen berekenen met een dict en de counter module en meeste downloads bovenaan zetten.
        for k, v in CountObjects.items():                                                                               # loop om key en value van list te dict
            resultaat.add_row([k, v])                                                                                   # resultaat tabel printen

    except FileNotFoundError:                                                                                           # als logfile niet gevonden kan worden
        print('Kan ' + logfile + ' niet openen')                                                                        # print output aan gebruiker
        input('druk op enter om af te sluiten...')                                                                      # vraag om input om af te sluiten
        clear()                                                                                                         # clear terminal
        sys.exit(0)                                                                                                     # sluit applicatie

    outfile = ConfigFile('logpath', 'Resultaatfile')                                                                    # definieren op welke plaats resultaatfile geschreven wordt
    resultaat_txt = resultaat.get_string()                                                                              # string van resultaattabel verkrijgen om in file te schrijven
    try:                                                                                                                # try en except om python IO errors te voorkomen wanneer outfile niet geschreven kan worden
        with open(outfile, 'a') as file:
            time = datetime.datetime.now()                                                                              # haalt huidige tijd op
            file.write("\n" + time.strftime('%H:%M:%S /%d/%m/%Y') + "\n" + resultaat_txt + "\n")                        # schrijft resultaattabel met huidige tijd naar file
    except IOError:
        print('Kan niet schrijven naar bestand, controleer uw permissies')                                              # print output naar gebruiker

    if cron() == True and noinput == True:                                                                              #als cron() True is en noinput True is dan...(=connected to terminal)
        print(resultaat)                                                                                                #print resultaat
        sys.exit()                                                                                                      #sluit applicatie
    elif cron() == True and noinput == False:                                                                           #of als cron true is en noinput False is dan..(=connected to terminal)
        print(resultaat)                                                                                                #print resultaat
        input('druk op enter om verder te gaan...')                                                                     #vraag input om verder te gaan
        ToonMenu()                                                                                                      # input ontvangen, toon menu
        KeuzeInvoer()                                                                                                   # vraag om keuze
    elif cron() == False and noinput == False:                                                                          #of als cron() False is en noinput false is..
                                                                                                                        #(is niet connected aan terminal maar wel interactief, niet interactieve modus komt altijd in True,
                                                                                                                        #Dus toch weergevn om programma in IDE te laten werken (in IDE cron()==False)
        print(resultaat)                                                                                                #print resultaat
        input('druk op enter om verder te gaan...')
        ToonMenu()
        KeuzeInvoer()
    else:                                                                                                               #anders
        sys.exit(0)                                                                                                     #applicatie sluiten


# Functie om een top 10 te weergeven van de meest gedownloade bestanden
def top10(noinput):
    logfile = ConfigFile('logpath', 'AnalysatieLogfile')                                                                # Locatie logfile
    zoekterm = "OK DOWNLOAD"                                                                                            # zoekterm voor logfile
    bestanden = []                                                                                                      # lijst om bestandsnamen in te plaatsen
    try:
        with open(logfile, 'r') as f:                                                                                   # open logfile in read mode als f:
            for lines in f:                                                                                             # Voor alle regels in f:
                if zoekterm in lines:                                                                                   # als zoekterm in regels zit dan...
                    r = re.search(r'".*?".*".*\/(.*)"', lines)                                                          # regex om filenames uit regels te filteren
                    all = (r.group(1))                                                                                  # all = resultaatgroep 1 van de regex
                    bestanden.append(all)                                                                               # plaats alle gevonden bestanden in lijst

        CountObjects = dict(Counter(bestanden).most_common(10))                                                         # tel hoevaak bestanden voorkomen in de list d.m.v. de Counter module, plaats meest voorkomende bovenaan en weergeef enkel de eerste 10
        resultaat = PrettyTable(['Bestandsnaam', 'Aantal downloads'])                                                   # Resultaattabel d.m.v. de prettytable module
        for k, v in CountObjects.items():                                                                               # for loop om resultaten in resultaattabel te plaatsen
            resultaat.add_row([k, v])

    except FileNotFoundError:                                                                                           # als logfile niet gevonden kan worden
        print('Kan ' + logfile + ' niet openen')                                                                        # print output aan gebruiker
        input('druk op enter om af te sluiten...')                                                                      # wacht op input om af te sluiten
        clear()                                                                                                         # clear terminal
        sys.exit(0)                                                                                                     # sluit applicatie

    outfile = ConfigFile('logpath', 'Resultaatfile')                                                                    # definieren op welke plaats resultaatfile geschreven wordt
    resultaat_txt = resultaat.get_string()                                                                              # string van resultaattabel verkrijgen om in file te schrijven
    try:                                                                                                                # try en except om python IO errors te voorkomen wanneer outfile niet geschreven kan worden
        with open(outfile, 'a') as file:
            time = datetime.datetime.now()                                                                              # haalt huidige tijd op
            file.write("\n" + time.strftime('%H:%M:%S /%d/%m/%Y') + "\n" + resultaat_txt + "\n")                        # schrijft resultaattabel met huidige tijd naar file
    except IOError:
        print('Kan niet schrijven naar bestand, controleer uw permissies')                                              # print output naar gebruiker

    if cron() == True and noinput == True:                                                                              #als cron() True is en noinput True is dan...(=connected to terminal)
        print(resultaat)                                                                                                #print resultaat
        sys.exit()                                                                                                      #sluit applicatie
    elif cron() == True and noinput == False:                                                                           #of als cron true is en noinput False is dan..(=connected to terminal)
        print(resultaat)                                                                                                #print resultaat
        input('druk op enter om verder te gaan...')                                                                     #vraag input om verder te gaan
        ToonMenu()                                                                                                      # input ontvangen, toon menu
        KeuzeInvoer()                                                                                                   # vraag om keuze
    elif cron() == False and noinput == False:                                                                          #of als cron() False is en noinput false is..
                                                                                                                        #(is niet connected aan terminal maar wel interactief, niet interactieve modus komt altijd in True,
                                                                                                                        #Dus toch weergevn om programma in IDE te laten werken (in IDE cron()==False)
        print(resultaat)                                                                                                #print resultaat
        input('druk op enter om verder te gaan...')
        ToonMenu()
        KeuzeInvoer()
    else:                                                                                                               #anders
        sys.exit(0)                                                                                                     #applicatie sluiten

# Functie om lijst te weergeven waarbij wordt weergeven: het aantal connecties, aantal gedownloade bytes per client,
# gebruikte anonymous password
def ConnectedClients(noinput):
    scriptpath = (os.path.dirname(os.path.realpath(__file__)))
    ConfiguratieBestand = (scriptpath + 'config.ini')
    logfile = ConfigFile('logpath', 'AnalysatieLogfile')                                                                # Locatie logfile
    zoekterm = "OK LOGIN:"                                                                                              # zoektermen voor configuratie bestand
    zoekterm2 = "OK DOWNLOAD"

    ipConnections = {}                                                                                                  # Dicts om zoekresultaten in op te slaan
    ipPassword = {}
    ipBytes = {}
    try:
        with open(logfile, 'r') as f:                                                                                   # File openen als f:
            for lines in f:                                                                                             # voor alle regels in F:
                if zoekterm in lines:                                                                                   # als eerste zoekterm in regels zit dan...
                    r = re.search(r'"([^"]*\.[^"]*\.[^"]*\.[^"]*)"', lines)                                             # Regex om IP uit lines die de zoekterm bevatten te filteren
                    a = re.search(r'password ?"([^"]*)"', lines)                                                        # Regex om password uit lindes die zoekterm bevatten te filteren
                    ip = (r.group(1))                                                                                   # ip = resultaatgroep 1 van de regex filter
                    pw = (a.group(1))                                                                                   # pw = resultaatgroep 1 van de regex filter
                    ipConnections[ip] = ipConnections.get(ip, 0) + 1                                                    # Telt hoevaak het IP voorkomt
                    if "anon" in lines:                                                                                 # Als username anon zich in de regels bevind dan...
                        ipPassword[ip] = pw                                                                             # Plaatst password bij bijbehorend ip
                elif zoekterm2 in lines:                                                                                # Als zoekterm 2 in regels dan....
                    r = re.search(r'"([^"]*\.[^"]*\.[^"]*\.[^"]*)"', lines)                                             # Regex om IP uit lines die zoekterm 2 bevatten te filteren
                    b = re.search(r'(\d+) ?bytes', lines)                                                               # Regex om bytes uit lines die zoekterm 2 bevatten te filteren
                    ip = (r.group(1))                                                                                   # ip = resultaatgroep 1 van de regex filter
                    bytes = (b.group(1))                                                                                # bytes = resultaatgroep 1 van de regex filter
                    ipBytes[ip] = ipBytes.get(ip, 0) + int(bytes)                                                       # Telt hoeveel bytes ieder IP gedownload heeft

        resultaat = PrettyTable(['Ip', 'Connections', 'Password', 'Bytes'])                                             # resultaat tabel d.m.v. PrettyTable module
        for k, v in ipConnections.items():                                                                              # voor key en value in dict ipconnections (.items returned een lijst waarin een tuple staat met key en value van de dict_
            resultaat.add_row([k, ipConnections.get(k, k), ipPassword.get(k, ""), ipBytes.get(k, 0)])                   # voegt resultaten aan resultaat tabel toe.

    except FileNotFoundError:                                                                                           # als logfile niet gevonden kan worden
        print('Kan ' + logfile + ' niet openen')                                                                        # print output aan gebruiker
        input('druk op enter om af te sluiten...')                                                                      # vraag input om af te sluiten
        clear()                                                                                                         # clear de terminal
        sys.exit(0)                                                                                                     # sluit applicatie af

    outfile = ConfigFile('logpath', 'Resultaatfile')                                                                    # definieren op welke plaats resultaatfile geschreven wordt
    resultaat_txt = resultaat.get_string()                                                                              # string van resultaattabel verkrijgen om in file te schrijven
    try:                                                                                                                # try en except om python IO errors te voorkomen wanneer outfile niet geschreven kan worden
        with open(outfile, 'a') as file:
            time = datetime.datetime.now()                                                                              # haalt huidige tijd op
            file.write("\n" + time.strftime('%H:%M:%S /%d/%m/%Y') + "\n" + resultaat_txt + "\n")                        # schrijft resultaattabel met huidige tijd naar file
    except IOError:
        print('Kan niet schrijven naar bestand, controleer uw permissies')                                              # print output naar gebruiker

    if cron() == True and noinput == True:                                                                              #als cron() True is en noinput True is dan...(=connected to terminal)
        print(resultaat)                                                                                                #print resultaat
        sys.exit()                                                                                                      #sluit applicatie
    elif cron() == True and noinput == False:                                                                           #of als cron true is en noinput False is dan..(=connected to terminal)
        print(resultaat)                                                                                                #print resultaat
        input('druk op enter om verder te gaan...')                                                                     #vraag input om verder te gaan
        ToonMenu()                                                                                                      # input ontvangen, toon menu
        KeuzeInvoer()                                                                                                   # vraag om keuze
    elif cron() == False and noinput == False:                                                                          #of als cron() False is en noinput false is..
                                                                                                                        #(is niet connected aan terminal maar wel interactief, niet interactieve modus komt altijd in True,
                                                                                                                        #Dus toch weergevn om programma in IDE te laten werken (in IDE cron()==False)
        print(resultaat)                                                                                                #print resultaat
        input('druk op enter om verder te gaan...')
        ToonMenu()
        KeuzeInvoer()
    else:                                                                                                               #anders
        sys.exit(0)                                                                                                     #applicatie sluiten

                                                                                                                        # Functie om terminal te clearen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')                                                                    # Cleared terminal window op zowel Windows als Linux systemen. clear = linux cls = windows.

def cron():                                                                                                             # kijkt of stdout verbonden is met terminal
    return sys.stdout.isatty()                                                                                          # True = stdout verbonden met terminal
                                                                                                                        # False = stdout proces is cron of handmatig redirected naar ander proces of file
# Functie om command line opties te accepteren doormiddel van module Argeparse
def CommandoLineOpties():
    try:
        parser = argparse.ArgumentParser(description='Lijst met opties',
                                         add_help=True)                                                                 # Command line helpfunctie voor applicatie aanzetten

        parser.add_argument(ConfigFile('CliLetters', 'Missing'), dest='command', action='store_const', const='missing', # Command line letters aanmaken, letters instelbaar via config.ini. bijbehorende letter matcht altijd const='tekst'.
                            help='Toon missende bestanden')                                                             # Tevens een beschrijving wat de letter doet voor in de help functie.
        parser.add_argument(ConfigFile('CliLetters', 'Top10'), dest='command', action='store_const', const='top10',
                            help='Toon top10 downloads')
        parser.add_argument(ConfigFile('CliLetters', 'Connected'), dest='command', action='store_const',
                            const='connected',
                            help='Toon aantal connected clients')
        args = parser.parse_args()                                                                                      # Command line letter doorgeven aan module

                                                                                                                        # Definieren welke functie uitgevoerd moet worden bij ingeven letter in Command Line
                                                                                                                        # Functies worden uitgevoerd met functie(True) omdat dit de niet-interactieve navigatie van de applicatie is.
        if args.command == 'missing':
            notfound(True)

        elif args.command == 'top10':
            top10(True)

        elif args.command == 'connected':
            ConnectedClients(True)
        else:                                                                                                           # Wanneer er geen Command Line letters worden meegegeven zal de applicatie in interactieve modus starten
            ToonMenu()
            KeuzeInvoer()
    except KeyboardInterrupt:
        clear()
        sys.exit(0)


CommandoLineOpties()