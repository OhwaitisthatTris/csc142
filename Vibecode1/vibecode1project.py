class Player:
    def __init__(self, name, number, position, team_abbrev):
        self.name = name
        self.number = number
        self.position = position
        self.team_abbrev = team_abbrev

    def __repr__(self):
        return f"{self.team_abbrev} | {self.name} #{self.number} ({self.position})"


class Roster:
    def __init__(self, team_name, team_abbrev):
        self.team_name = team_name
        self.team_abbrev = team_abbrev
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def list_players(self):
        for p in self.players:
            print(p)

    def get_by_position(self, position):
        return [p for p in self.players if p.position == position]




class AlbrightSoftball(Roster):
    def __init__(self):
        super().__init__("Albright College", "ALB")

    
        self.add_player(Player("Player A", 12, "LF", self.team_abbrev))
        self.add_player(Player("Player B", 7, "CF", self.team_abbrev))
        self.add_player(Player("Player C", 3, "RF", self.team_abbrev))
        self.add_player(Player("Player D", 21, "1B", self.team_abbrev))
        self.add_player(Player("Player E", 10, "2B", self.team_abbrev))
        self.add_player(Player("Player F", 5, "SS", self.team_abbrev))
        self.add_player(Player("Player G", 18, "3B", self.team_abbrev))
        self.add_player(Player("Player H", 2, "C", self.team_abbrev))
        self.add_player(Player("Player I", 14, "P", self.team_abbrev))


class AlverniaSoftball(Roster):
    def __init__(self):
        super().__init__("Alvernia University", "ALV")

        self.add_player(Player("Player J", 9, "LF", self.team_abbrev))
        self.add_player(Player("Player K", 4, "CF", self.team_abbrev))
        self.add_player(Player("Player L", 11, "RF", self.team_abbrev))
        self.add_player(Player("Player M", 22, "1B", self.team_abbrev))
        self.add_player(Player("Player N", 6, "2B", self.team_abbrev))
        self.add_player(Player("Player O", 8, "SS", self.team_abbrev))
        self.add_player(Player("Player P", 15, "3B", self.team_abbrev))
        self.add_player(Player("Player Q", 1, "C", self.team_abbrev))
        self.add_player(Player("Player R", 16, "P", self.team_abbrev))


def main():
    alb = AlbrightSoftball()
    alv = AlverniaSoftball()

    print("\n--- ALB Batting Order ---")
    alb.list_players()

    print("\n--- ALV Fielding Positions ---")
    alv.list_players()

if __name__ == "__main__":
    main()

import random

# -----------------------------------------
# Base Classes
# -----------------------------------------

class Player:
    def __init__(self, name, number, position, team_abbrev):
        self.name = name
        self.number = number
        self.position = position
        self.team_abbrev = team_abbrev

    def __repr__(self):
        return f"{self.team_abbrev} | {self.name} #{self.number} ({self.position})"


class Roster:
    def __init__(self, team_name, team_abbrev):
        self.team_name = team_name
        self.team_abbrev = team_abbrev
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def list_players(self):
        for p in self.players:
            print(p)

    def get_batting_order(self):
        return self.players[:]  # simple 1–9 order


# -----------------------------------------
# Team Definitions
# -----------------------------------------

class AlbrightSoftball(Roster):
    def __init__(self):
        super().__init__("Albright College", "ALB")

        self.add_player(Player("Player A", 12, "LF", self.team_abbrev))
        self.add_player(Player("Player B", 7, "CF", self.team_abbrev))
        self.add_player(Player("Player C", 3, "RF", self.team_abbrev))
        self.add_player(Player("Player D", 21, "1B", self.team_abbrev))
        self.add_player(Player("Player E", 10, "2B", self.team_abbrev))
        self.add_player(Player("Player F", 5, "SS", self.team_abbrev))
        self.add_player(Player("Player G", 18, "3B", self.team_abbrev))
        self.add_player(Player("Player H", 2, "C", self.team_abbrev))
        self.add_player(Player("Player I", 14, "P", self.team_abbrev))


class AlverniaSoftball(Roster):
    def __init__(self):
        super().__init__("Alvernia University", "ALV")

        self.add_player(Player("Player J", 9, "LF", self.team_abbrev))
        self.add_player(Player("Player K", 4, "CF", self.team_abbrev))
        self.add_player(Player("Player L", 11, "RF", self.team_abbrev))
        self.add_player(Player("Player M", 22, "1B", self.team_abbrev))
        self.add_player(Player("Player N", 6, "2B", self.team_abbrev))
        self.add_player(Player("Player O", 8, "SS", self.team_abbrev))
        self.add_player(Player("Player P", 15, "3B", self.team_abbrev))
        self.add_player(Player("Player Q", 1, "C", self.team_abbrev))
        self.add_player(Player("Player R", 16, "P", self.team_abbrev))


# Pitch-by-Pitch Simulation


def simulate_at_bat(batter):
    balls = 0
    strikes = 0

    print(f"\nAt bat: {batter.name} #{batter.number} ({batter.position})")

    while True:
        pitch = random.choice(["strike", "ball", "foul", "inplay"])

        if pitch == "strike":
            strikes += 1
            print(f"Pitch: STRIKE ({strikes}-S, {balls}-B)")
            if strikes == 3:
                print("Strikeout!")
                return "out"

        elif pitch == "ball":
            balls += 1
            print(f"Pitch: BALL ({strikes}-S, {balls}-B)")
            if balls == 4:
                print("Walk!")
                return "walk"

        elif pitch == "foul":
            if strikes < 2:
                strikes += 1
            print(f"Pitch: FOUL ({strikes}-S, {balls}-B)")

        elif pitch == "inplay":
            result = random.choice(["out", "single"])
            if result == "out":
                print("Ball in play... OUT!")
                return "out"
            else:
                print("Ball in play... BASE HIT!")
                return "hit"


def simulate_half_inning(batting_team, fielding_team):
    batting_order = batting_team.get_batting_order()
    batter_index = 0
    outs = 0

    print("\n==============================")
    print(f"ALB batting vs ALV fielding")
    print("==============================")

    while outs < 3:
        batter = batting_order[batter_index]
        result = simulate_at_bat(batter)

        if result == "out":
            outs += 1
            print(f"Outs: {outs}")


        batter_index = (batter_index + 1) % len(batting_order)

    print("\nHalf-inning over. 3 outs recorded.")



def main():
    alb = AlbrightSoftball()
    alv = AlverniaSoftball()

    simulate_half_inning(alb, alv)


if __name__ == "__main__":
    main()
