package uk.me.martinwestacott.aoc.day1;

import uk.me.martinwestacott.aoc.CommonUtils;

import java.util.ArrayList;
import java.util.List;

public class DayTwo {

    public record Command(String direction, int distance) {
    }

    public record Position(int horizontal, int depth, int aim) {
        public Position(int horizontal, int depth) {
            this(horizontal, depth, 0);
        }
    }

    public Command parseCommand(String data) {
        var split = data.split(" ");
        return new Command(split[0], Integer.valueOf(split[1]));
    }


    public static void main(String[] args) {
        var lineData = CommonUtils.readData(CommonUtils.getResourceFilePath("day2-input.txt"));

        var ops = new DayTwo();
        var commands = lineData.stream()
                .map(line -> ops.parseCommand(line)).toList();

        var position = ops.moveSub(commands);
        var result = position.horizontal * position.depth;

        System.out.println("Part one result: " + result);


        var posWithAim = ops.moveSubWithAim(commands);
        var partTwoResult = posWithAim.horizontal  * posWithAim.depth;
        System.out.println("Part Two result: " + partTwoResult);

    }

    public Position moveSub(List<Command> commands) {
        Position position = new Position(0, 0);

        for (var cmd : commands) {
            position = processCommand(cmd, position);
        }

        return position;
    }

    public Position processCommand(Command cmd, Position position) {

        switch (cmd.direction) {
            case "forward":
                return new Position(position.horizontal + cmd.distance, position.depth);
            case "up":
                return new Position(position.horizontal, position.depth - cmd.distance);
            case "down":
                return new Position(position.horizontal, position.depth + cmd.distance);
        }

        return position;
    }

    public Position processCommandWithAim(Command cmd, Position position) {

        switch (cmd.direction) {
            case "forward":
                return new Position(position.horizontal + cmd.distance, position.depth + (position.aim * cmd.distance), position.aim);
            case "up":
                return new Position(position.horizontal, position.depth,position.aim - cmd.distance);
            case "down":
                return new Position(position.horizontal, position.depth,position.aim + cmd.distance);
        }

        return position;
    }

    public Position moveSubWithAim(List<Command> commands) {
        Position position = new Position(0, 0,0);

        for (var cmd : commands) {
            position = processCommandWithAim(cmd, position);
        }

        return position;
    }

}
