import java.util.ArrayList;
import java.util.Random;

public class Wetterstation {

    private ArrayList<Wetterling> _wetterlings;
    private final int _stationID;
    
    public Wetterstation(){
        this._wetterlings = new ArrayList<Wetterling>();
        Random random = new Random();
        this._stationID = random.nextInt((9999999-1000000) + 1) + 1000000;
    }

    public void messen(){
        Wetter weather = this._messen();
        StationManager.setData(weather, this._stationID);
        this.alert();
    }

    private Wetter _messen(){
        Random random = new Random();
        return new Wetter(random.nextInt(30), random.nextInt(100));
    }

    private void alert(){
        for(Wetterling wetterling : this._wetterlings){
            wetterling.alert(this._stationID);
        }
    }

    public void removeObserve(Wetterling wetterling){
        this._wetterlings.remove(wetterling);
        System.out.println(wetterling.getName() + " remove from Observer");
    }
    
    public void joinObvserve(Wetterling wetterling) {
        this._wetterlings.add(wetterling);
        System.out.println(wetterling.getName() + " added to Observer");
    }
    
}

enum PublishType{
    pull, push, undefined
}
