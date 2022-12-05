package uk.me.martinwestacott;

import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.function.Function;
import java.util.stream.Collectors;

public class DayFour {

    public record SectionPair(Set<Integer> sectionA, Set<Integer> sectionB) {
    }

    public static void main(String[] args) {
        var data = CommonUtils.readData(CommonUtils.getResourceFilePath("day4-input.txt"));

        var ops = new DayFour();

        var containedCount = ops.getSectionCount(data, ops::isFullyContainedWithin);
        System.out.println("Fully Contained Count: " + containedCount);

        var intersectedCount = ops.getSectionCount(data, ops::isIntersected);
        System.out.println("Intersected Count: " + intersectedCount);
    }

    public int getSectionCount(List<String> data, Function<SectionPair, Boolean> setComparator) {
        return data.stream().map(this::createSection).map(setComparator).filter(val -> val == true).collect(Collectors.toList()).size();
    }

    public SectionPair createSection(String line) {

        var sectionStrings = line.split(",");

        Set<Integer> sectionSetA = createRangeSet(sectionStrings[0]);
        Set<Integer> sectionSetB = createRangeSet(sectionStrings[1]);

        return new SectionPair(sectionSetA, sectionSetB);
    }

    private static Set<Integer> createRangeSet(String sectionStrings) {
        var sectionRange = sectionStrings.split("-");

        Integer lower = Integer.valueOf(sectionRange[0]);
        Integer upper = Integer.valueOf(sectionRange[1]);

        Set<Integer> sectionSet = new HashSet<>();
        for (var i = lower; i <= upper; i++) {
            sectionSet.add(i);
        }
        return sectionSet;
    }


    public boolean isFullyContainedWithin(SectionPair sections) {

        if (sections.sectionA.containsAll(sections.sectionB) || sections.sectionB.containsAll(sections.sectionA)) {
            return true;
        }
        return false;
    }

    public boolean isIntersected(SectionPair sections) {

        Set<Integer> intersection = new HashSet<>(sections.sectionA);
        intersection.retainAll(sections.sectionB);

        if (intersection.isEmpty()) {
            return false;
        }
        return true;
    }

}
