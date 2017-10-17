# vine

pretty printer for tree data structures

## Run Tests

```
python test_vine.py
```

## Example

input:
```
('players.1.name', 'Julie Andrews')
('players.1.email', 'julie@example.com')
('players.1.password', '$2b$12$/9c0zbwO1tWUV9xMOjLKgeYUSBqiSsOkhrwtX7waW4EHmElFYM7eC ')
('players.1.password.type', 'bcrypt')
('players.1.configs.color_theme', 'mocha')
('players.1.configs.screen_size', '1440x900')    
('players.2.name', 'John Von Neumann')
('players.2.email', '0x6a@0.0.0.1')
('players.2.password', 'fb6cecc85a100197ae3ad68d1f9f2886')
('players.2.password.type', 'md5')
('players.2.configs.color_theme', 'galactic')
('players.2.configs.screen_size', '128x80')
('players.3.email', 'donotreply@example.com')

('games.1.name', 'cat and mouse')
('games.1.rating', '5.6')    
('games.2.name', 'hard to get')
('games.2.rating', '3.2')    
('games.3.name', 'your mom')
('games.3.rating', '10.0')    
('games.4.name', "that's what she said")
('games.4.rating', '8.9')    
('games.5.name', 'play it cool')
('games.5.rating', 'pg-13')    
```

output:
```
players.1.name                 =  Julie Andrews
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
       .rating                 =  pg-13
```
