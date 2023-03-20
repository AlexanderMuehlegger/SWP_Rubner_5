import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Wetterstation {

    private PublishType _type; 
    private Wetter _weather;
    private ArrayList<Wetterling> _wetterlings;
    
    public Wetterstation(PublishType type){
        this._type = type;
        this._wetterlings = new ArrayList<Wetterling>();
    }

    public void messen(){
        this._weather = this._messen();
        this.alert();
    }

    private Wetter _messen(){
        Random random = new Random();
        return new Wetter(random.nextInt(30), random.nextInt(100));
    }

    private void alert(){
        for(Wetterling wetterling : this._wetterlings){
            
        }
    }

    public void publish(){
        switch(this._type){
            case pull:
                this.publish_pull();
                break;
            case push:
                this.publish_push();
                break;
            default:
                System.err.println("ERROR: 2318237198");
        }
        
    }

    private void publish_pull(){
        Scanner scanner = new Scanner(System.in);

        System.out.println("NEW DATA AWAILABLE!!!!!\nWant to see it now?(y/n)");
        String input = scanner.next();

        if(input.equals("y")){
            System.out.printf("current Temp: %d\ncurrent humitity: %d%\n", this._weather.get_temp(), this._weather.get_airHumit());
        }

        scanner.close();
    }

    private void publish_push(){
        System.out.printf("New DATA:\ncurrent Temp: %d\ncurrent humitity: %d%\n", this._weather.get_temp(), this._weather.get_airHumit());
    }
}

enum PublishType{
    pull, push, undefined
}
