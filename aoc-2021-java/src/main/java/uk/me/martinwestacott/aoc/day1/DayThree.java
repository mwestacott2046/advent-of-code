package uk.me.martinwestacott.aoc.day1;

import uk.me.martinwestacott.aoc.CommonUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class DayThree {

    public static void main(String[] args) {
        var lineData = CommonUtils.readData(CommonUtils.getResourceFilePath("day3-input.txt"));

        var powerConsumption = getPowerConsumption(lineData);
        System.out.println("Power Consumption: " + powerConsumption);

        var lifeSupportRating = getLifeSupportRating(lineData);
        System.out.println("Life Support Rating: " + lifeSupportRating);

    }

    private static int getPowerConsumption(List<String> lineData) {
        var digitsLen = lineData.get(0).length();

        StringBuilder gammaRateString = new StringBuilder();
        StringBuilder epsilonRateString = new StringBuilder();

        for (int digit = 0; digit < digitsLen; digit++) {

            int zeroCount = 0;
            int oneCount = 0;
            for (var line : lineData) {

                var digitChar = line.charAt(digit);

                switch (digitChar) {
                    case '0':
                        zeroCount += 1;
                        break;
                    case '1':
                        oneCount += 1;
                        break;
                }
            }

            if (zeroCount > oneCount) {
                gammaRateString.append("0");
                epsilonRateString.append("1");
            } else {
                gammaRateString.append("1");
                epsilonRateString.append("0");
            }
        }

        var gammaRate = Integer.parseInt(gammaRateString.toString(), 2);
        var epsilonRate = Integer.parseInt(epsilonRateString.toString(), 2);

        var powerConsumption = gammaRate * epsilonRate;
        return powerConsumption;
    }


    private static int getLifeSupportRating(List<String> lineData) {
        int oxygenGeneratorRating = getOxygenGeneratorRating(lineData);
        int CO2ScrubberRating = getCO2ScrubberRating(lineData);
        return oxygenGeneratorRating * CO2ScrubberRating;
    }

    private static int getOxygenGeneratorRating(List<String> lineData) {
        List<String> remaining = new ArrayList<>(lineData);

        int pos = 0;
        while (remaining.size() > 1) {

            String filterDigit = findMaxFilterDigit(remaining, pos);
            remaining = filterRemaining(remaining, filterDigit, pos);
            pos++;
        }


        return Integer.parseInt(remaining.get(0), 2);
    }

    private static int getCO2ScrubberRating(List<String> lineData) {
        List<String> remaining = new ArrayList<>(lineData);

        int pos = 0;
        while (remaining.size() > 1) {

            String filterDigit = flipDigit(findMaxFilterDigit(remaining, pos));
            remaining = filterRemaining(remaining, filterDigit, pos);
            pos++;
        }


        return Integer.parseInt(remaining.get(0), 2);
    }



    private static List<String> filterRemaining(List<String> remaining, String filterDigit, int pos) {
        return remaining.stream()
                .filter(line -> filterDigit.equals(Character.toString(line.charAt(pos))))
                .collect(Collectors.toList());
    }

    private static String findMaxFilterDigit(List<String> remaining, int pos) {
        int zeroCount = 0;
        int oneCount = 0;

        for (var line : remaining) {

            var digitChar = line.charAt(pos);

            switch (digitChar) {
                case '0':
                    zeroCount += 1;
                    break;
                case '1':
                    oneCount += 1;
                    break;
            }
        }

        if (zeroCount > oneCount) {
            return "0";
        } else {
            return "1";
        }
    }

    public static String flipDigit (String digit){
        if (digit == "0") {
            return "1";
        }
        return "0";
    }

}
