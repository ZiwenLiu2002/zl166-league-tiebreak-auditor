from contract import Standing, StandingsOutput


def validate(value):
    teams = set(value.teams)
    if not 2 <= len(teams) == len(value.teams) <= 12 or len(value.matches) > 100:
        raise ValueError("invalid teams or match count")
    if min(value.win_points, value.draw_points, value.loss_points) < 0:
        raise ValueError("points must be non-negative")
    for match in value.matches:
        if (
            match.home == match.away
            or match.home not in teams
            or match.away not in teams
            or min(match.home_score, match.away_score) < 0
        ):
            raise ValueError("invalid match")


def compute_standings(value, workspace):
    validate(value)
    data = {team: [0, 0, 0, 0] for team in value.teams}
    for match in value.matches:
        home, away = data[match.home], data[match.away]
        home[0] += 1
        away[0] += 1
        home[2] += match.home_score
        home[3] += match.away_score
        away[2] += match.away_score
        away[3] += match.home_score
        if match.home_score > match.away_score:
            home[1] += value.win_points
            away[1] += value.loss_points
        elif match.home_score < match.away_score:
            away[1] += value.win_points
            home[1] += value.loss_points
        else:
            home[1] += value.draw_points
            away[1] += value.draw_points
    ordered = sorted(
        value.teams, key=lambda team: (-data[team][1], -(data[team][2] - data[team][3]), -data[team][2], team)
    )
    rows = [
        Standing(
            rank=index + 1,
            team=team,
            played=data[team][0],
            points=data[team][1],
            goals_for=data[team][2],
            goals_against=data[team][3],
            goal_difference=data[team][2] - data[team][3],
        )
        for index, team in enumerate(ordered)
    ]
    return StandingsOutput(standings=rows)
