# resources: https://docs.python.org/3/library/os.html
import os

# List of bad file extensions that I got from https://sensorstechforum.com/popular-windows-file-types-used-malware-2018/
badExtensions = ['.shadow', ' .djvu', ' .djvur', ' .djvuu',
                 ' .udjvu', ' .uudjvu', ' .djvuq', ' .djvus', ' .djvur',
                 ' .djvut', ' .pdff', ' .tro', ' .tfude', ' .tfudet', ' .tfudeq',
                 ' .rumba', ' .adobe', ' .adobee', ' .blower', ' .promos', ' .promoz',
                 ' .promorad', ' .promock', ' .promok', ' .promorad2', ' .kroput',
                 ' .kroput1', ' .pulsar1', ' .kropun1', ' .charck', ' .klope',
                 ' .kropun', ' .charcl', ' .doples', ' .luces', ' .luceq',
                 ' .chech', ' .proden', ' .drume', ' .tronas', ' .trosak',
                 ' .grovas', ' .grovat', ' .roland', ' .refols', ' .raldug',
                 ' .etols', ' .guvara', ' .browec', ' .norvas', ' .moresa',
                 ' .vorasto', ' .hrosas', ' .kiratos', ' .todarius', ' .hofos',
                 ' .roldat', ' .dutan', ' .sarut', ' .fedasot', ' .berost',
                 ' .forasom', ' .fordan', ' .codnat', ' .codnat1', ' .bufas',
                 ' .dotmap', ' .radman', ' .ferosas', ' .rectot', ' .skymap',
                 ' .mogera', ' .rezuc', ' .stone', ' .redmat', ' .lanset',
                 ' .davda', ' .poret', ' .pidom', ' .pidon', ' .heroset',
                 ' .boston', ' .muslat', ' .gerosan', ' .vesad', ' .horon',
                 ' .neras', ' .truke', ' .dalle', ' .lotep', ' .nusar',
                 ' .litar', ' .besub', ' .cezor', ' .lokas', ' .godes',
                 ' .budak', ' .vusad', ' .herad', ' .berosuce', ' .gehad',
                 ' .gusau', ' .madek', ' .darus', ' .tocue', ' .lapoi',
                 ' .todar', ' .dodoc', ' .bopador', ' .novasof', ' .ntuseg',
                 ' .ndarod', ' .access', ' .format', ' .nelasod', ' .mogranos',
                 ' .cosakos', ' .nvetud', ' .lotej', ' .kovasoh', ' .prandel',
                 ' .zatrov', ' .masok', ' .brusaf', ' .londec', ' .krusop',
                 ' .mtogas', ' .nasoh', ' .nacro', ' .pedro', ' .nuksus',
                 ' .vesrato', ' .masodas', ' .cetori', ' .stare', ' .carote',
                 ' .gero', ' .hese', ' .seto', ' .peta', ' .moka', ' .kvag', ' .karl',
                 ' .nesa', ' .noos', ' .kuub', ' .reco', ' .bora', '.pcapng', '.mp4',
                 '.mp3', '.m4v', '.mov', '.avi', '.asf']

# TODO: badFiles
# TODO: installing clamav
# TODO: lots of stuff

def main():
    choice = input("1. Check for users \n2. Scan for bad files \n3. Install ClamAV \n")
    choice = int(choice)
    if (choice == 1):
        print("Checking for users")
        users()
    elif (choice == 2):
        print("Checking for bad files")
        scanMalicious()
    else:
        print("Installing ClamAV")
        clamAV()

# Scans the whole computer and checks each file's extensions and compares it to the list of badExtensions
def scanMalicious():
    input("Scanning the whole computer")
    for root, dirs, files in os.walk("/"):
        for file in files:
            filename, extension = os.path.splitext(file)
            for bad in badExtensions:
                if(extension == bad):
                    print("Filename: " + filename + " Extention: " + extension)
# Takes a list of users that are approved and their account type and checks it against the list of users on the computer
def users():
    pass

#Installs a simple antivirus
def clamAV():
    pass


main()
