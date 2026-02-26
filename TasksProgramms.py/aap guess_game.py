import random

def guess_the_number():
    target = random.randint(1, 100)
    attempts = 0
    
    print("Maine 1 se 100 ke beech ek number socha hai. Kya aap guess kar sakte hain?")

    while True:
        user_guess = int(input("Apna guess likhein: "))
        attempts += 1
        
        if user_guess < target:
            print("Thoda bada number try karein! (Too Low)")
        elif user_guess > target:
            print("Thoda chhota number try karein! (Too High)")
        else:
            print(f"Mubarak ho! Aapne {attempts} koshishon mein sahi guess kiya.")
            break

guess_the_number()
