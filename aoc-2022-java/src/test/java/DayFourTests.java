import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import uk.me.martinwestacott.DayFour;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class DayFourTests {

    @Test
    public void createSection() {
        DayFour ops = new DayFour();

        var section = ops.createSection("2-4,3-6");

        assertEquals(3, section.sectionA().size());

        assertEquals(4, section.sectionB().size());
    }


    @Test
    public void isFullyContainedWithin_WhenBConatinedInA_returnsTrue() {
        DayFour ops = new DayFour();

        var section = ops.createSection("2-8,3-7");

        Assertions.assertTrue(ops.isFullyContainedWithin(section));
    }

    @Test
    public void isFullyContainedWithin_WhenAConatinedInB_returnsTrue() {
        DayFour ops = new DayFour();

        var section = ops.createSection("6-6,4-6");

        Assertions.assertTrue(ops.isFullyContainedWithin(section));
    }

    @Test
    public void isFullyContainedWithin_WhenNotContained_returnsFalse() {
        DayFour ops = new DayFour();

        var section = ops.createSection("2-4,6-8");

        Assertions.assertFalse(ops.isFullyContainedWithin(section));
    }

    @Test
    public void getContainedCount (){
        var data = Arrays.asList(
                "2-4,6-8",
                "2-3,4-5",
                "5-7,7-9",
                "2-8,3-7",
                "6-6,4-6",
                "2-6,4-8");

        DayFour ops = new DayFour();

        Assertions.assertEquals(2,ops.getContainedCount(data));

    }

    @Test
    public void getIntersectedCount (){
        var data = Arrays.asList(
                "2-4,6-8",
                "2-3,4-5",
                "5-7,7-9",
                "2-8,3-7",
                "6-6,4-6",
                "2-6,4-8");

        DayFour ops = new DayFour();

        Assertions.assertEquals(4,ops.getIntersectedCount(data));

    }


}
