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


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    start = input("{}WARNING: If your forensic question requires information from user accounts or the location of a malicious file, enter 0 to prevent this script from deleting information. Otherwise enter 1 to allow the program to delete files and user information.{} ".format(colors.WARNING, colors.END))
    delete = False
    if(start == 1):
        delete = True
    choice = input("1. Check for users 2. Scan for bad files 3. Install Security Software ")
    choice = int(choice)
    if (choice == 1):
        print("Checking for users")
        users(delete)
    elif (choice == 2):
        scanMalicious(delete)
    else:
        print("Installing ClamAV")
        #securitySoftware(delete)


def scanMalicious(delete):
    print(f"{colors.HEADER}Scanning the whole computer{colors.END}")
    locs = []
    for root, dirs, files in os.walk("/"):
        for file in files:
            filename, extension = os.path.splitext(file)
            for bad in badExtensions:
                if(extension == '.jpg'):
                    #print("Filename: " + filename + " Extention: " + extension)
                    locs.append(file)
    fileStorage = "malicious_files_list.txt"
    desktopFile = open(fileStorage, "w")
    desktopFile.write("\n".join(locs))
    desktopFile.close
    print(f"{colors.UNDERLINE}File '{fileStorage}' created{colors.END}")


def users(delete):
    #if(delete):
    userList = input(f"{colors.HEADER}Enter the name of the users that should be on the device seperated by commas. Any user not mentiond in this list will be deleted:{colors.END} ")
    userList = userList.split(",")
    print(type(userList))
    print(userList)

#def securitySoftware(delete):
    #f(delete):
    # TODO:


main()
#scanMalicious()
