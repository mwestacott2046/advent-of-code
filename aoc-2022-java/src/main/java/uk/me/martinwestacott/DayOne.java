package uk.me.martinwestacott;

import com.google.common.io.Resources;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.OptionalInt;
import java.util.stream.Collectors;

public class DayOne {

    public static void main(String[] args){

        var lineData = CommonUtils.readData(CommonUtils.getResourceFilePath("day1-input.txt"));

        var calories = getElfCalorieCounts(lineData);

        var maxCalories = getMaxCalories(calories);

        System.out.println("Max Calories:" + maxCalories);

        var top3Sum = getTop3Sum(calories);

        System.out.println("Top 3 Calories:" + top3Sum);

    }

    public static int getTop3Sum(List<Integer> calories) {
        var orderedCalories = calories.stream()
                .sorted(Comparator.reverseOrder())
                .collect(Collectors.toList());

        var top3Sum = orderedCalories.subList(0,3).stream().reduce(0,Integer::sum);
        return top3Sum.intValue();
    }

    public static int getMaxCalories(List<Integer> calories) {
        var maxCalories = calories.stream()
                .mapToInt(x ->x)
                .max().orElse(0);
        return maxCalories;
    }


    public static List<Integer> getElfCalorieCounts(List<String> lineData) {
        List<Integer> elfCalories = new ArrayList<>();

        int currentCalories = 0;

        for (var line :lineData) {
            if (line.isEmpty()) {
                elfCalories.add(currentCalories);
                currentCalories =0;
            } else {
                var calorieValue = Integer.valueOf(line);
                currentCalories += calorieValue;
            }
        }

        if (currentCalories >0){
            elfCalories.add(currentCalories);
        }

        return elfCalories;
    }

}
