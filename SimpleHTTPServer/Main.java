import com.sun.net.httpserver.Headers;
import com.sun.net.httpserver.HttpServer;

import javax.activation.MimetypesFileTypeMap;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.URLConnection;
import java.net.URI;

public class Main {
    public static void main(String[] args) throws IOException {
        InetSocketAddress inetSocketAddress = new InetSocketAddress(1337);
        HttpServer server = HttpServer.create(inetSocketAddress, 0);
        server.createContext("/", request -> {
                String root = "klient/app";
                URI uri = request.getRequestURI();
                String path = uri.getPath();
                if(path.equals("/")) {
                    path = "/index.html";
                }
                System.out.println("looking for: " + root + path);
                File file = new File(root + path).getCanonicalFile();

                if (!file.isFile()) {
                    // Object does not exist or is not a file: reject with 404 error.
                    String response = "404 (Not Found)\n";
                    request.sendResponseHeaders(404, response.length());
                    OutputStream os = request.getResponseBody();
                    os.write(response.getBytes());
                    os.close();
                } else {
                    // Object exists and is a file: accept with response code 200.
                    MimetypesFileTypeMap map = new MimetypesFileTypeMap();
                    String mime = map.getContentType(file);
                    Headers h = request.getResponseHeaders();
                    h.set("Content-Type", mime);
                    request.sendResponseHeaders(200, 0);

                    OutputStream os = request.getResponseBody();
                    FileInputStream fs = new FileInputStream(file);
                    final byte[] buffer = new byte[0x10000];
                    int count = 0;
                    while ((count = fs.read(buffer)) >= 0) {
                        os.write(buffer, 0, count);
                    }
                    fs.close();
                    os.close();
                }
            });
        server.start();
    }
}
