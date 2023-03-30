public class SWDrucker implements IDrucker {

    @Override
    public void drucken(String doc) {
        System.out.println("SW printing: " + doc);
    }
    
}
