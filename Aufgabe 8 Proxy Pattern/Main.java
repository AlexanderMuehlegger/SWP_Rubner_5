public class Main {
    public static void main(String[] args){
        Drucker drucker = new Drucker();
        drucker.drucken("Test print");

        drucker.drucken("this is colorfull");

        drucker.switchDrucker(new SWDrucker());

        drucker.drucken("This is colorless");
        
    }
}
