import org.junit.jupiter.api.Test;
import uk.me.martinwestacott.DaySix;

import static org.junit.jupiter.api.Assertions.*;

public class DaySixTests {

    @Test
    public void findStartOfPacketMarker(){
        var ops = new DaySix();

        var result = ops.findStartOfPacketMarker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4);
        assertEquals(5, result);
    }

    @Test
    public void findStartOfPacketMarker_two(){
        var ops = new DaySix();

        var result = ops.findStartOfPacketMarker("nppdvjthqldpwncqszvftbrmjlhg", 4);
        assertEquals(6, result);
    }

    @Test
    public void findStartOfPacketMarker_three(){
        var ops = new DaySix();

        var result = ops.findStartOfPacketMarker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4);
        assertEquals(10, result);
    }

    @Test
    public void isUnique_returnsTrue(){
        var ops = new DaySix();
        assertTrue(ops.isUnique("abcd"));
    }

    @Test
    public void isUnique_returnsFalse(){
        var ops = new DaySix();
        assertFalse(ops.isUnique("abcb"));
    }

}
