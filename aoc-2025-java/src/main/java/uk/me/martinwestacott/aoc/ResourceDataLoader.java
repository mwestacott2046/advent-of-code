package uk.me.martinwestacott.aoc;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class ResourceDataLoader {

    public List<String> getDataList(String filename, boolean isTest) {

        String filepath;
        if (isTest) {
            filepath = "/test-data/" + filename;
        } else {
            filepath = "/data/" + filename;
        }

        try {
            return getListFromResource(filepath);
        } catch (URISyntaxException | IOException e) {
            return List.of();
        }
    }



    private List<String> getListFromResource(String name) throws URISyntaxException, IOException {
        Path path = getPath(name);
        return Files.readAllLines(path, StandardCharsets.UTF_8);
    }

    private Path getPath(String name) throws URISyntaxException {
        var url = this.getClass().getResource(name);
        return Paths.get(url.toURI());
    }
}