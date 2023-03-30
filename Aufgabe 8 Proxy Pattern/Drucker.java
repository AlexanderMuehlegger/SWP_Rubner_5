public class Drucker implements IDrucker {

    private IDrucker drucker;


    public Drucker(){
        this.drucker = new CLDrucker();
    }

    @Override
    public void drucken(String doc) {
        this.drucker.drucken(doc);
    }

    public void switchDrucker(IDrucker drucker){
        this.drucker = drucker;
    }

}