package PizzaFactory.Pizzerias;

import PizzaFactory.enums.PizzaType;
import PizzaFactory.enums.Place;
import PizzaFactory.Pizza;

public abstract class Pizzeria{
    protected Place place;

    public Pizzeria(Place place){
        this.place = place;
    }

    abstract public Pizza erstellePizza(PizzaType type);
}
