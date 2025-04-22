# Blackjack
The popular (multiplayer?) card game, brought to you in a completely virtual format! 

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
![Screenshot 2025-04-21 at 8 16 05 PM](https://github.com/user-attachments/assets/6a386bff-c549-4733-932a-56aa2777bfb8)

![Screenshot 2025-04-21 at 8 16 13 PM](https://github.com/user-attachments/assets/76ffff2c-3d31-42d3-8a2d-8b5bd83ec1a0)



