package uk.me.martinwestacott;

import com.google.common.io.Resources;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class CommonUtils {
    public static List<String> readData(String filename){
        List<String> data = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {

            String line = reader.readLine();

            while (line != null) {
                data.add(line);
                line = reader.readLine();
            }

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return data;
    }

    public static String getResourceFilePath(String fileName) {
        var resourceUri = Resources.getResource(fileName);
        return resourceUri.getFile();
    }

}
