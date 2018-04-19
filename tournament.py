

def setUpTournament(schools):
  for team1 in schools:
    for team2 in schools:
      if (team2 != team1):
        print(team1," vs. ",team2)
    print("")


def setUpWackyTournament(schools):
  for s in schools:
    for s in schools:
        print(s," vs. ",s)
    print("")


if __name__=="__main__":
  setUpWackyTournament(["UCSB","UCSD","Stanford","Cal Poly"])
