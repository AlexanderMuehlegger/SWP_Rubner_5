package PizzaFactory.Pizzerias;

import PizzaFactory.Pizza;
import PizzaFactory.enums.PizzaType;
import PizzaFactory.enums.Place;

public class RosstockPizzeria extends Pizzeria{
    
    public RosstockPizzeria() {
        super(Place.Rostock);
    }

    @Override
    public Pizza erstellePizza(PizzaType type) {
        return new Pizza(type, this.place)
            .backen()
            .einpacken()
            .scheiden();
    }
}
