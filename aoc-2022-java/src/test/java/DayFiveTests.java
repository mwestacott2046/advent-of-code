import org.junit.jupiter.api.Test;
import uk.me.martinwestacott.CommonUtils;
import uk.me.martinwestacott.DayFive;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

public class DayFiveTests {


    @Test
    public void decodeMove(){
        var ops = new DayFive();

        var result = ops.decodeMove("move 1 from 2 to 3");

        assertEquals(1, result.count());
        assertEquals(2, result.from());
        assertEquals(3, result.to());
    }



    @Test
    public void initialiseData (){
        var data = CommonUtils.readData(CommonUtils.getResourceFilePath("day5-test.txt"));

        var ops = new DayFive();
        var result = ops.loadInitialState(data);

        assertNotNull(result);

        result.crane().getStacks().forEach(stack ->  System.out.println(stack.toString()));

        assertEquals("N", result.crane().getStacks().get(0).pop());
        assertEquals("Z", result.crane().getStacks().get(0).pop());

        assertEquals("P", result.crane().getStacks().get(2).pop());

        assertEquals("D", result.crane().getStacks().get(1).pop());
        assertEquals("C", result.crane().getStacks().get(1).pop());
        assertEquals("M", result.crane().getStacks().get(1).pop());

    }

}
