/*/
 This file is part of keysmith.
 
 keysmith is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 keysmith is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with keysmith. If not, see <http://www.gnu.org/licenses/>.
/*/


import com.beust.jcommander.JCommander;
import com.beust.jcommander.Parameter;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.LineNumberReader;
import java.io.RandomAccessFile;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;


//*//
public class keysmith {

    /* constants */
    final static int    DEFAULT_DEGREE = 3;
    final static String DEFAULT_WORDS  = "word.list";
    final static String VERSION        = "0.0";


    public static class Options {
        @Parameter
        private List<String> parameters = new ArrayList<String>();
        
        @Parameter(names = { "-h" , "--help" },description = "Show help",help = true)
        private boolean help = false;
        
        @Parameter(names = { "-v" , "--verbose" },description = "Enable verbose messages")
        private boolean verbose = false;
        
        @Parameter(names = { "-V" , "--version" },description = "Print version")
        private boolean version = false;
    }


    private static int countLines ( String filename , boolean countEmpty ) throws IOException {
        int lines = 0;
        LineNumberReader reader = new LineNumberReader(new FileReader(filename));
        for(String line = reader.readLine(); line != null ;line = reader.readLine())
            if (countEmpty || line.compareTo("") != 0) ++lines;
        reader.close();
        return lines;
    }


    //* keysmith *//
    public static void main ( String[] args ) {
        
        /* initialize */
        Options opts = new Options();
        new JCommander(opts,args);
        //jc.setProgramName("keysmith");
        if (opts.parameters.size() > 1 || opts.help) {
            //jc.usage();
            System.exit(0);
        }
        if (opts.version) {
            System.out.println(VERSION);
            System.exit(0);
        }
        int degree = (opts.parameters.size() == 0) ? DEFAULT_DEGREE : Integer.parseInt(opts.parameters.get(0));
        
        
        /* words */
        if (opts.verbose) System.out.print("counting words in "+DEFAULT_WORDS+"...");
        int list = 0;
        try {
            list = countLines(DEFAULT_WORDS,false);
        }
        catch (Exception error) {
            System.err.println("Error: " + error.getMessage());
            System.exit(1);
        }
        if (opts.verbose) System.out.println(list);
        if (list < 2) {
            System.err.println("word list is too short");
            System.exit(1);
        }
        
        
        //* nonces *//
        if (opts.verbose) System.out.print("retrieving random numbers...");
        int[] nonces = new int[degree];
        try {
            
            /* request */
            URL url = new URL("https://www.random.org/integers/?num="+Integer.toString(degree)+"&min=0&max="+Integer.toString(list-1)+"&col=1&base=10&format=plain&rnd=new");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setFollowRedirects(false);
            connection.setUseCaches (false);
            
            /* response */
            BufferedReader incoming = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            for (int i = 0; i < degree ;++i) {
                String line = incoming.readLine();
                if (line == null) {
                    System.err.println("nonce famine");
                    System.exit(1);
                }
                nonces[i] = Integer.parseInt(line);
            }
            incoming.close();
            
            //*//
            if (connection != null) connection.disconnect();
            if (opts.verbose) System.out.println("done");
        }
        catch (Exception error) {
            error.printStackTrace();
            System.exit(1);
        }
        
        
        /* key */
        String key = "";
        if (opts.verbose) System.out.print("generating a key...");
        try {
            RandomAccessFile reader = new RandomAccessFile(DEFAULT_WORDS,"r");
            for (int i = 0; i < degree ;++i) {
                String word = "";
                for (int index = nonces[i]; index >= 0 ;--index) {
                    word = reader.readLine();
                    
                    if (word == null) {
                        System.err.println("nonce famine");
                        System.exit(1);
                    }
                    if (word.compareTo("") == 0) ++index;
                }
                key += word;
                reader.seek(0);
            }
            reader.close();
        }
        catch (Exception error) {
            error.printStackTrace();
            System.exit(1);
        }
        System.out.println(key);
        
        
        //*//
    }

}
