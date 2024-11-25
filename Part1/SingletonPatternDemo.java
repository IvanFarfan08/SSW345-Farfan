public class SingletonPatternDemo {
    public static void main(String[] args) {
        //This is wrong:
        //SingleObject object = new SingleObject();
        //As the constructor is private.

        //Get the only object available.
        SingleObject object = SingleObject.getInstance();

        //Show message
        object.showMessage();
    }
}
