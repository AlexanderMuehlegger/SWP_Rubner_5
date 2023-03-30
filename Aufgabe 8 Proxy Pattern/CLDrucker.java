public class CLDrucker implements IDrucker {

    @Override
    public void drucken(String doc) {
        System.out.println("COLOR printing: " + doc);
    }
    
}
