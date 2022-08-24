import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class Cafe {

    public void chaiLatte() {
        System.out.println("Welcome, here is your chai");
    }
    public void americano(String name)  {
        System.out.printf("Welcome %s, here is your chai\n", name);
    }
    //Array
    public void buildMenu() {
        String[] menu={"Chai","Hot Chocolate","Frappuccino"};
        System.out.println(menu[0]);
        System.out.println(Arrays.toString(menu)); //import arrays and use toString method
        for (String item : menu) {  //foreach loop, define the Type name it grab it from the string array
            System.out.println(item);
        }
        int[] numbers= new int[5];
        numbers[0] =10;
        numbers[1]=20;
        //numbers[6]=90; //index is out of bounds for length 5
        //use Exception handling! you still need your app to work
        try{
            numbers[6]=90;
        }
        catch(Exception e){
            System.out.println("keep working on arrays, you goofed it up!");
        }
        System.out.println((Arrays.toString(numbers)));
    }
    //if you want to return an item to the tester, it cannot be public void, it would need to be public ArrayList<String>, because that's the type it returns.
    public void customerList()  {
        ArrayList<String> customers= new ArrayList<>();
        customers.add("Sarah");
        customers.add("Diana");
        customers.add("Jeremy");
        customers.add("Mel");
        customers.remove("Mel");
        customers.remove(2); //will remove Jeremy at idx 2
        System.out.println(customers);
        customers.add("Jamal");
        System.out.println((customers.get(2)));
        System.out.println(customers.size());
    }
    public void customerFavorites(){
        //CallIt<type of key,type of value>
        HashMap<String, String> favorites= new HashMap<>();
        favorites.put("Reena", "Green Tea");
        favorites.put("Mel", "Peach Tea");
        favorites.put("Jeremy", "Sleepy Time Tea");
        favorites.put("Sam", "Dragon Fruit Tea");
        favorites.put("Jess", "Jasmine Tea");
        //use case, I want to know Jeremy's fav tea without using idx
        System.out.println(favorites.get("Jeremy"));
        System.out.println("No of favorites drinks in cafe :\t" + favorites.size());
        //demonstrate that hashmaps are not sequential below, vs array or arrayList
        System.out.println(favorites);

        //print a line that says key with value in a nice sentence, use a foreach loop
        for (String keyName : favorites.keySet()) {
            System.out.printf("%s favorite tea is %s\n", keyName, favorites.get(keyName));
            
        }
    }
}