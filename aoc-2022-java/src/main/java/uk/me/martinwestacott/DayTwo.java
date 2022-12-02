package uk.me.martinwestacott;

import java.util.List;

public class DayTwo {

    public enum RPS {
        Rock,
        Paper,
        Scissors
    }

    public enum WinState {
        Win,
        Lose,
        Draw
    }

    public record GameRound(RPS opponent, RPS player) {
    }

    public record GameStrategy(RPS opponent, WinState state) {
    }


    public GameRound decodeRound(String round) {
        var plays = round.split(" ");
        return new GameRound(decodePlay(plays[0]), decodePlay(plays[1]));
    }

    public GameStrategy decodeStrategy(String round) {
        var plays = round.split(" ");
        return new GameStrategy(decodePlay(plays[0]), decodeWinState(plays[1]));
    }

    private WinState decodeWinState(String state) {
        switch (state.toUpperCase()) {
            case "X":
                return WinState.Lose;
            case "Y":
                return WinState.Draw;
            case "Z":
                return WinState.Win;
        }
        throw new RuntimeException("Unable to Decode win state: " + state);
    }

    private RPS decodePlay(String play) {

        switch (play.toUpperCase()) {
            case "A", "X":
                return RPS.Rock;
            case "B", "Y":
                return RPS.Paper;
            case "C", "Z":
                return RPS.Scissors;
        }
        throw new RuntimeException("Unable to Decode play: " + play);
    }

    public WinState calcWinState(GameRound round) {
        if (round.opponent == round.player) {
            return WinState.Draw;
        }

        if (round.player == RPS.Rock && round.opponent == RPS.Scissors) {
            return WinState.Win;
        }

        if (round.player == RPS.Scissors && round.opponent == RPS.Paper) {
            return WinState.Win;
        }

        if (round.player == RPS.Paper && round.opponent == RPS.Rock) {
            return WinState.Win;
        }

        return WinState.Lose;
    }

    public RPS calcPlayerMove(GameStrategy strategy) {
        if (strategy.state == WinState.Draw) {
            return strategy.opponent;
        }

        if (strategy.state == WinState.Win) {
            switch (strategy.opponent) {
                case Rock:
                    return RPS.Paper;
                case Paper:
                    return RPS.Scissors;
                case Scissors:
                    return RPS.Rock;
            }
        }

        RPS loseOp = RPS.Rock;
        switch (strategy.opponent) {
            case Rock:
                loseOp = RPS.Scissors;
                break;
            case Paper:
                loseOp = RPS.Rock;
                break;
            case Scissors:
                loseOp = RPS.Paper;
                break;
        }
        return loseOp;
    }


    public int calcScore(GameRound round) {
        return calcScore(round.player, calcWinState(round));
    }

    public int calcScore(RPS play, WinState state) {
        return getScore(play) + getScore(state);
    }

    private int getScore(RPS value) {
        int score = 0;
        switch (value) {
            case Rock:
                score = 1;
                break;
            case Paper:
                score = 2;
                break;
            case Scissors:
                score = 3;
                break;
        }
        return score;
    }

    private int getScore(WinState value) {
        int score = 0;
        switch (value) {
            case Lose:
                score = 0;
                break;
            case Draw:
                score = 3;
                break;
            case Win:
                score = 6;
                break;
        }
        return score;
    }


    public static void main(String[] args) {

        var data = CommonUtils.readData(
                CommonUtils.getResourceFilePath("day2-input.txt")
        );
        var ops = new DayTwo();

        Integer result = ops.calcPartOneResult(data);
        System.out.println("Totals Score: " + result);

        Integer resultPart2 = ops.calcPartTwoResult(data);
        System.out.println("Totals Score Part 2: " + resultPart2);
    }

    public Integer calcPartTwoResult(List<String> data) {
        var result = data.stream()
                .map(str -> decodeStrategy(str))
                .map(gameStrategy -> calcScore(calcPlayerMove(gameStrategy), gameStrategy.state))
                .reduce(Integer::sum)
                .orElse(0);
        return result;
    }

    public Integer calcPartOneResult(List<String> data) {

        var result = data.stream()
                .map(str -> decodeRound(str))
                .map(gameRound -> calcScore(gameRound))
                .reduce(Integer::sum)
                .orElse(0);
        return result;
    }
}
