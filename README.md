# Blackjack
The popular (multiplayer?) card game, brought to you in a completely virtual format! 

## Description
Also known as "twenty-one", Blackjack pits each player against the dealer. Their task is to accumulate a hand of cards that totals as close to 21 as possible without exceeding 21. On their turn, players choose to either "HIT" (draw another card) or "STAY" (take no more cards). Once someone's hand exceeds 21, they automatically "BUST". Cards are totaled based on face value, where Jacks, Queens, and Kings are all worth 10, and Aces have a dynamic value of either 1 or 11. At the end of a round, all active players whose cards total higher than the dealer's win. If a player's hand is equal to the dealer's hand, there is a tie (neither of them wins).

## Game Features

## Getting Started

1. Create and activate your virtual environemnt (if applicable)like so:
`cd ~ `
`python3 -m venv myenv`
`source ~/myenv/bin/activate`

2. Clone this repository
`git clone git@github.com:nhasan6/Blackjack.git`

3. Go into cloned repo and install dependencies

`cd Blackjack `
`pip3 install -e .`

4. Run as a package like so:

`Cd ..`
`python -m Blackjack.main`

5. Go to terminal and enter # players



6. Decide if you want to Hit or Stay. You’ll get a card and see how it goes!


## Controls

Click on HIT to draw another card.
Click on STAY to draw no more cards (ends your turn early).



# Blackjack
The popular (multiplayer?) card game, brought to you in a completely virtual format!


Have fun and good luck beating the dealer! 🎲


## Description
Also known as "twenty-one", Blackjack pits each player against the dealer. Their task is to accumulate a hand of cards that totals as close to 21 as possible without exceeding 21. On their turn, players choose to either "HIT" (draw another card) or "STAY" (take no more cards). Once someone's hand exceeds 21, they automatically "BUST". Cards are totaled based on face value, where Jacks, Queens, and Kings are all worth 10, and Aces have a dynamic value of either 1 or 11. At the end of a round, all active players whose cards total higher than the dealer's win. If a player's hand is equal to the dealer's hand, there is a tie (neither of them wins).


## Getting Started


### 1. Create and Activate a Virtual Environment (Optional but Recommended)


```bash
cd ~
python3 -m venv myenv
source ~/myenv/bin/activate
```


### 2. Clone the Repository


```bash
git clone git@github.com:nhasan6/Blackjack.git
```


### 3. Navigate into the Project Folder and Install Dependencies


```bash
cd Blackjack
pip install -e .
```


> `-e .` installs the project in editable mode, useful for development.


### 4. Run the Game


Navigate one directory **above** the `Blackjack` folder and run the game as a package:


```bash
cd ..
python -m Blackjack.main
```


---


## Gameplay Instructions


1. Enter the number of players (1–3) in the terminal when prompted.
2. Use the buttons in the game window to:
  - **Hit**: Draw a new card
  - **Stay**: End your turn
3. Try to beat the dealer without going over 21!

---

## Notes

- The game is built using `pygame-ce` for compatibility with Python 3.13+.
- Works best in fullscreen or high-resolution display.


---


## Screenshots
