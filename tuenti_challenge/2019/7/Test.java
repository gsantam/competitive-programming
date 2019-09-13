import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
public class Test {

public static int[] notSoComplexHash(String inputText) {
    int[] hash = new int[16];
    Arrays.fill(hash, (byte) 0x00);
    byte[] textBytes = inputText.getBytes(StandardCharsets.ISO_8859_1);
    for (int i = 0; i < textBytes.length; i++) {
        hash[i % 16] =  (hash[i % 16] + textBytes[i]);
    }
    return hash;
}

   public static void main(String args[]) {
      String Str1 = new String("Subject: Boat;From: Charlie;To: Desmond;------Not Penny's boat");
      int[] my_hash = notSoComplexHash(Str1);
      System.out.println(my_hash[0]);
      
   }
}
