param (
    [string]$file
)
gcc ./src/$file/convert.c -I ../MKTMultiApp/src/ -I dependencies -shared -Wno-implicit-int -o ./build/windows/$file.dll
