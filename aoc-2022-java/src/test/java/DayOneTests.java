import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import uk.me.martinwestacott.DayOne;

import java.util.Arrays;

public class DayOneTests {

    @Test
    public void getElfCalorieCounts(){
        var inputValues = Arrays.asList("1","2","3","","4","5","","6","7");

        var results= DayOne.getElfCalorieCounts(inputValues);

        Assertions.assertEquals(6, results.get(0));
        Assertions.assertEquals(9, results.get(1));
        Assertions.assertEquals(13, results.get(2));
    }

    @Test
    public void getTop3Sum(){
        var inputValues = Arrays.asList(10,20,101,30,40,100,2,66,303,707);

        var result= DayOne.getTop3Sum(inputValues);

        Assertions.assertEquals(1111, result);
    }


    @Test
    public void getMaxCalories(){
        var inputValues = Arrays.asList(10,707,20,101,30,40,100,2,66,303);

        var result= DayOne.getMaxCalories(inputValues);

        Assertions.assertEquals(707, result);
    }

}
