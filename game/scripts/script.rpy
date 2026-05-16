default ai_name = "Companion"
default ai_mode = "gentle"
default energy_battery = 100
default sensory_load = 0

define n = Character(None, what_italic=True, what_color="#340671")
define ai = Character("[ai_name]", color="#5ec1c0")
define barista = Character("Barista", color="#cb6f1e")
define parent = Character("Family Member", color="#b9237d")

label start:
    scene black
    with dissolve
    
    n "Initializing Social Support Interface V1.0..."
    n "Before we boot up the environment simulations, let's configure your AI Companion."

    python:
        ai_name_input = renpy.input("What name would you like to give your AI Companion?", default="Aria")
        ai_name = ai_name_input.strip()
        if not ai_name:
            ai_name = "Aria"

    n "Name saved as [ai_name]."

    menu:
        n "Select your companion's core operating protocol:"
        
        "Gentle Support Mode (Soft encouragement, low pressure)":
            $ ai_mode = "gentle"
            jump companion_awakened

        "Analytical Anchor Mode (Logic-driven breakdown, explicit data)":
            $ ai_mode = "analytical"
            jump companion_awakened

label companion_awakened:
    scene black
    with dissolve

    if ai_mode == "gentle":
        ai "System active! Hi, I'm [ai_name]. I'm locked onto your biosignals. No matter how overwhelming things get, we take it at your pace. Ready?"
    else:
        ai "System operational. Protocol: Analytical Anchor. I will scan rooms, decode subtext, and keep track of your metrics. Let us begin."

    n "Your current metrics: Battery [energy_battery]%% | Sensory Load [sensory_load]%%."
    jump setting_one_cafe

label setting_one_cafe:
    n "Setting 1: The Local Coffee Shop. The hum of the espresso machine is loud, and a long line is forming behind you."
    barista "Next up! What can I get for you?"

    menu:
        "Panic and order a random drink just to get it over with":
            $ energy_battery -= 20
            $ sensory_load += 15
            if ai_mode == "gentle":
                ai "Hey, it's okay. You felt rushed, and that's a normal response. Let's step to a quieter corner."
            else:
                ai "Observation: High-pressure timing caused a system bypass. Battery down to [energy_battery]%%."

        "Take an extra 5 seconds to look at the menu and order your exact comfort drink":
            $ energy_battery -= 5
            $ sensory_load += 5
            if ai_mode == "gentle":
                ai "Incredible job holding your ground! You took the time you needed."
            else:
                ai "Optimal execution. Sensory impact managed effectively. Efficiency remains nominal."

    jump setting_two_hallway

label setting_two_hallway:
    n "Setting 2: The Main Corridor. Class just ended. The hallway is a chaotic sea of movement, shouting, and slamming lockers."
    
    if ai_mode == "gentle":
        ai "This is incredibly loud. Remember, you don't have to push through this crowd if you don't want to."
    else:
        ai "Environmental Scan: Audio decibels hitting peak tolerances. Hallway density high."

    menu:
        "Put your headphones on, block out the world, and take the long, empty side corridor":
            $ energy_battery += 10
            n "You slip away from the crowd. The quiet hallway lets your nervous system reset."
            ai "Smart detour. Protecting your battery level is a tactical win."

        "Mask your discomfort, push through the main crowd to be on time, and absorb the noise":
            $ sensory_load += 40
            $ energy_battery -= 35
            if ai_mode == "gentle":
                ai "That was immense pressure. Let's find a wall to lean against for a moment. I'm right here with you."
            else:
                ai "Warning: Critical spike in Sensory Load ([sensory_load]%%). Battery dangerously low."

    jump setting_three_dinner

label setting_three_dinner:
    n "Setting 3: The Dinner Table. The sensory load is quieter, but a family member looks at you expectantly."
    parent "So...how was your day? You seem sort of 'distant' today."

    if ai_mode == "analytical":
        ai "Parsing subtext: They aren't criticizing you. This is an expression of care cloaked in ambiguous wording."

    menu:
        "Give a scripted, masked answer: 'I'm fine, just tired!' and force eye contact":
            $ energy_battery -= 15
            n "They nod, satisfied by the script, but the internal masking drains your remaining reserve."
            ai "Script successfully executed. However, your battery has fallen to [energy_battery]%%."

        "Be honest with boundaries: 'My brain is completely cooked, but I'm glad to be home'":
            $ energy_battery += 5
            n "The honesty clears the air. You don't have to force an act at home."
            if ai_mode == "gentle":
                ai "I am so incredibly proud of you for communicating your actual needs clearly!"
            else:
                ai "Authentic parameter transmission successful. Social friction neutralized cleanly."
            jump game_conclusion

label game_conclusion:
    scene black
    with dissolve

    ai "The simulation day has officially concluded! Let's check out your diagnostic profile."

    if energy_battery < 40:
        ai "Your final Social Battery dropped down to [energy_battery]%%. That means today was an uphill battle against extreme fatigue."
        ai "You didn't fail. Navigating an unaccommodating world is exhausting work. Please give yourself permission to completely recharge right now."
    else:
        ai "Excellent stabilization! Your final Social Battery finished at [energy_battery]%%."
        ai "By utilizing strategically calculated detours, boundaries, and comfort choices, you effectively protected your peace today. Outstanding work."

    n "Thank you for running the program. You are doing much better than you realize."
    return