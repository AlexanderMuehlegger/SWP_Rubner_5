import java.util.HashMap;

public class StationManager {
    private static HashMap<Integer, Wetter> Data = new HashMap<Integer, Wetter>();

    public static void setData(Wetter weather, int id){
        Data.put(id, weather);
    }

    public static Wetter getData(int id){
        return Data.get(id);
    }
}
