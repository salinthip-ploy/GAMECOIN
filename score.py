class Score:
    def __init__(self):
        self.high_score = self.load_high_score()

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except:
            return 0

    def save_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
            with open("high_score.txt", "w") as file:
                file.write(str(score))
