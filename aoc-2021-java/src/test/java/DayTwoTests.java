import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import uk.me.martinwestacott.aoc.day1.DayTwo;

import java.util.ArrayList;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class DayTwoTests {

    @Test
    public void parseCommand() {
        var ops = new DayTwo();

        var cmd = ops.parseCommand("forward 5");

        assertEquals("forward", cmd.direction());
        assertEquals(5, cmd.distance());
    }


    @Test
    public void processCommand_forward() {
        var ops = new DayTwo();
        var startPos = new DayTwo.Position(10, 10);
        var result = ops.processCommand(new DayTwo.Command("forward", 5), startPos);

        assertEquals(15, result.horizontal());
        assertEquals(10, result.depth());
    }

    @Test
    public void processCommand_up() {
        var ops = new DayTwo();
        var startPos = new DayTwo.Position(10, 10);
        var result = ops.processCommand(new DayTwo.Command("up", 5), startPos);

        assertEquals(10, result.horizontal());
        assertEquals(5, result.depth());
    }

    @Test
    public void processCommand_down() {
        var ops = new DayTwo();
        var startPos = new DayTwo.Position(10, 10);
        var result = ops.processCommand(new DayTwo.Command("down", 5), startPos);

        assertEquals(10, result.horizontal());
        assertEquals(15, result.depth());
    }

    @Test
    public void moveSub() {

        var moves = new ArrayList<DayTwo.Command>();

        moves.add(new DayTwo.Command("forward",5));
        moves.add(new DayTwo.Command("down",5));
        moves.add(new DayTwo.Command("forward",8));
        moves.add(new DayTwo.Command("up",3));
        moves.add(new DayTwo.Command("down",8));
        moves.add(new DayTwo.Command("forward",2));

        var ops = new DayTwo();
        var position = ops.moveSub(moves);

        assertEquals(15, position.horizontal());
        assertEquals(10, position.depth());
    }

    @Test
    public void moveSubWithAim() {

        var moves = new ArrayList<DayTwo.Command>();

        moves.add(new DayTwo.Command("forward",5));
        moves.add(new DayTwo.Command("down",5));
        moves.add(new DayTwo.Command("forward",8));
        moves.add(new DayTwo.Command("up",3));
        moves.add(new DayTwo.Command("down",8));
        moves.add(new DayTwo.Command("forward",2));

        var ops = new DayTwo();
        var position = ops.moveSubWithAim(moves);

        assertEquals(15, position.horizontal());
        assertEquals(60, position.depth());
    }
}
