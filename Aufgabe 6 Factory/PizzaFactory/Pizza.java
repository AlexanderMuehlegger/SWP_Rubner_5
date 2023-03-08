package PizzaFactory;

import PizzaFactory.enums.PizzaType;
import PizzaFactory.enums.Place;

public class Pizza {
    private PizzaType type;
    private Place place;

    public Pizza(PizzaType type, Place place){
        this.type = type;
        this.place = place;
    }

    public Pizza backen(){
        System.out.println(this.place.name() + this.type.name() + " wird gebacken!");
        return this;
    }
    
    public Pizza scheiden(){
        System.out.println(this.place.name() + this.type.name() + " wird geschnitten!");
        return this;
    }
    
    public Pizza einpacken(){
        System.out.println(this.place.name() + this.type.name() + " wird eingepackt!");
        return this;
    }
}

