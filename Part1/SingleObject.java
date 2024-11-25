public class SingleObject {

    //Create an object of class SingleObject
    private static SingleObject instance = new SingleObject();

    //Constructor is private so that the class can't be instantiated.
    private SingleObject() {}

    //Get the only object available.
    public static SingleObject getInstance() {
        return instance;
    }

    public void showMessage(){
        System.out.println("Hello World");
    }
}
