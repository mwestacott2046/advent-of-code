package uk.me.martinwestacott.aoc.challanges;

import uk.me.martinwestacott.aoc.ResourceDataLoader;

import java.util.List;

public class DayOne {

    public static void main(String[] args) {
        List<String> data = new ResourceDataLoader().getDataList("aoc-2025-day1.txt", false);

        if (!data.isEmpty()) {
            System.out.println("Part One Visits at zero: " + calcZeroVisitsPartOne(data));

            System.out.println("Part Two Visits at zero: " + calcZeroVisitsPartTwo(data));
        }
    }

    private static int calcZeroVisitsPartOne(List<String> data) {
        int dialPosition = 50;
        int zeroVisits = 0;
        for (String line : data) {
            int moveBy = getMoveValue(line);
            int movedTo = dialPosition + moveBy;
            if (movedTo < 0) {
                dialPosition = (100 + movedTo) % 100;
            } else {
                dialPosition = movedTo % 100;
            }
            zeroVisits += countDialAtZero(dialPosition);
        }
        return zeroVisits;
    }

    private static int calcZeroVisitsPartTwo(List<String> data) {
        int dialPosition = 50;
        int zeroVisits = 0;
        for (String line : data) {
            int moveBy = getMoveValue(line);

            int movedTo = dialPosition + moveBy;
            if (movedTo < 0) {
                while (movedTo < -100) {
                    movedTo += 100;
                    zeroVisits += 1;
                }
                if (movedTo < 0 && dialPosition != 0) {
                    zeroVisits += 1;
                }
                dialPosition = (100 + movedTo) % 100;
            } else {
                while (movedTo > 100) {
                    zeroVisits +=1;
                    movedTo -=100;
                }

                dialPosition = movedTo % 100;
            }
            zeroVisits += countDialAtZero(dialPosition);
        }
        return zeroVisits;
    }

    private static int getMoveValue(String line) {
        int moveBy = Integer.parseInt(line.substring(1));
        return line.charAt(0) == 'L' ? moveBy * -1 : moveBy;
    }

    private static int countDialAtZero(int dialPosition) {
        return 0 == dialPosition ? 1 : 0;
    }
}
