public class main {
    public static void main(String[] args){
        Wetterstation station = new Wetterstation();
        Wetterling w1 = new Wetterling("Müller", PublishType.pull);
        Wetterling w2 = new Wetterling("Brigitte", PublishType.push);

        station.joinObvserve(w1);
        station.joinObvserve(w2);

        station.messen();

        station.removeObserve(w1);

        station.messen();
    }
}
