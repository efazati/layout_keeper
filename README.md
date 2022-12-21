# Layout Keeper

create a new config file same as `config_4k.py` and list all of the postions and applications you want, also you can use `postion_finder.py` to findout what is the current position of your applications

#### position_finder.py
```
PS C:\apps\shortcuts> python.exe .\position_finder.py
? README.md - shortcuts - Visual Studio Code :: Size: [2194, 1186] Pos: [0, 0]
keybindigs.ahk - Notepad :: Size: [570, 744] Pos: [905, 211]
```

### Depenedency
- Win 10 - 11
- https://ritchielawrence.github.io/cmdow/

### Example
```
positions = {
    'left_side_up': {
        'siz': [703, 693],
        'pos': [-2566, 0]
    },
    'left_side_down': {
        'siz': [703, 711],
        'pos': [-2566, 687]
    }
}
```

```
modes = [
    {'name': 'Browse',
     'apps': [
         {'name': 'Google Chat', 'pos': 'left_side_up'},
         {'name': 'Webex', 'pos': 'left_side_down'},
        ],
   }
] 
```
For app name, always use the static part of the app name, so for example this is visual studio title `? README.md - shortcuts - Visual Studio Code`, I picked `Visual Studio` as the app name
Also you can use autohotkey.com to create a keybinding for each mode

```
^!4::
Run, C:\apps\shortcuts\Standup.cmd
return
```