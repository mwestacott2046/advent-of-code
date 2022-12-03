import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import uk.me.martinwestacott.aoc.day1.DayOne;

import java.util.Arrays;

public class DayOneTests {

    @Test
    public void countIncreases(){
        var data = Arrays.asList(199, 200, 208, 210, 200, 207, 240, 269, 260, 263);

        Assertions.assertEquals(7,DayOne.countIncreases(data));
    }

    @Test
    public void countWindowedIncreases(){
        var data = Arrays.asList(199, 200, 208, 210, 200, 207, 240, 269, 260, 263);

        Assertions.assertEquals(5,DayOne.countWindowedIncreases(data,3));
    }

}
