package uk.me.martinwestacott;

import com.google.common.base.Strings;

import java.util.*;
import java.util.stream.Stream;

public class DayThree {

    private static int lowercaseA = 97;
    private static int lowercaseZ = 122;
    private static int uppercaseA = 65;
    private static int uppercaseZ = 90;

    public List<String> splitBag(String bag) {
        var mid = bag.length() / 2;
        return Arrays.asList(bag.substring(0, mid), bag.substring(mid));
    }

    public String findFirstDuplicate(String item1, String item2) {
        var searchTerms = item1.split("");
        for (var item : searchTerms) {
            if (item2.contains(item)) {
                return item;
            }
        }
        return "";
    }

    public int getPriority(String item) {
        if (Strings.isNullOrEmpty(item)) {
            return 0;
        }

        var charItem = item.charAt(0);
        var code = (int) charItem;

        if (code >= lowercaseA && code <= lowercaseZ) {
            return code - (lowercaseA - 1);
        }

        if (code >= uppercaseA && code <= uppercaseZ) {
            return 27 + (code - uppercaseA);
        }

        return 0;
    }

    public static void main(String[] args) {
        var data = CommonUtils.readData(
                CommonUtils.getResourceFilePath("day3-input.txt")
        );
        var ops = new DayThree();

        int priorityResult = ops.getReorganisationPriorities(data);
        System.out.println("Total Priorities Sum: " + priorityResult);


        int badgeResult = ops.getGroupBadgePriorities(data);
        System.out.println("Badge Priorities Sum: " + badgeResult);

    }


    public int getReorganisationPriorities(List<String> data) {
        var result = data.stream()
                .map(bag -> splitBag(bag))
                .map(compartments -> findFirstDuplicate(compartments.get(0), compartments.get(1)))
                .map(duplicate -> getPriority(duplicate))
                .reduce(Integer::sum).orElse(0);

        return result;
    }

    public int getGroupBadgePriorities(List<String> data) {
        var groups = groupBags(data, 3);

        var result = groups.stream().map(grp -> findBadge(grp))
                .map(badge -> getPriority(badge))
                .reduce(Integer::sum).orElse(0);
        return result;
    }

    public List<List<String>> groupBags(List<String> data, int groupSize) {

        List<List<String>> groups = new ArrayList<>();

        Stream.iterate(0, n -> n < data.size(), n -> n + groupSize)
                .forEach(n -> {
                    groups.add(data.subList(n, n + groupSize));
                });

        return groups;
    }

    public String findBadge(List<String> bags) {

        var searchItems = new HashSet<String>(Arrays.stream(bags.get(0).split("")).toList());
        var bag2 = bags.get(1);
        var bag3 = bags.get(2);

        for (var item : searchItems) {
            if (bag2.contains(item) && bag3.contains(item)) {
                return item;
            }
        }

        return "";
    }
}
