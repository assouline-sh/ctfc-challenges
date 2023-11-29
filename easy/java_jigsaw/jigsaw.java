import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    System.out.println("What's the flag?: ");
    Scanner in = new Scanner(System.in);
    String input = in.next();
    
    String changed = change(input);
    String flag = "FWI~u6yhuv6bo67uq4qj";
    for (int i = 0; i < flag.length(); i++) {
        if (changed.charAt(i) != flag.charAt(i)) {
            System.out.println("not that...");
            return;
        }
    }
    System.out.println("That flag is correct!");
   }
   
   private static String change(String s) {
    char[] temp = new char[s.length()];
    for(int i = 0; i < s.length(); i++) {
      temp[i] = (char)(s.charAt(i) + 3);
    }
    return new String(temp);
  }
}