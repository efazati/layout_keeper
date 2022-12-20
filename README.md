# Layout Keeper

create a new config file same as `core/config_4k.py` and list all of the postions and applications you want, also you can use `postion_finder.py` to findout what is the current position of your applications

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

Also you can use autohotkey.com to create a keybinding for each mode

```
^!4::
Run, C:\apps\shortcuts\Standup.cmd
return
```