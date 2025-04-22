# Blackjack
The popular multi-player card game, brought to you in a completely virtual format! 

## Description
Also known as "twenty-one", Blackjack pits each player against the dealer. Their task is to accumulate a hand of cards that totals as close to 21 as possible without exceeding 21. On their turn, players choose to either "HIT" (draw another card) or "STAY" (take no more cards). Once someone's hand exceeds 21, they automatically "BUST". Cards are totaled based on face value, where Jacks, Queens, and Kings are all worth 10, and Aces have a dynamic value of either 1 or 11. At the end of a round, all active players whose cards total higher than the dealer's win. If a player's hand is equal to the dealer's hand, there is a tie (neither of them wins).

> [!NOTE]
The rules of this Blackjack game have been modified as per the project's instructions. For example, in normal Blackjack a dealer must "HIT" on any hand below 17. In this implementation, they stop hitting once their hand is greater than or equal to 16. 

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

1. Press SPACE to begin the game. 
2. Enter the number of players (1–3) in the terminal when prompted. (GUI will remain frozen until terminal input is received. An error will also be thrown for non-integer inputs.)
3. Use the buttons in the game window to:
  - **Hit**: Draw a new card
  - **Stay**: End your turn
4. Try to beat the dealer without going over 21!

---

## Notes

- The game is built using `pygame-ce` for compatibility with Python 3.13+.
---

## Screenshots

![Screenshot 2025-04-21 at 9 51 55 PM](https://github.com/user-attachments/assets/408c7854-fff4-4aa6-9b27-87acb24ee3d5)
![Screenshot 2025-04-21 at 9 52 33 PM](https://github.com/user-attachments/assets/5408761d-1086-4ab9-b2d8-8a6e5251821f)
![Screenshot 2025-04-21 at 9 52 44 PM](https://github.com/user-attachments/assets/81a39bbf-75c1-46cf-87d5-a81fdfc74655)
![Screenshot 2025-04-21 at 9 53 28 PM](https://github.com/user-attachments/assets/4de20017-9a4b-44cd-9ec3-76dfbaef6fa2)

## Future Development
- Receive user input like the number of players and the player names in the GUI
- Implement the addition of AI players, aside from the dealer
- Improve the GUI's graphics and display of round and win counters
- Implement an AI card counting feature
