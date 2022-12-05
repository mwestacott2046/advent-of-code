package uk.me.martinwestacott;

import java.util.*;
import java.util.stream.Collectors;

public class DayFive {

    public class Crane {
        private int maxStacks;
        private List<Stack<String>> stacks;

        public Crane(int maxStacks, List<List<String>> stackLists) {
            this.maxStacks = maxStacks;
            this.stacks = new ArrayList<>();

            for (int i = 0; i < maxStacks; i++) {

                Stack<String> stack = new Stack<>();
                var data = stackLists.get(i);
                Collections.reverse(data);

                data.forEach(item -> stack.push(item));

                this.stacks.add(stack);
            }
        }

        public void moveCrates(int count, int from, int to) {

            for (int i = 0; i < count; i++) {
                var crate = stacks.get(from - 1).pop();
                stacks.get(to - 1).push(crate);
            }
        }

        public void moveCrates9001(int count, int from, int to) {

            ArrayList<String> movedCrates = new ArrayList<>();
            for (int i = 0; i < count; i++) {
                movedCrates.add(stacks.get(from - 1).pop());
            }
            if (count > 1) {
                Collections.reverse(movedCrates);
            }
            for (var crate : movedCrates) {
                stacks.get(to - 1).push(crate);
            }
        }

        public String readStackTops() {
            StringBuilder builder = new StringBuilder();
            for (int i = 0; i < maxStacks; i++) {
                builder.append(stacks.get(i).peek());
            }

            return builder.toString();
        }

        public List<Stack<String>> getStacks() {
            return stacks;
        }

    }

    public record MoveCommand(int count, int from, int to) {
    }

    public record CraneWithMoves(Crane crane, List<MoveCommand> moves) {
    }


    public static void main(String[] args) {
        var data = CommonUtils.readData(CommonUtils.getResourceFilePath("day5-input.txt"));

        var ops = new DayFive();

        var craneState = ops.loadInitialState(data);
        craneState.moves().stream().forEach(move -> ops.processMove(move, craneState.crane()));
        System.out.println("Stack Tops: " + craneState.crane.readStackTops());

        var craneState2 = ops.loadInitialState(data);
        craneState2.moves().stream().forEach(move -> ops.processMove9001(move, craneState2.crane()));
        System.out.println("Stack Tops 9001: " + craneState2.crane.readStackTops());

    }

    private void processMove(MoveCommand move, Crane crane) {
        crane.moveCrates(move.count, move.from, move.to);
    }

    private void processMove9001(MoveCommand move, Crane crane) {
        crane.moveCrates9001(move.count, move.from, move.to);
    }

    public CraneWithMoves loadInitialState(List<String> data) {

        int currentRow = 0;
        while (!data.get(currentRow).isEmpty()) {
            currentRow++;
        }

        var stackNumbers = Arrays.stream(data.get(currentRow - 1).split(" "))
                .filter(str -> !str.isEmpty())
                .map(digit -> Integer.valueOf(digit))
                .collect(Collectors.toList());

        var maxStack = stackNumbers.stream().max(Integer::compare).orElse(0);

        var craneData = data.subList(0, currentRow - 1);
        var movesData = data.subList(currentRow + 1, data.size());

        List<MoveCommand> moveCommands = movesData.stream()
                .map(line -> decodeMove(line))
                .collect(Collectors.toList());


        var stacks = loadStackData(craneData, maxStack);

        return new CraneWithMoves(new Crane(maxStack, stacks), moveCommands);
    }

    public MoveCommand decodeMove(String line) {
        var items = line.split(" ");
        return new MoveCommand(Integer.valueOf(items[1]), Integer.valueOf(items[3]), Integer.valueOf(items[5]));
    }

    public List<List<String>> loadStackData(List<String> stackData, int maxStack) {
        List<List<String>> stacks = new ArrayList<>();
        for (int i = 0; i < maxStack; i++) {
            stacks.add(new ArrayList<>());
        }

        int startCol = 1;
        for (var line : stackData) {

            for (int i = 0; i < maxStack; i++) {
                int col = startCol + (i * 4);
                if (col < line.length()) {
                    char charVal = line.charAt(col);
                    if (!Character.isWhitespace(charVal)) {
                        stacks.get(i).add(Character.toString(charVal));
                    }
                }
            }
        }

        return stacks;
    }

}
