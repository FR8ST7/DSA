import java.util.Scanner;

public class ShapeTest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Shape shape = null;

        while (true) {
            System.out.println("\nChoose a shape to calculate the area:");
            System.out.println("1. Triangle");
            System.out.println("2. Rectangle");
            System.out.println("3. Exit");
            System.out.print("Enter your choice (1/2/3): ");

            int choice = scanner.nextInt();

            if (choice == 3) {
                System.out.println("Exiting...");
                break;
            }

            if (choice == 1) {
                shape = new Triangle();
                System.out.print("Enter base of the triangle: ");
                double base = scanner.nextDouble();
                System.out.print("Enter height of the triangle: ");
                double height = scanner.nextDouble();
                shape.setDimension1(base);
                shape.setDimension2(height);
            } else if (choice == 2) {
                shape = new Rectangle();
                System.out.print("Enter width of the rectangle: ");
                double width = scanner.nextDouble();
                System.out.print("Enter height of the rectangle: ");
                double height = scanner.nextDouble();
                shape.setDimension1(width);
                shape.setDimension2(height);
            } else {
                System.out.println("Invalid choice. Please try again.");
                continue;
            }

            shape.displayArea();
        }

        scanner.close();
    }
}

public abstract class shape {
        protected double dimension1;
        protected double dimension2;
        public void setDimension1(double dimension1) {
            this.dimension1 = dimension1;
        }
        public void setDimension2(double dimension2) {
            this.dimension2 = dimension2;
        }
        public double getDimension1() {
            return dimension1;
        }
        public double getDimension2() {
            return dimension2;
        }
        public abstract void displayArea();
    }
    
    class Triangle extends Shape {

        @Override
        public void displayArea() {
            double area = 0.5 * dimension1 * dimension2; 
            System.out.println("Area of Triangle: " + area);
        }
    }

class Rectangle extends Shape {

    @Override
    public void displayArea() {
        double area = dimension1 * dimension2; // Area of rectangle = width * height
        System.out.println("Area of Rectangle: " + area);
    }
}

