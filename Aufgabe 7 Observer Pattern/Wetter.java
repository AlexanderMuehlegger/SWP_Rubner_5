public class Wetter {
    private int _temp;
    private int _airHumit;

    public Wetter(int temp, int humitity){
        this._temp = temp;
        this._airHumit = humitity;
    }

    public int get_temp() {
        return this._temp;
    }

    public void set_temp(int _temp) {
        this._temp = _temp;
    }

    public int get_airHumit() {
        return this._airHumit;
    }

    public void set_airHumit(int _airHumit) {
        this._airHumit = _airHumit;
    }

}
