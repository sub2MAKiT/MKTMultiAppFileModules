# windows wsl is a bit special so...
import os
import sys

os.system('gcc ./src/{}/convert.c -I ../MKTMultiApp/src/ -I dependencies -shared -Wno-implicit-int -o ./build/windows/{}.so'.format(sys.argv[1],sys.argv[1]))

