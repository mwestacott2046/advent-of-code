package uk.me.martinwestacott.aoc.day1;

import uk.me.martinwestacott.aoc.CommonUtils;

import java.util.ArrayList;
import java.util.List;

public class DayOne {

    public static void main(String[] args) {
        var lineData = CommonUtils.readData(CommonUtils.getResourceFilePath("day1-input.txt"));

        var values = lineData.stream()
                .map(line -> Integer.valueOf(line)).toList();

        var increases = countIncreases(values);
        System.out.println("Number of Increases: " + increases);

        var windowedIncreases = countWindowedIncreases(values, 3);
        System.out.println("Number of windowed ncreases: " + windowedIncreases);

    }

    public static List<Integer> generateWindowSums(List<Integer> values, int windowSize) {
        List<Integer> windows = new ArrayList<>();

        for (int i = 0; i+ windowSize <= values.size() ; i++) {
            List<Integer> sublist = values.subList(i, i + windowSize);
            var sum = sublist.stream().reduce(0,Integer::sum);
            windows.add(sum);
        }

        return windows;
    }

    public static int countIncreases(List<Integer> dataList) {
        int increases = 0;
        if (dataList.size() > 0) {
            int previous = dataList.get(0);
            for (Integer next : dataList) {
                if (previous < next.intValue()) {
                    increases += 1;
                }
                previous = next.intValue();
            }
        }
        return increases;
    }

    public static int countWindowedIncreases(List<Integer> data, int windowSize) {
        var windows = generateWindowSums(data,windowSize);
        return countIncreases(windows);
    }
}
