import org.junit.jupiter.api.Test;
import uk.me.martinwestacott.DayThree;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;


public class DayThreeTests {

    public static final List<String> SMALL_TEST_DATA = Arrays.asList(
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
    );

    @Test
    public void splitBag() {

        String bag = "vJrwpWtwJgWrhcsFMMfFFhFp";
        var ops = new DayThree();
        var result = ops.splitBag(bag);

        assertEquals("vJrwpWtwJgWr", result.get(0));
        assertEquals("hcsFMMfFFhFp", result.get(1));
    }

    @Test
    public void findFirstDuplicate_returnsItem() {
        var ops = new DayThree();
        var result = ops.findFirstDuplicate("vJrwpWtwJgWr", "hcsFMMfFFhFp");

        assertEquals("p", result);
    }

    @Test
    public void findFirstDuplicate_returnsEmptyString() {
        var ops = new DayThree();
        var result = ops.findFirstDuplicate("aaaaa", "bbccddee");

        assertEquals("", result);
    }

    @Test
    public void getReorganisationPriorities() {

        var ops = new DayThree();
        assertEquals(157, ops.getReorganisationPriorities(SMALL_TEST_DATA));
    }


    @Test
    public void getPriority_a_returns_1() {
        var ops = new DayThree();
        var result = ops.getPriority("a");

        assertEquals(1, result);
    }

    @Test
    public void getPriority_z_returns_26() {
        var ops = new DayThree();
        var result = ops.getPriority("z");

        assertEquals(26, result);
    }

    @Test
    public void getPriority_a_returns_27() {
        var ops = new DayThree();
        var result = ops.getPriority("A");

        assertEquals(27, result);
    }

    @Test
    public void getPriority_Z_returns_52() {
        var ops = new DayThree();
        var result = ops.getPriority("Z");

        assertEquals(52, result);
    }

    @Test
    public void groupBags() {
        var ops = new DayThree();
        var result = ops.groupBags(SMALL_TEST_DATA, 3);

        assertEquals(2, result.size());
        assertEquals(3, result.get(0).size());
        assertEquals(3, result.get(1).size());

    }


    @Test
    public void getGroupBadgePriorities() {
        var ops = new DayThree();
        assertEquals(70, ops.getGroupBadgePriorities(SMALL_TEST_DATA));
    }

    @Test
    public void findBadge() {
        var ops = new DayThree();
        List<String> bags = Arrays.asList(
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg"
        );
        String result = ops.findBadge(bags);

        assertEquals("r", result);
    }

}
