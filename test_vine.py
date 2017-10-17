from vine import Node


expected_output = (
'''players.1.name                 =  Julie Andrews
         .email                =  julie@example.com
         .password             =  $2b$12$/9c0zbwO1tWUV9xMOjLKgeYUSBqiSsOkhrwtX7waW4EHmElFYM7eC 
                  .type        =  bcrypt
         .configs.color_theme  =  mocha
                 .screen_size  =  1440x900
       .2.name                 =  John Von Neumann
         .email                =  0x6a@0.0.0.1
         .password             =  fb6cecc85a100197ae3ad68d1f9f2886
                  .type        =  md5
         .configs.color_theme  =  galactic
                 .screen_size  =  128x80
       .3.email                =  donotreply@example.com
games.1.name                   =  cat and mouse
       .rating                 =  5.6
     .2.name                   =  hard to get
       .rating                 =  3.2
     .3.name                   =  your mom
       .rating                 =  10.0
     .4.name                   =  that's what she said
       .rating                 =  8.9
     .5.name                   =  play it cool
       .rating                 =  pg-13''')


def test_tree():
    tree = Node()

    tree.add_value_by_path('players.1.name', 'Julie Andrews')
    tree.add_value_by_path('players.1.email', 'julie@example.com')
    tree.add_value_by_path('players.1.password', '$2b$12$/9c0zbwO1tWUV9xMOjLKgeYUSBqiSsOkhrwtX7waW4EHmElFYM7eC ')
    tree.add_value_by_path('players.1.password.type', 'bcrypt')
    tree.add_value_by_path('players.1.configs.color_theme', 'mocha')
    tree.add_value_by_path('players.1.configs.screen_size', '1440x900')    

    tree.add_value_by_path('players.2.name', 'John Von Neumann')
    tree.add_value_by_path('players.2.email', '0x6a@0.0.0.1')
    tree.add_value_by_path('players.2.password', 'fb6cecc85a100197ae3ad68d1f9f2886')
    tree.add_value_by_path('players.2.password.type', 'md5')
    tree.add_value_by_path('players.2.configs.color_theme', 'galactic')
    tree.add_value_by_path('players.2.configs.screen_size', '128x80')

    tree.add_value_by_path('players.3.email', 'donotreply@example.com')

    tree.add_value_by_path('games.1.name', 'cat and mouse')
    tree.add_value_by_path('games.1.rating', '5.6')    
    tree.add_value_by_path('games.2.name', 'hard to get')
    tree.add_value_by_path('games.2.rating', '3.2')    
    tree.add_value_by_path('games.3.name', 'your mom')
    tree.add_value_by_path('games.3.rating', '10.0')    
    tree.add_value_by_path('games.4.name', "that's what she said")
    tree.add_value_by_path('games.4.rating', '8.9')    
    tree.add_value_by_path('games.5.name', 'play it cool')
    tree.add_value_by_path('games.5.rating', 'pg-13')    
    assert(tree.str() == expected_output)
    print(expected_output)
    print('\n TESTS PASS \n')

    
if __name__ == '__main__':
    test_tree()
