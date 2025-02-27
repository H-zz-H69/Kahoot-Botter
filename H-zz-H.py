import sys
import asyncio
import os
import itertools
from kahoot import KahootClient
from colorama import Fore, init

init(autoreset=True)

def logo():
    print(f"""{Fore.MAGENTA}
       ==----------     ---------:      
       =-:-:::::--:     -::::::--:      
       --:+     -::     -:     =-:      
      +=-:=     -::     ::     =-:=     
      ::::::::::::::::::::     =-:+     
      ::                       =-:=     
      ::                       =-:=     
      ::--=====================--:---   
       --:-                       -::   
       =-:+                       -::   
       =-:+                       -:-   
       =-:+     -::-----------::::::-   
       =-:+     -::     ::     =-:=     
       =-:+     -::     ::     =-:=     
       =-:+     -:-     ::     =-:      
       =-:+     -::     ::     --:      
       =-:=++===-:-     ::-====--:      
       --::::::::::     ::::::::::    {Fore.LIGHTMAGENTA_EX}
       https://github.com/H-zz-H69
              Made by H-zz-H  
    """)

async def anim(event):
    for frame in itertools.cycle(['|', '/', '-', '\\']):
        if event.is_set():
            break
        print(f"{Fore.LIGHTMAGENTA_EX}\rWait for the animation to begin: {frame}", end='', flush=True)
        await asyncio.sleep(0.2)
    print("\r", end='', flush=True)  

async def join_game(game_pin, username):
    client = KahootClient()
    try:
        await client.join_game(game_pin, username)
        print(f"{Fore.LIGHTMAGENTA_EX}Successfully joined game as {username}")
    except Exception as e:
        print(f"{Fore.RED}Error joining game as {username}: {e}")
    finally:
        print(f"{Fore.YELLOW}Finished attempting to join as {username}")

async def run_bots(game_pin, base_username, count):
    stop_event = asyncio.Event()
    animation_task = asyncio.create_task(anim(stop_event))
    
    tasks = [join_game(game_pin, f"{base_username}_{i+1}") for i in range(count)]
    await asyncio.gather(*tasks)
    
    stop_event.set()
    await animation_task

def main():
    if len(sys.argv) < 4:
        logo()
        print(f"{Fore.MAGENTA}Usage: script.py (gamepin) (username) (bot count)")
        sys.exit(1)

    game_pin = sys.argv[1]
    base_username = sys.argv[2]
    try:
        bot_count = int(sys.argv[3])
        if bot_count <= 0:
            raise ValueError
    except ValueError:
        print(f"{Fore.RED}Error: Bot count must be more than 0.")
        sys.exit(1)

    logo()
    print(f"{Fore.MAGENTA}Running {bot_count} bots for game PIN: {game_pin}")
    print(f"{Fore.MAGENTA}Using base username: {base_username}")
    
    asyncio.run(run_bots(game_pin, base_username, bot_count))

main()