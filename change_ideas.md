# Ideas for future changes
## Modifications
### Inventory
- Add options to display `flies`, `locations`.
- Revamp system for storing data about `fish` (name, rarity, crafting output). Maybe make a class for fish?
### Main menu
- Only display options that are possible for player (e.g., no travel option if player only has one `location` unlocked).
### Fishing
- Move **Change fly** option from main menu. Options in menu: [RETURN] to cast, "A" to change fly, "B" for powerups, and "C" to leave.
### Market
- Variability in sell-prices (proportional or within a range).
- Location-based sell-price variability.
## Additions
### Market
What if it was inspired by the Pike Place Market? Idk how but that'd be cool.
#### Buying
- Randomly determine what is in stock (location-based).
- Can buy other fish?
### Powerups
- Figure out powerup merchant
- Add powerups option to `go_fishing`.
- **Sake**: increases "fishing power" (`odds`?).
- **Coffee grounds**: throw into the water to make fish faster, decreases `cast_time` (make sure can't go below zero).
- **Gold flakes**: increase fish tier by 1 (allows super rare catches).
- **Dissolving melatonin**: makes fish sleepy (more able to catch with a net?).
### Crafting
- Can craft **fish** into other items (**flies**, **powerups**, etc.).
- Fish sold by the Fishmonger have a chance to contain special materials.
### Minigames
#### Dangerous fish
- May need items to defend against some fish.
- If you're farming for something and keep catching small but dangerous fish, I don't want you to have to play a minigame over and over. Maybe I could do something similar to "He is Coming" where it's an autobattler and you can just skip the encounter and get the outcomes.
#### Go Fish
- You receive around 5 fish from the current location pool, then trade off asking each other for fish. If the other player does not have a matching fish, do one **Fishing** cycle.
### Story
My vision for the point-and-click version has a horror undertone involving monsters of the deep and such. I'd like to incorporate some of that here.
#### Locations
I currently have two locations: **The Dells** and **Chicago**. However, it might be cool to have different locations around a certain area (a river, a lake), so you can still return to the same **Market** and develop relationships (or at least familiarity) with the NPCs. 
#### NPCs
- **The Fisherman**: 
  - This character was the main inspiration for this game. I had an idea for a diaglogue-based RPG with three characters who would die soon. My favorite was the fisherman, so I decided to design a game specifically for him.
  - The Fisherman is the father or father-figure of the main character.
  - He has a sort of disease-like relationship to fishing, something something horror elements. The activity takes something from him, and he passes this down to the MC (something something cancer allegory).
- **The Fishmonger**
  - Can buy **fish** from him, which seems useless at first, but these fish have a chance to contain special crafting materials.
  - Secret: can eventually unlock the ability to play **Go Fish** with him. I'll need to make the Fishmonger interesting enough to encourage players to interact with him.
  - Taking design inspo from the underscores album would be funny.
- **The Drink Lady**
  - This is a filler name for an NPC who will sell **Sake** and **Coffee grounds**, and maybe some other powerups. I need to figure out who and how I want her to be.
- Other market NPCs.

Would need to be location-based.
### Minigames
- Go-fish (maybe could play with the Fishmonger).
- A dungeon-crawler (it would be funny).
# Next steps
## Market
- Clean up code for selling (simplify variables, revisit organization)
## Powerups
- Add **Sake** and **Coffee grounds**.