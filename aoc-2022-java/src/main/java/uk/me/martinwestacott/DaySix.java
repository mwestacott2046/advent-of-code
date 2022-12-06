package uk.me.martinwestacott;

public class DaySix {
    public static void main(String[] args) {
        var data = CommonUtils.readData(CommonUtils.getResourceFilePath("day6-input.txt"));

        DaySix ops = new DaySix();
        int charsToStart = ops.findStartOfPacketMarker(data.get(0), 4);
        System.out.println("Start of Packet (4) chars required: " + charsToStart);

        int charsToStart14 = ops.findStartOfPacketMarker(data.get(0), 14);
        System.out.println("Start of Packet (14) chars required: " + charsToStart14);
    }

    public int findStartOfPacketMarker(String dataStream, int markerLength) {

        int pos = 0;
        while (pos < dataStream.length()- markerLength){

            var buffer = dataStream.substring(pos, pos + markerLength);

            if (isUnique(buffer)){
                return pos + markerLength;
            }

            pos++;
        }

        return -1;
    }

    public boolean isUnique(String buffer) {

        for (int i = 0; i < buffer.length() -1; i++) {
            char charA = buffer.charAt(i);
            for (int j = i + 1; j < buffer.length(); j++) {
                char charB = buffer.charAt(j);
                if (charA == charB){
                    return false;
                }
            }
        }

        return true;
    }
}
