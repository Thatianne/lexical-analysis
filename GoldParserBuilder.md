## Instalação do Gold Parser Build
### Instalar wine
### Instalar winetricks
### Baixar Gold Parser Build
### Baixar .NET 3.5
### Criar prefixo do SO de 32bits
  ``` bash
WINEARCH=win32 WINEPREFIX=~/.wine32 winecfg
```
### Selecionar SO Windows XP
  ``` bash
env WINEPREFIX=~/.wine32 winecfg
```
  Windows Version = Windows XP
  OK
### Instalar .NET
``` bash
env WINEPREFIX=~/.wine32 winetricks
```
 - Install an application -> OK -> Cancel -> Run uninstaller -> Install -> selecionar o executável do .Net 3.5 baixado

### Instalar Gold Parser Build
```bash
env WINEPREFIX=~/.wine32 wine GOLDBuilder.exe
```
### Rodar Gold Parser Build
```bash
env WINEPREFIX=~/.wine32 wine ~/.wine32/drive_c/Program\ Files/GOLD\ Parser\ Builder/GOLDBuilder.exe
```