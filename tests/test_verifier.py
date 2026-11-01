from slimconfig import build_output

import verifier
from contract import StandingsInput, StandingsOutput


def verdict(given, made):
    return verifier.verify_task(
        "audit-league-standings", build_output(given, StandingsInput), build_output(made, StandingsOutput), None, "."
    )


def test_table_and_tiebreaks():
    given = {
        "teams": ["a", "b", "c"],
        "matches": [
            {"home": "a", "away": "b", "home_score": 1, "away_score": 0},
            {"home": "c", "away": "a", "home_score": 2, "away_score": 1},
        ],
        "win_points": 3,
        "draw_points": 1,
        "loss_points": 0,
    }
    made = {
        "standings": [
            {
                "rank": 1,
                "team": "c",
                "played": 1,
                "points": 3,
                "goals_for": 2,
                "goals_against": 1,
                "goal_difference": 1,
            },
            {
                "rank": 2,
                "team": "a",
                "played": 2,
                "points": 3,
                "goals_for": 2,
                "goals_against": 2,
                "goal_difference": 0,
            },
            {
                "rank": 3,
                "team": "b",
                "played": 1,
                "points": 0,
                "goals_for": 0,
                "goals_against": 1,
                "goal_difference": -1,
            },
        ]
    }
    assert verdict(given, made)["valid"] is True
    assert verdict(given, {"standings": list(reversed(made["standings"]))})["valid"] is False


def test_empty_season_and_bad_match():
    given = {"teams": ["a", "b"], "matches": [], "win_points": 3, "draw_points": 1, "loss_points": 0}
    made = {
        "standings": [
            {
                "rank": 1,
                "team": "a",
                "played": 0,
                "points": 0,
                "goals_for": 0,
                "goals_against": 0,
                "goal_difference": 0,
            },
            {
                "rank": 2,
                "team": "b",
                "played": 0,
                "points": 0,
                "goals_for": 0,
                "goals_against": 0,
                "goal_difference": 0,
            },
        ]
    }
    assert verdict(given, made)["valid"] is True
    bad = build_output(
        given | {"matches": [{"home": "a", "away": "a", "home_score": 0, "away_score": 0}]}, StandingsInput
    )
    assert verifier.verify_input("compute_standings", bad)["valid"] is False
