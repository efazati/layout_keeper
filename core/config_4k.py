positions = {
    'left_side_up': {
        'siz': [954, 703],
        'pos': [-2573, -7]
    },
    'left_side_down': {
        'siz': [942, 715],
        'pos': [-2567, 684]
    },
    'left_main': {
        'siz': [1647, 1410],
        'pos': [-1636, -7]
    },
    'right_main': {
        'siz': [2072, 1405],
        'pos': [-7, -7]
    },
    'right_side': {
        'siz': [521, 1412],
        'pos': [2052, 0]
    },
}

modes = [
    {'name': 'Browse',
     'apps': [
         {'name': 'Obsidian', 'pos': 'left_main'},
         {'name': 'Google Chat', 'pos': 'left_side_up'},
         {'name': 'Webex', 'pos': 'left_side_down'},
         {'name': 'Sidebery', 'pos': 'right_main'},
         {'name': 'Google Calendar', 'pos': 'right_side'},
        ],
    'active': 'Sidebery',
    },
    {'name': 'Code',
     'apps': [
         {'name': 'Sidebery', 'pos': 'left_main'},
         {'name': 'Google Chat', 'pos': 'left_side_up'},
         {'name': 'Webex', 'pos': 'left_side_down'},
         {'name': 'Visual Studio', 'pos': 'right_main'},
         {'name': 'Google Calendar', 'pos': 'right_side'},
        ],
    'active': 'Sidebery',
    }
]
