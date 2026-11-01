from dataclasses import dataclass
from enum import Enum
from typing import Annotated

from slimconfig import Output


class Tool(Enum):
    COMPUTE_STANDINGS = "compute_standings"


class Task(Enum):
    AUDIT_LEAGUE_STANDINGS = "audit-league-standings"


@dataclass
class Match(Output):
    home: Annotated[str, "Home team id"]
    away: Annotated[str, "Away team id"]
    home_score: Annotated[int, "Non-negative home score"]
    away_score: Annotated[int, "Non-negative away score"]


@dataclass
class StandingsInput(Output):
    teams: Annotated[list[str], "Two to twelve unique team ids"]
    matches: Annotated[list[Match], "At most one hundred completed matches"]
    win_points: Annotated[int, "Points for a win"]
    draw_points: Annotated[int, "Points for a draw"]
    loss_points: Annotated[int, "Points for a loss"]


@dataclass
class Standing(Output):
    rank: Annotated[int, "One-based ordinal after all tie-breaks"]
    team: Annotated[str, "Team id"]
    played: Annotated[int, "Matches played"]
    points: Annotated[int, "Competition points"]
    goals_for: Annotated[int, "Goals scored"]
    goals_against: Annotated[int, "Goals conceded"]
    goal_difference: Annotated[int, "Goals for minus goals against"]


@dataclass
class StandingsOutput(Output):
    standings: Annotated[list[Standing], "Teams sorted by points, goal difference, goals for, then team id"]


TOOLS = {Tool.COMPUTE_STANDINGS: (StandingsInput, StandingsOutput)}
TASKS = {Task.AUDIT_LEAGUE_STANDINGS: (StandingsInput, StandingsOutput)}
