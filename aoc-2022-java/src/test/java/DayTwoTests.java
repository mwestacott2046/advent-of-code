import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import uk.me.martinwestacott.DayTwo;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class DayTwoTests {

    @Test
    public void decodePlay_Rock_Paper() {
        var decoder = new DayTwo();

        var result = decoder.decodeRound("A Y");

        assertEquals(DayTwo.RPS.Rock, result.opponent());
        assertEquals(DayTwo.RPS.Paper, result.player());
    }

    @Test
    public void decodePlay_Paper_Scissors() {
        var decoder = new DayTwo();

        var result = decoder.decodeRound("B Z");

        assertEquals(DayTwo.RPS.Paper, result.opponent());
        assertEquals(DayTwo.RPS.Scissors, result.player());
    }

    @Test
    public void decodePlay_Scissors_Rock() {
        var decoder = new DayTwo();

        var result = decoder.decodeRound("C X");

        assertEquals(DayTwo.RPS.Scissors, result.opponent());
        assertEquals(DayTwo.RPS.Rock, result.player());
    }

    @ParameterizedTest
    @MethodSource("calcWinStateArgs")
    public void calcWinState(DayTwo.RPS player, DayTwo.RPS opponent, DayTwo.WinState expectedState) {
        var round = new DayTwo.GameRound(opponent, player);

        var decoder = new DayTwo();
        var result = decoder.calcWinState(round);

        assertEquals(expectedState, result);
    }


    private static Stream<Arguments> calcWinStateArgs() {
        return Stream.of(
                Arguments.of(DayTwo.RPS.Rock, DayTwo.RPS.Scissors, DayTwo.WinState.Win),
                Arguments.of(DayTwo.RPS.Rock, DayTwo.RPS.Rock, DayTwo.WinState.Draw),
                Arguments.of(DayTwo.RPS.Rock, DayTwo.RPS.Paper, DayTwo.WinState.Lose),

                Arguments.of(DayTwo.RPS.Scissors, DayTwo.RPS.Scissors, DayTwo.WinState.Draw),
                Arguments.of(DayTwo.RPS.Scissors, DayTwo.RPS.Rock, DayTwo.WinState.Lose),
                Arguments.of(DayTwo.RPS.Scissors, DayTwo.RPS.Paper, DayTwo.WinState.Win),

                Arguments.of(DayTwo.RPS.Paper, DayTwo.RPS.Scissors, DayTwo.WinState.Lose),
                Arguments.of(DayTwo.RPS.Paper, DayTwo.RPS.Rock, DayTwo.WinState.Win),
                Arguments.of(DayTwo.RPS.Paper, DayTwo.RPS.Paper, DayTwo.WinState.Draw)
        );
    }


    @ParameterizedTest
    @MethodSource("calcScoreArgs")
    public void calcScore(DayTwo.RPS player, DayTwo.RPS opponent, int expectedScore) {
        var round = new DayTwo.GameRound(opponent, player);

        var decoder = new DayTwo();
        var result = decoder.calcScore(round);

        assertEquals(expectedScore, result);
    }

    private static Stream<Arguments> calcScoreArgs() {
        return Stream.of(
                Arguments.of(DayTwo.RPS.Rock, DayTwo.RPS.Scissors, 7),
                Arguments.of(DayTwo.RPS.Rock, DayTwo.RPS.Rock, 4),
                Arguments.of(DayTwo.RPS.Rock, DayTwo.RPS.Paper, 1),

                Arguments.of(DayTwo.RPS.Scissors, DayTwo.RPS.Scissors, 6),
                Arguments.of(DayTwo.RPS.Scissors, DayTwo.RPS.Rock, 3),
                Arguments.of(DayTwo.RPS.Scissors, DayTwo.RPS.Paper, 9),

                Arguments.of(DayTwo.RPS.Paper, DayTwo.RPS.Scissors, 2),
                Arguments.of(DayTwo.RPS.Paper, DayTwo.RPS.Rock, 8),
                Arguments.of(DayTwo.RPS.Paper, DayTwo.RPS.Paper, 5)
        );
    }

    @Test
    public void calcPartOneResult() {
        var ops = new DayTwo();

        List<String> data = Arrays.asList("A Y", "B X", "C Z");
        var result = ops.calcPartOneResult(data);

        assertEquals(15, result);
    }


    @Test
    public void decodeStrategy_rock_win() {
        var decoder = new DayTwo();
        var result = decoder.decodeStrategy("A Z");

        assertEquals(DayTwo.WinState.Win, result.state());
        assertEquals(DayTwo.RPS.Rock, result.opponent());
    }

    @Test
    public void decodeStrategy_paper_draw() {
        var decoder = new DayTwo();
        var result = decoder.decodeStrategy("B Y");

        assertEquals(DayTwo.WinState.Draw, result.state());
        assertEquals(DayTwo.RPS.Paper, result.opponent());
    }

    @Test
    public void decodeStrategy_scissors_lose() {
        var decoder = new DayTwo();
        var result = decoder.decodeStrategy("C X");

        assertEquals(DayTwo.WinState.Lose, result.state());
        assertEquals(DayTwo.RPS.Scissors, result.opponent());
    }

    @ParameterizedTest
    @MethodSource("calcPlayerMoveArgs")
    public void calcPlayerMove(DayTwo.RPS opponentMove, DayTwo.WinState strategy, DayTwo.RPS expectedMove) {
        var decoder = new DayTwo();
        var result = decoder.calcPlayerMove(new DayTwo.GameStrategy(opponentMove, strategy));

        assertEquals(expectedMove, result);
    }

    private static Stream<Arguments> calcPlayerMoveArgs() {
        return Stream.of(
                Arguments.of(DayTwo.RPS.Scissors, DayTwo.WinState.Win, DayTwo.RPS.Rock),
                Arguments.of(DayTwo.RPS.Scissors, DayTwo.WinState.Draw, DayTwo.RPS.Scissors),
                Arguments.of(DayTwo.RPS.Scissors, DayTwo.WinState.Lose, DayTwo.RPS.Paper),

                Arguments.of(DayTwo.RPS.Paper, DayTwo.WinState.Win, DayTwo.RPS.Scissors),
                Arguments.of(DayTwo.RPS.Paper, DayTwo.WinState.Draw, DayTwo.RPS.Paper),
                Arguments.of(DayTwo.RPS.Paper, DayTwo.WinState.Lose, DayTwo.RPS.Rock),

                Arguments.of(DayTwo.RPS.Rock, DayTwo.WinState.Lose, DayTwo.RPS.Scissors),
                Arguments.of(DayTwo.RPS.Rock, DayTwo.WinState.Draw, DayTwo.RPS.Rock),
                Arguments.of(DayTwo.RPS.Rock, DayTwo.WinState.Win, DayTwo.RPS.Paper)
        );
    }

    @Test
    public void calcPartTwoResult() {
        var ops = new DayTwo();

        List<String> data = Arrays.asList("A Y", "B X", "C Z");
        var result = ops.calcPartTwoResult(data);

        assertEquals(12, result);
    }

}
