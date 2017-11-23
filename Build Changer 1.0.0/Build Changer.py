import os
import spttConfig
import buildType
import datetime



year = datetime.date.today().year

sysdrive = os.environ['systemdrive']

programFilesPath = sysdrive+'\ProgramData\Builds_SmartPTT'

source = '\\orpo-tfs-buildbot.elcom.local\Artifact share\Binaries (NOT ENCRYPTED, FAST BUILD)'
target = 'C:\Program Files (x86)\SmartPTT'
wrongAnswer = 'Wrong answer. Please try again'
buildPath = "D:\Repo_I"

def start(x):
    spttVerList = {'1', '2', 'RF', 'rf'}

    while True:

        if x == '1':
            return(float(9.1))
            break
        elif x == '2':
            return(float(9.2))
            break

        if x in spttVerList:
            if x == 'RF' or 'rf':
                print(os.startfile('D:\Python develop'))
                return start(spttConfig.intro())

        if x not in spttVerList:
            print(wrongAnswer)
            return start(spttConfig.intro())


checkType = start(spttConfig.intro())

buildTypeOutput = buildType.buildTypeLetter(checkType)

def selectingBuildType(x):
    configList = {'e', 'p', 'DD', 'dd'}

    while True:

        if x == 'e':
            return('enterprise_' + str(year))
            break
        elif x == 'p':
            return('PLUS_' + str(year))
            break
        elif x == 'DD' or 'dd':
            if x in configList:
                return float(1.0)
        elif x not in configList:
            print(wrongAnswer)
            return selectingBuildType(buildTypeOutput)

selectedBuild = type(selectingBuildType(buildTypeOutput))

if selectedBuild is not float:
    def tryDef():
        try:
            os.stat("D:\Repo_I3")
        except OSError:
            return False
        return True
    if tryDef() == True:
       print('11')
    else:
       os.mkdir(r'str(programFilesPath) + '\\' + str(checkType))

if selectedBuild == float:
    print('1')
