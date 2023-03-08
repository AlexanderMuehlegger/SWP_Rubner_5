package PizzaFactory;

import PizzaFactory.enums.PizzaType;
import PizzaFactory.enums.Place;

public class main {
    public static void main(String[] args){
        PizzaFactory factory = new PizzaFactory();

        factory.create(Place.Hamburg, PizzaType.Calzone);
        factory.create(Place.Berlin, PizzaType.Calzone);
        factory.create(Place.Rostock, PizzaType.Hawaii);
        factory.create(Place.Hamburg, PizzaType.Salami);
        factory.create(Place.undefined, PizzaType.Calzone);
        factory.create(Place.Rostock, PizzaType.QuattroStagioni);
    }
}
