import java.util.Scanner;

public class Wetterling{
    private PublishType _type;
    private String _name;

    public String getName(){
        return this._name;
    }

    public Wetterling(String name, PublishType type){
        this._name = name;
        this._type = type;
    }

    public void alert(int stationID){
        switch(this._type){
            case pull:
                this.publish_pull(stationID);
                break;
            case push:
                this.publish_push(StationManager.getData(stationID));
                break;
            default:
                System.err.println("ERROR: 2318237198");
        }
    }

    private void publish_pull(int id){
        Scanner scanner = new Scanner(System.in);

        System.out.println(this._name + " NEW DATA AWAILABLE!!!!!\nWant to see it now?(y/n)");
        String input = scanner.next();

        if(input.equals("y")){
            Wetter weather = StationManager.getData(id);
            System.out.printf("current Temp: %d\ncurrent humitity: %d%s\n\n", weather.get_temp(), weather.get_airHumit(), "%");
        }

        scanner.close();
    }

    private void publish_push(Wetter weather){
        System.out.printf(this._name + " new DATA:\ncurrent Temp: %d\ncurrent humitity: %d%s\n\n", weather.get_temp(), weather.get_airHumit(), "%");
    }

}