package PizzaFactory.Pizzerias;

import PizzaFactory.Pizza;
import PizzaFactory.enums.PizzaType;
import PizzaFactory.enums.Place;

public class BerlinerPizzeria extends Pizzeria{

    public BerlinerPizzeria() {
        super(Place.Berlin);
    }

    @Override
    public Pizza erstellePizza(PizzaType type) {
        return new Pizza(type, this.place)
            .backen()
            .einpacken()
            .scheiden();
    }

}
