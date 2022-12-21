positions = {
    'left_side_up': {
        'siz': [703, 693],
        'pos': [-2566, 0]
    },
    'left_side_down': {
        'siz': [703, 711],
        'pos': [-2566, 687]
    },
    'left_main': {
        'siz': [1869, 1392],
        'pos': [-1869, 0]
    },
    'right_main': {
        'siz': [2194, 1186],
        'pos': [0, 0]
    },
    'left_half_left': {
        'siz': [1283, 1392],
        'pos': [-2566, 0]
    },
    'left_half_right': {
        'siz': [1283, 1392],
        'pos': [-1283, 0]
    },
}

modes = [
    {'name': 'Browse',
     'apps': [
         {'name': 'Obsidian', 'pos': 'left_main'},
         {'name': 'Google Chat', 'pos': 'left_side_up'},
         {'name': 'Google Calendar', 'pos': 'left_side_down'},
         {'name': 'Sidebery', 'pos': 'right_main'},
        ],
    'active': 'Sidebery',
    },
    {'name': 'Code',
     'apps': [
         {'name': 'Sidebery', 'pos': 'left_main'},
         {'name': 'Google Chat', 'pos': 'left_side_up'},
         {'name': 'Google Calendar', 'pos': 'left_side_down'},
         {'name': 'Visual Studio', 'pos': 'right_main'},
        ],
    'active': 'Visual Studio',
    },
    {'name': 'Chat',
     'apps': [
         {'name': 'Sidebery', 'pos': 'right_main'},
         {'name': 'Google Chat', 'pos': 'left_half_left'},
         {'name': 'Webex', 'pos': 'left_half_right'},
        ],
    'active': 'Google Chat',
    },
    {'name': 'Meet',
     'apps': [
         {'name': 'Sidebery', 'pos': 'right_main'},
         {'name': 'Google Chat', 'pos': 'left_side_up'},
         {'name': 'Google Calendar', 'pos': 'left_side_down'},
         {'name': 'Google Meet', 'pos': 'left_main'},
        ],
    'active': 'Google Meet',
    },
    {'name': 'Remote',
     'apps': [
         {'name': 'Sidebery', 'pos': 'left_main'},
         {'name': 'Google Chat', 'pos': 'left_side_up'},
         {'name': 'Google Calendar', 'pos': 'left_side_down'},
         {'name': 'MyRemotePC ', 'pos': 'right_main'},
        ],
    'active': 'MyRemotePC ',
    },
    {'name': 'Standup',
     'apps': [
         {'name': 'Google Meet', 'pos': 'left_main'},
         {'name': 'Google Chat', 'pos': 'left_side_up'},
         {'name': 'Google Calendar', 'pos': 'left_side_down'},
         {'name': 'MyRemotePC ', 'pos': 'right_main'},
        ],
    'active': 'MyRemotePC ',
    },
]
