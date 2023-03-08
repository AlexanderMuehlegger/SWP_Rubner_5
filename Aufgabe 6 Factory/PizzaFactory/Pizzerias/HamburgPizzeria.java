package PizzaFactory.Pizzerias;

import PizzaFactory.Pizza;
import PizzaFactory.enums.PizzaType;
import PizzaFactory.enums.Place;

public class HamburgPizzeria extends Pizzeria {
    

    public HamburgPizzeria() {
        super(Place.Hamburg);
    }

    @Override
    public Pizza erstellePizza(PizzaType type) {
        return new Pizza(type, this.place)
            .backen()
            .einpacken()
            .scheiden();
    }
}
