package PizzaFactory;

import PizzaFactory.Pizzerias.BerlinerPizzeria;
import PizzaFactory.Pizzerias.HamburgPizzeria;
import PizzaFactory.Pizzerias.Pizzeria;
import PizzaFactory.Pizzerias.RosstockPizzeria;
import PizzaFactory.enums.PizzaType;
import PizzaFactory.enums.Place;

public class PizzaFactory {
    private Pizzeria hamburg;
    private Pizzeria berlin;
    private Pizzeria rosstock;

    public PizzaFactory(){
        this.hamburg = new HamburgPizzeria();
        this.berlin = new BerlinerPizzeria();
        this.rosstock = new RosstockPizzeria();
    }

    public void create(Place place, PizzaType type){
        switch(place){
            case Hamburg:
                this.hamburg.erstellePizza(type);
                break;
            case Berlin:
                this.berlin.erstellePizza(type);
                break;
            case Rostock:
                this.rosstock.erstellePizza(type);
                break;
            case undefined:
                System.err.println("ERROR: hkdie-7892729");
        }
    }
}
