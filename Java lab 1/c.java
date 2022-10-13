import java.util.Scanner;
public class c {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double x = scanner.nextDouble();
        double y = scanner.nextDouble();
        double z = scanner.nextDouble();
        double q = x * y * z;
        String e = String.format("%.1f" , q / 1000000000);
        System.out.print(e);
    }
    
}
