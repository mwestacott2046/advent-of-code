package uk.me.martinwestacott.aoc.challanges;

import uk.me.martinwestacott.aoc.ResourceDataLoader;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.LongPredicate;
import java.util.stream.LongStream;

public class DayTwo {

    record RangePair(long start, long end) {
    }

    public static void main(String[] args) {
        String data = new ResourceDataLoader().getDataText("aoc-2025-day2.txt", false);

        if (!data.isEmpty()) {
            System.out.println("Part One Visits at zero: " + findInvalidIdSum(data, DayTwo::isInvalidDuplicateId));

            System.out.println("Part Two Visits at zero: " + findInvalidIdSum(data, DayTwo::isRepeatedPatternId));
        }
    }

    private static long findInvalidIdSum(String data, LongPredicate isInvalidDuplicateId) {

        List<Long> invalidIds = new ArrayList<>();

        String[] ranges = data.split(",");
        Arrays.stream(ranges)
                .map(DayTwo::getRangePair)
                .forEach(pair ->
                        invalidIds.addAll(findInvalidIds(pair, isInvalidDuplicateId))
                );

        return invalidIds.stream().mapToLong(Long::longValue).sum();
    }

    private static RangePair getRangePair(String range) {
        try {


            String[] rangeItems = range.split("-");
            long rangeStart = Long.parseLong(rangeItems[0]);
            long rangeEnd = Long.parseLong(rangeItems[1]);
            return new RangePair(rangeStart, rangeEnd);
        }catch (NumberFormatException e){
            System.out.println("Invalid range: " + range);
            throw e;
        }
    }

    private static List<Long> findInvalidIds(RangePair rangePair, LongPredicate isInvalidId) {

        return LongStream.rangeClosed(rangePair.start, rangePair.end)
                .filter(isInvalidId)
                .boxed()
                .toList();
    }

    private static boolean isInvalidDuplicateId(long identifier) {
        String idString = Long.toString(identifier);
        if (idString.length() % 2 == 0) {
            int middle = idString.length() / 2;
            String left = idString.substring(0, middle);
            String right = idString.substring(middle);
            return left.equals(right);
        }
        return false;
    }

    private static boolean isRepeatedPatternId(long identifier) {
        String idString = Long.toString(identifier);
        int middle = idString.length() / 2;
        for (int end = 1; end <= middle; end++) {
            String pattern = idString.substring(0,end);
            int repeats = idString.length() / pattern.length();
            String test = pattern.repeat(repeats);
            if (test.equals(idString)) {
                return true;
            }
        }
        return false;
    }
}
