// Class name must = file name
// Class name must be Pascal cased - First letter of every word is capatilized

public class HelloWorld { 
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}

// Keep in mind of Public & Static for OOP
// Method - A function that belongs to a Class (Everything in Java must belong to a class! Therefore all functions are methods.)
// main (method) - entry point that is required for any java file intended to be run from the command line.
// Void (return type) > String[] (Array of strings) + arguments > System (In every class) > Out (A variable of Print.stream class) > println (accepts the string)
// String (return type) > return "string"

// Public - accessible from other classes, Static - method that is called from the class itself not from an instance, void - main() method doesn't run
// Compile(Make it readable) class by typing in: javac filename
// Run in cmd by typing in: java filename