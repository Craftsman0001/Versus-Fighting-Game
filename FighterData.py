import pygame

def load_spritesheets():
    # function that downloads the fighters spritesheets for each action
    idle_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Idle.png")
    run_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Run.png")
    jump_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Jump.png")
    fall_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Fall.png")
    attack1_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Attack1.png")
    attack2_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Attack2.png")
    hit_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Take Hit.png")
    death_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Death.png")
    attack3_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Attack3.png")

    idle_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Idle.png")
    run_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Run.png")
    jump_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Jump.png")
    fall_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Fall.png")
    attack1_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Attack1.png")
    attack2_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Attack2.png")
    hit_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Take Hit.png")
    death_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Death.png")

    idle_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Idle.png")
    run_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Run.png")
    jump_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Going Up.png")
    fall_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Going Down.png")
    attack1_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Attack1.png")
    attack2_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Attack2.png")
    hit_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Take Hit.png")
    death_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Death.png")
    attack3_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Attack3.png")

    idle_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Idle.png")
    run_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Run.png")
    jump_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Jump.png")
    fall_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Fall.png")
    attack1_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Attack1.png")
    attack2_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Attack2.png")
    hit_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Take Hit.png")
    death_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Death.png")

    idle_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Idle.png")
    run_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Run.png")
    jump_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Jump.png")
    fall_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Fall.png")
    attack1_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Attack1.png")
    attack2_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Attack2.png")
    hit_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Take Hit 2.png")
    death_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Death.png")


    idle_Squire_sprite_sheet = pygame.image.load("Assets/Fighters/Squire/Idle.png")
    run_Squire_sprite_sheet = pygame.image.load("Assets/Fighters/Squire/Run.png")
    jump_Squire_sprite_sheet = pygame.image.load("Assets/Fighters/Squire/Jump.png")
    fall_Squire_sprite_sheet = pygame.image.load("Assets/Fighters/Squire/Fall.png")
    attack1_Squire_sprite_sheet = pygame.image.load("Assets/Fighters/Squire/Attack1.png")
    attack2_Squire_sprite_sheet = pygame.image.load("Assets/Fighters/Squire/Attack3.png")
    attack3_Squire_sprite_sheet = pygame.image.load("Assets/Fighters/Squire/Attack4.png")
    hit_Squire_sprite_sheet = pygame.image.load("Assets/Fighters/Squire/Take Hit.png")
    death_Squire_sprite_sheet = pygame.image.load("Assets/Fighters/Squire/Death.png")

    idle_knight_sprite_sheet = pygame.image.load("Assets/Fighters/Knight/Idle.png")
    run_knight_sprite_sheet = pygame.image.load("Assets/Fighters/Knight/Run.png")
    jump_knight_sprite_sheet = pygame.image.load("Assets/Fighters/Knight/Jump.png")
    fall_knight_sprite_sheet = pygame.image.load("Assets/Fighters/Knight/Fall.png")
    attack1_knight_sprite_sheet = pygame.image.load("Assets/Fighters/Knight/Attack.png")
    attack2_knight_sprite_sheet = pygame.image.load("Assets/Fighters/Knight/Attack.png")
    hit_knight_sprite_sheet = pygame.image.load("Assets/Fighters/Knight/Take Hit.png")
    death_knight_sprite_sheet = pygame.image.load("Assets/Fighters/Knight/Death.png")

    idle_Huntress_sprite_sheet = pygame.image.load("Assets/Fighters/Huntress/Idle.png")
    run_Huntress_sprite_sheet = pygame.image.load("Assets/Fighters/Huntress/Run.png")
    jump_Huntress_sprite_sheet = pygame.image.load("Assets/Fighters/Huntress/Jump.png")
    fall_Huntress_sprite_sheet = pygame.image.load("Assets/Fighters/Huntress/Fall.png")
    attack_Huntress_sprite_sheet = pygame.image.load("Assets/Fighters/Huntress/Attack.png")
    # projectile_Huntress_sprite_sheet = pygame.image.load("Assets/Fighters/Huntress/Arrow/Static.png")
    attack2_Huntress_sprite_sheet = pygame.image.load("Assets/Fighters/Huntress/Attack.png")
    hit_Huntress_sprite_sheet = pygame.image.load("Assets/Fighters/Huntress/Get Hit.png")
    death_Huntress_sprite_sheet = pygame.image.load("Assets/Fighters/Huntress/Death.png")


    return {
        "fantasy_warrior": [idle_fantasy_warrior_sprite_sheet, run_fantasy_warrior_sprite_sheet, jump_fantasy_warrior_sprite_sheet, fall_fantasy_warrior_sprite_sheet, attack1_fantasy_warrior_sprite_sheet, attack2_fantasy_warrior_sprite_sheet, hit_fantasy_warrior_sprite_sheet, death_fantasy_warrior_sprite_sheet, attack3_fantasy_warrior_sprite_sheet],
        "wizard": [idle_wizard_sprite_sheet, run_wizard_sprite_sheet, jump_wizard_sprite_sheet, fall_wizard_sprite_sheet, attack1_wizard_sprite_sheet, attack2_wizard_sprite_sheet, hit_wizard_sprite_sheet, death_wizard_sprite_sheet],
        "martial_hero": [idle_martial_hero_sprite_sheet, run_martial_hero_sprite_sheet, jump_martial_hero_sprite_sheet, fall_martial_hero_sprite_sheet, attack1_martial_hero_sprite_sheet, attack2_martial_hero_sprite_sheet, hit_martial_hero_sprite_sheet, death_martial_hero_sprite_sheet, attack3_martial_hero_sprite_sheet],
        "oni_samurai": [idle_oni_samurai_sprite_sheet, run_oni_samurai_sprite_sheet, jump_oni_samurai_sprite_sheet, fall_oni_samurai_sprite_sheet, attack1_oni_samurai_sprite_sheet, attack2_oni_samurai_sprite_sheet, hit_oni_samurai_sprite_sheet, death_oni_samurai_sprite_sheet],
        "samurai": [idle_samurai_sprite_sheet, run_samurai_sprite_sheet, jump_samurai_sprite_sheet, fall_samurai_sprite_sheet, attack1_samurai_sprite_sheet, attack2_samurai_sprite_sheet, hit_samurai_sprite_sheet, death_samurai_sprite_sheet],
        "Squire" :[idle_Squire_sprite_sheet, run_Squire_sprite_sheet, jump_Squire_sprite_sheet, fall_Squire_sprite_sheet, attack1_Squire_sprite_sheet, attack2_Squire_sprite_sheet, hit_Squire_sprite_sheet, death_Squire_sprite_sheet, attack3_Squire_sprite_sheet],
        "Knight" : [idle_knight_sprite_sheet, run_knight_sprite_sheet, jump_knight_sprite_sheet, fall_knight_sprite_sheet, attack1_knight_sprite_sheet, attack2_knight_sprite_sheet, hit_knight_sprite_sheet, death_knight_sprite_sheet],
        "Huntress" : [idle_Huntress_sprite_sheet, run_Huntress_sprite_sheet, jump_Huntress_sprite_sheet, fall_Huntress_sprite_sheet, attack_Huntress_sprite_sheet, attack2_Huntress_sprite_sheet, hit_Huntress_sprite_sheet, death_Huntress_sprite_sheet]
    }

def load_animation_steps():
    # function that has the number of frames for each spritesheet
    idle_fantasy_warrior_animation_steps = [10]
    run_fantasy_warrior_animation_steps = [8]
    jump_fantasy_warrior_animation_steps = [3]
    fall_fantasy_warrior_animation_steps = [3]
    attack1_fantasy_warrior_animation_steps = [7]
    attack2_fantasy_warrior_animation_steps = [7]
    hit_fantasy_warrior_animation_steps = [3]
    death_fantasy_warrior_animation_steps = [7]
    attack3_fantasy_warrior_animation_steps = [8]

    idle_wizard_animation_steps = [8]
    run_wizard_animation_steps = [8]
    jump_wizard_animation_steps = [2]
    fall_wizard_animation_steps = [2]
    attack1_wizard_animation_steps = [8]
    attack2_wizard_animation_steps = [8]
    hit_wizard_animation_steps = [3]
    death_wizard_animation_steps = [7]

    idle_martial_hero_animation_steps = [10]
    run_martial_hero_animation_steps = [8]
    jump_martial_hero_animation_steps = [3]
    fall_martial_hero_animation_steps = [3]
    attack1_martial_hero_animation_steps = [7]
    attack2_martial_hero_animation_steps = [6]
    hit_martial_hero_animation_steps = [3]
    death_martial_hero_animation_steps = [11]
    attack3_martial_hero_animation_steps = [9]

    idle_oni_samurai_animation_steps = [4]
    run_oni_samurai_animation_steps = [8]
    jump_oni_samurai_animation_steps = [2]
    fall_oni_samurai_animation_steps = [2]
    attack1_oni_samurai_animation_steps = [4]
    attack2_oni_samurai_animation_steps = [4]
    hit_oni_samurai_animation_steps = [3]
    death_oni_samurai_animation_steps = [7]

    idle_samurai_animation_steps = [8]
    run_samurai_animation_steps = [8]
    jump_samurai_animation_steps = [2]
    fall_samurai_animation_steps = [2]
    attack1_samurai_animation_steps = [6]
    attack2_samurai_animation_steps = [6]
    hit_samurai_animation_steps = [4]
    death_samurai_animation_steps = [6]


    idle_Squire_animation_steps = [8]
    run_Squire_animation_steps = [8]
    jump_Squire_animation_steps = [2]
    fall_Squire_animation_steps = [2]
    attack1_Squire_animation_steps = [4]
    attack2_Squire_animation_steps = [4]
    attack3_Squire_animation_steps = [4]
    hit_Squire_animation_steps = [4]
    death_Squire_animation_steps = [6]

    idle_knight_animation_steps = [11]
    run_knight_animation_steps = [8]
    jump_knight_animation_steps = [4]
    fall_knight_animation_steps = [4]
    attack1_knight_animation_steps = [6]
    attack2_knight_animation_steps = [6]
    hit_knight_animation_steps = [4]
    death_knight_animation_steps = [9]

    idle_Huntress_animation_steps = [10]
    run_Huntress_animation_steps = [8]
    jump_Huntress_animation_steps = [2]
    fall_Huntress_animation_steps = [2]
    attack_Huntress_animation_steps = [6]
    projectile_Huntress_animation_steps = [1]
    hit_Huntress_animation_steps = [3]
    death_Huntress_animation_steps = [10]

    return {
        "fantasy_warrior": [idle_fantasy_warrior_animation_steps, run_fantasy_warrior_animation_steps, jump_fantasy_warrior_animation_steps, fall_fantasy_warrior_animation_steps,  attack1_fantasy_warrior_animation_steps, attack2_fantasy_warrior_animation_steps, hit_fantasy_warrior_animation_steps, death_fantasy_warrior_animation_steps, attack3_fantasy_warrior_animation_steps],
        "wizard": [idle_wizard_animation_steps, run_wizard_animation_steps, jump_wizard_animation_steps, fall_wizard_animation_steps, attack1_wizard_animation_steps, attack2_wizard_animation_steps, hit_wizard_animation_steps, death_wizard_animation_steps],
        "martial_hero": [idle_martial_hero_animation_steps, run_martial_hero_animation_steps, jump_martial_hero_animation_steps, fall_martial_hero_animation_steps, attack1_martial_hero_animation_steps, attack2_martial_hero_animation_steps, hit_martial_hero_animation_steps, death_fantasy_warrior_animation_steps, attack3_martial_hero_animation_steps],
        "oni_samurai": [idle_oni_samurai_animation_steps, run_oni_samurai_animation_steps, jump_oni_samurai_animation_steps, fall_oni_samurai_animation_steps, attack1_oni_samurai_animation_steps, attack2_oni_samurai_animation_steps, hit_oni_samurai_animation_steps, death_oni_samurai_animation_steps],
        "samurai": [idle_samurai_animation_steps, run_samurai_animation_steps, jump_samurai_animation_steps, fall_samurai_animation_steps, attack1_samurai_animation_steps, attack2_samurai_animation_steps, hit_samurai_animation_steps, death_samurai_animation_steps],
        "Squire" : [idle_Squire_animation_steps, run_Squire_animation_steps, jump_Squire_animation_steps, fall_Squire_animation_steps, attack1_Squire_animation_steps, attack2_Squire_animation_steps, hit_Squire_animation_steps, death_Squire_animation_steps, attack3_Squire_animation_steps],
        "Knight" : [idle_knight_animation_steps, run_knight_animation_steps, jump_knight_animation_steps, fall_knight_animation_steps, attack1_knight_animation_steps, attack2_knight_animation_steps, hit_knight_animation_steps, death_knight_animation_steps],
        "Huntress" : [idle_Huntress_animation_steps, run_Huntress_animation_steps, jump_Huntress_animation_steps, fall_Huntress_animation_steps, attack_Huntress_animation_steps, projectile_Huntress_animation_steps, hit_Huntress_animation_steps, death_Huntress_animation_steps]
    }

def fighter_variables() :
    #function that has the data for each fighter
    fantasy_warrior_x_size = 162
    fantasy_warrior_y_size = 162
    fantasy_warrior_scale = 4
    fantasy_warrior_offset = [72, 56]
    fantasy_warrior_timer_attack_1 = 350
    fantasy_warrior_timer_attack_2 = 200
    fantasy_warrior_timer_attack_3 = 450

    wizard_x_size = 250
    wizard_y_size = 250
    wizard_scale = 3
    wizard_offset = [112, 107]
    wizard_timer_attack_1 = 400
    wizard_timer_attack_2 = 400
    wizard_timer_attack_3 = 0

    martial_hero_x_size = 126
    martial_hero_y_size = 126
    martial_hero_scale = 3.5
    martial_hero_offset = [50, 30.5]
    martial_hero_timer_attack_1 = 350
    martial_hero_timer_attack_2 = 200
    martial_hero_timer_attack_3 = 550

    oni_samurai_x_size = 200
    oni_samurai_y_size = 200
    oni_samurai_scale = 3.3
    oni_samurai_offset = [85, 73.5]
    oni_samurai_timer_attack_1 = 200
    oni_samurai_timer_attack_2 = 200
    oni_samurai_timer_attack_3 = 0

    samurai_x_size = 200
    samurai_y_size = 200
    samurai_scale = 3.3
    samurai_offset = [88, 67.5]
    samurai_timer_attack_1 = 5000 #280
    samurai_timer_attack_2 = 5000 #300
    samurai_timer_attack_3 = 0


    Squire_x_size = 150
    Squire_y_size = 150
    Squire_scale = 3.7
    Squire_offset = [65, 46]
    Squire_timer_attack_1 = 200
    Squire_timer_attack_2 = 200
    Squire_timer_attack_3 = 200

    knight_x_size = 140
    knight_y_size = 140
    knight_scale = 3.7
    knight_offset = [60, 34.5]
    knight_timer_attack_1 = 300
    knight_timer_attack_2 = 300
    knight_timer_attack_3 = 0

    Huntress_x_size = 100
    Huntress_y_size = 100
    Huntress_scale = 4
    Huntress_offset = [37.5, 22]
    Huntress_projectile_x_size = 24
    Huntress_projectile_y_size = 5
    Huntress_projectile_image_scale = 1.3
    Huntress_projectile_y_offset = -30
    Huntress_projectile_width = 100
    Huntress_projectile_height = 20

    return {
        "fantasy_warrior" : [fantasy_warrior_x_size, fantasy_warrior_y_size, fantasy_warrior_scale, fantasy_warrior_offset, fantasy_warrior_timer_attack_1, fantasy_warrior_timer_attack_2, fantasy_warrior_timer_attack_3],
        "wizard" : [wizard_x_size, wizard_y_size, wizard_scale, wizard_offset, wizard_timer_attack_1, wizard_timer_attack_2, wizard_timer_attack_3],
        "martial_hero" : [martial_hero_x_size, martial_hero_y_size, martial_hero_scale, martial_hero_offset, martial_hero_timer_attack_1, martial_hero_timer_attack_2, martial_hero_timer_attack_3],
        "oni_samurai" : [oni_samurai_x_size, oni_samurai_y_size, oni_samurai_scale, oni_samurai_offset, oni_samurai_timer_attack_1, oni_samurai_timer_attack_2, oni_samurai_timer_attack_3],
        "samurai": [samurai_x_size, samurai_y_size, samurai_scale, samurai_offset, samurai_timer_attack_1, samurai_timer_attack_2, samurai_timer_attack_3],
        "Squire": [Squire_x_size, Squire_y_size, Squire_scale, Squire_offset, Squire_timer_attack_1, Squire_timer_attack_2, Squire_timer_attack_3],
        "Knight" : [knight_x_size, knight_y_size, knight_scale, knight_offset, knight_timer_attack_1, knight_timer_attack_2, knight_timer_attack_3],
        "Huntress" : [Huntress_x_size, Huntress_y_size, Huntress_scale, Huntress_offset, Huntress_projectile_x_size, Huntress_projectile_y_size, Huntress_projectile_image_scale, Huntress_projectile_y_offset, Huntress_projectile_width, Huntress_projectile_height]
    }

def projectiles() :
    #function that has the data for each fighter projectile
    projectile_sprite_sheet = pygame.image.load("Assets/Fighters/Huntress/Arrow/Move.png")
    projectile_animation_steps = [2]

    return {
        "Huntress" : [projectile_sprite_sheet, projectile_animation_steps]
    }

def BackGrounds() :
    background1 = [pygame.image.load("Assets/BackGrounds/Landscape1.jpg"), -200]
    background2 = [pygame.image.load("Assets/BackGrounds/Landscape2.png"), -150]
    background3 = [pygame.image.load("Assets/BackGrounds/Landscape3.png"), -150]
    background4 = [pygame.image.load("Assets/BackGrounds/Landscape4.png"), -150]
    background5 = [pygame.image.load("Assets/BackGrounds/Landscape5.png"), -193]
    background6 = [pygame.image.load("Assets/BackGrounds/Landscape6.png"), -150]
    images = [background1, background2, background3, background4, background5, background6]

    return images


